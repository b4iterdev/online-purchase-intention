import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix,
    classification_report, RocCurveDisplay, PrecisionRecallDisplay
)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

os.makedirs('outputs', exist_ok=True)
os.makedirs('reports', exist_ok=True)

# 1. Load data
print("--> Loading dataset...")
df = pd.read_csv('data/online_shoppers_intention.csv')

# Check duplicates and missing values
dups = df.duplicated().sum()
if dups > 0:
    print(f"Removing {dups} duplicate rows.")
    df = df.drop_duplicates().reset_index(drop=True)

# Clean target
y = df['Revenue'].astype(int)
X = df.drop(columns=['Revenue'])

# Identify feature groups
categorical_cols = ['Month', 'VisitorType', 'Weekend']
# OperatingSystems, Browser, Region, TrafficType are encoded as integers but are categorical concepts
discrete_categorical_cols = ['OperatingSystems', 'Browser', 'Region', 'TrafficType']
# Group rare categories or treat them as categorical
for col in discrete_categorical_cols:
    X[col] = X[col].astype(str)

all_cat_cols = categorical_cols + discrete_categorical_cols
numeric_cols = [c for c in X.columns if c not in all_cat_cols]

print(f"Numerical features ({len(numeric_cols)}): {numeric_cols}")
print(f"Categorical features ({len(all_cat_cols)}): {all_cat_cols}")

# 2. EDA Summary & Plots
print("--> Generating EDA charts...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Target Distribution
sns.countplot(x=y, ax=axes[0], palette='Blues_d')
axes[0].set_title('Target Distribution (Revenue: 0 = No, 1 = Yes)')
axes[0].set_xlabel('Revenue')
axes[0].set_ylabel('Count')
for p in axes[0].patches:
    axes[0].annotate(f'{p.get_height()} ({p.get_height()/len(y):.1%})',
                     (p.get_x() + p.get_width() / 2., p.get_height() / 2),
                     ha='center', va='center', color='white', fontweight='bold')

# PageValues vs Revenue
sns.boxplot(x=y, y=X['PageValues'], ax=axes[1], palette='Set2')
axes[1].set_yscale('log')
axes[1].set_title('PageValues (Log scale) vs Revenue')
axes[1].set_xlabel('Revenue')
axes[1].set_ylabel('PageValues (log scale)')
plt.tight_layout()
plt.savefig('outputs/eda_overview.png', dpi=200)
plt.close()

# Correlation Matrix of Numerical Features
plt.figure(figsize=(10, 8))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, square=True)
plt.title('Correlation Matrix (Numeric Features)')
plt.tight_layout()
plt.savefig('outputs/correlation_matrix.png', dpi=200)
plt.close()

# 3. Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train size: {X_train.shape}, Test size: {X_test.shape}")

# 4. Preprocessor setup
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), all_cat_cols)
    ]
)

# 5. Define 5 Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=7, weights='distance'),
    "Decision Tree": DecisionTreeClassifier(max_depth=6, class_weight='balanced', random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=150, max_depth=12, class_weight='balanced', random_state=42, n_jobs=-1),
    "SVM": SVC(kernel='rbf', C=1.0, probability=True, class_weight='balanced', random_state=42)
}

# 6. Evaluation Loop
results = []
trained_pipelines = {}

print("--> Training and evaluating models...")
for name, clf in models.items():
    print(f"--- Training {name} ---")
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', clf)
    ])
    
    # 5-fold Stratified Cross-Validation on Train set
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_validate(
        pipe, X_train, y_train, cv=cv,
        scoring=['f1', 'roc_auc', 'precision', 'recall'],
        n_jobs=-1
    )
    
    # Train on full train set, evaluate on holdout test set
    pipe.fit(X_train, y_train)
    trained_pipelines[name] = pipe
    
    y_pred = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:, 1] if hasattr(pipe.named_steps['classifier'], "predict_proba") else None
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_proba) if y_proba is not None else np.nan
    pr_auc = average_precision_score(y_test, y_proba) if y_proba is not None else np.nan
    
    results.append({
        'Model': name,
        'CV_F1_Mean': cv_scores['test_f1'].mean(),
        'CV_F1_Std': cv_scores['test_f1'].std(),
        'CV_ROC_AUC_Mean': cv_scores['test_roc_auc'].mean(),
        'Test_Accuracy': acc,
        'Test_Precision': prec,
        'Test_Recall': rec,
        'Test_F1': f1,
        'Test_ROC_AUC': roc_auc,
        'Test_PR_AUC': pr_auc
    })

res_df = pd.DataFrame(results)
print("\n=== Model Benchmark Results ===")
print(res_df.to_string(index=False))
res_df.to_csv('outputs/benchmark_results.csv', index=False)

# 7. Visualization of Results
# Bar plot for Test F1, Precision, Recall, ROC-AUC
metrics_to_plot = ['Test_Accuracy', 'Test_Precision', 'Test_Recall', 'Test_F1', 'Test_ROC_AUC']
df_melt = res_df.melt(id_vars=['Model'], value_vars=metrics_to_plot, var_name='Metric', value_name='Score')

plt.figure(figsize=(12, 6))
sns.barplot(data=df_melt, x='Model', y='Score', hue='Metric', palette='viridis')
plt.title('Comparison of 5 Models on Test Set')
plt.ylim(0, 1.05)
plt.ylabel('Score')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig('outputs/model_comparison_bar.png', dpi=200)
plt.close()

# ROC Curve Comparison
plt.figure(figsize=(8, 6))
for name, pipe in trained_pipelines.items():
    RocCurveDisplay.from_estimator(pipe, X_test, y_test, name=name, ax=plt.gca())
plt.plot([0, 1], [0, 1], 'k--', label='Random Chance')
plt.title('ROC Curves on Test Set')
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('outputs/roc_curves.png', dpi=200)
plt.close()

# Precision-Recall Curve Comparison
plt.figure(figsize=(8, 6))
for name, pipe in trained_pipelines.items():
    PrecisionRecallDisplay.from_estimator(pipe, X_test, y_test, name=name, ax=plt.gca())
plt.title('Precision-Recall Curves on Test Set')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('outputs/pr_curves.png', dpi=200)
plt.close()

# Confusion Matrices for all 5 models
fig, axes = plt.subplots(1, 5, figsize=(22, 4))
for idx, (name, pipe) in enumerate(trained_pipelines.items()):
    y_pred = pipe.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], cbar=False)
    axes[idx].set_title(name)
    axes[idx].set_xlabel('Predicted')
    axes[idx].set_ylabel('Actual' if idx == 0 else '')
plt.suptitle('Confusion Matrices on Test Set', y=1.05, fontsize=14)
plt.tight_layout()
plt.savefig('outputs/confusion_matrices.png', dpi=200)
plt.close()

# Feature Importance for Random Forest
rf_model = trained_pipelines['Random Forest'].named_steps['classifier']
feature_names = trained_pipelines['Random Forest'].named_steps['preprocessor'].get_feature_names_out()
importances = rf_model.feature_importances_
top_idx = np.argsort(importances)[-15:]

plt.figure(figsize=(10, 6))
plt.barh(range(len(top_idx)), importances[top_idx], align='center', color='teal')
plt.yticks(range(len(top_idx)), [feature_names[i].replace('num__', '').replace('cat__', '') for i in top_idx])
plt.xlabel('Feature Importance')
plt.title('Top 15 Most Important Features (Random Forest)')
plt.tight_layout()
plt.savefig('outputs/rf_feature_importance.png', dpi=200)
plt.close()

print("--> Pipeline run complete. Outputs saved to `outputs/`.")
