---
marp: true
theme: default
size: 16:9
paginate: true
header: "Online Purchase Intention Prediction | Machine Learning Coursework"
footer: "Faculty of Computer Science • Phenikaa University"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
  section {
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    padding: 40px 60px;
    background: #fafaf9;
    color: #1c1917;
    font-size: 18px;
    line-height: 1.5;
  }
  h1 {
    font-size: 38px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
  }
  h2 {
    font-size: 28px;
    font-weight: 700;
    color: #1e293b;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-bottom: 18px;
  }
  h3 {
    font-size: 20px;
    font-weight: 600;
    color: #0369a1;
    margin-bottom: 6px;
  }
  .tag {
    display: inline-block;
    padding: 3px 10px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: 999px;
    background: #e0f2fe;
    color: #0369a1;
    margin-bottom: 12px;
  }
  .split {
    display: grid;
    grid-template-columns: 1fr 1.25fr;
    gap: 36px;
    align-items: start;
  }
  .split-even {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 28px;
    align-items: start;
  }
  .stat-hero {
    border-left: 4px solid #0284c7;
    padding-left: 16px;
    margin: 14px 0;
  }
  .stat-num {
    font-size: 38px;
    font-weight: 800;
    color: #0369a1;
    line-height: 1;
  }
  .stat-desc {
    font-size: 14px;
    color: #64748b;
    margin-top: 4px;
  }
  .step-row {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    margin-bottom: 14px;
  }
  .step-badge {
    min-width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #0284c7;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 13px;
    margin-top: 2px;
  }
  .step-content strong {
    color: #0f172a;
    display: block;
    font-size: 16px;
  }
  .step-content p {
    font-size: 14px;
    color: #475569;
    margin: 2px 0 0 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 15px;
    margin-top: 10px;
    background: #ffffff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  th {
    background: #0f172a;
    color: #ffffff;
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
  }
  td {
    padding: 9px 14px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
  }
  tr:last-child td {
    border-bottom: none;
  }
  .highlight-row {
    background: #f0f9ff;
    font-weight: 700;
    color: #0369a1;
  }
  .footer-clean {
    font-size: 14px;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 10px;
    margin-top: 14px;
  }
---

<!-- Slide 1: Title Slide -->
<!-- _header: "" -->
<!-- _footer: "" -->

<span class="tag">Machine Learning Final Project</span>

# Online Purchase Intention Prediction
### A Comparative Benchmark of 5 Supervised Classifiers

<div class="stat-hero">
  <div style="font-size: 17px; color: #334155; line-height: 1.5;">
    How clickstream behavior, Google Analytics indicators, and class balancing strategies predict customer checkouts in e-commerce.
  </div>
</div>

<div style="margin-top: 48px; border-top: 1px solid #e2e8f0; padding-top: 18px; display: flex; gap: 48px;">
  <div>
    <div style="font-size: 13px; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Authors</div>
    <div style="font-weight: 700; color: #0f172a;">Hoàng Văn Đô (24107948)</div>
    <div style="font-weight: 700; color: #0f172a;">Phan Hoàng Nhật (24100092)</div>
  </div>
  <div>
    <div style="font-size: 13px; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Faculty</div>
    <div style="color: #334155;">Faculty of Computer Science</div>
    <div style="color: #64748b; font-size: 14px;">Phenikaa University, Hanoi</div>
  </div>
  <div>
    <div style="font-size: 13px; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Dataset & Code</div>
    <div style="color: #0369a1; font-weight: 600;">UCI Shoppers Intention (12.3k sessions)</div>
    <div style="color: #64748b; font-size: 14px;">Scikit-Learn Python Pipeline</div>
  </div>
</div>

---

<!-- Slide 2: The Problem Context -->
## The E-Commerce Conversion Dilemma

<div class="split">
  <div>
    <div class="stat-hero">
      <div class="stat-num">~15.5%</div>
      <div class="stat-desc">Actual purchasing sessions in dataset (84.5% leave without buying)</div>
    </div>
    <p style="color: #475569; font-size: 15px; margin-top: 14px;">
      In online retail, millions browse but few buy. Intervening with discounts or live chat on every user causes huge profit leakage. Intervening on nobody loses high-value customers.
    </p>
    <div style="background: #e0f2fe; border-radius: 8px; padding: 12px 16px; margin-top: 18px;">
      <strong style="color: #0369a1; font-size: 14px;">Goal:</strong>
      <div style="color: #0c4a6e; font-size: 14px;">Predict purchase intention in real-time so merchants can intervene only when it matters.</div>
    </div>
  </div>

  <div>
    <div class="step-row">
      <div class="step-badge">1</div>
      <div class="step-content">
        <strong>The Accuracy Paradox</strong>
        <p>A naive model predicting "Nobody Buys" gets 84.5% accuracy but zero business value. We must optimize F1, Recall & PR-AUC.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">2</div>
      <div class="step-content">
        <strong>High Dimensional Sparsity</strong>
        <p>Combining numeric analytics with categorical sources (browser, OS, months) expands feature space to 68 dimensions after one-hot encoding.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">3</div>
      <div class="step-content">
        <strong>Five Fundamental Models Tested</strong>
        <p>Logistic Regression, KNN, Decision Tree, Random Forest, and SVM evaluated side-by-side.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 3: Dataset Anatomy -->
## UCI Dataset & Feature Architecture

<div class="split">
  <div>
    <img src="../outputs/eda_overview.png" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />
    <div style="font-size: 12px; color: #64748b; text-align: center; margin-top: 6px;">
      Left: 84.5% vs 15.5% Class Imbalance | Right: Log-scale distribution of PageValues
    </div>
  </div>

  <div>
    <h3 style="color: #0f172a; margin-top: 0;">12,205 Clean Unique Sessions</h3>
    <div style="font-size: 14px; color: #475569; line-height: 1.6;">
      <p><strong>10 Numerical Behavioral Features:</strong><br/>
      • Page counts & browsing durations: <code>Administrative</code>, <code>Informational</code>, <code>ProductRelated</code>.<br/>
      • Web analytics: <code>BounceRates</code>, <code>ExitRates</code>, <code>PageValues</code>, <code>SpecialDay</code>.</p>
      <p><strong>7 Categorical Session Contexts:</strong><br/>
      • User context: <code>VisitorType</code>, <code>OperatingSystems</code>, <code>Browser</code>, <code>Region</code>.<br/>
      • Temporal cues: <code>Month</code>, <code>Weekend</code>, <code>TrafficType</code>.</p>
    </div>
    <div class="stat-hero" style="border-color: #f59e0b;">
      <div style="font-size: 14px; font-weight: 700; color: #b45309;">Key Domain Finding:</div>
      <div style="font-size: 13px; color: #78350f;">PageValues is non-zero almost exclusively for users who complete checkout.</div>
    </div>
  </div>
</div>

---

<!-- Slide 4: End-to-End Preprocessing Pipeline -->
## Leakage-Free Preprocessing Pipeline

<div class="split-even">
  <div>
    <div class="step-row">
      <div class="step-badge">A</div>
      <div class="step-content">
        <strong>Data Cleansing</strong>
        <p>Removed 125 exact duplicate sessions. Zero missing values detected across all 18 columns.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">B</div>
      <div class="step-content">
        <strong>Stratified 80/20 Holdout Split</strong>
        <p>9,764 training sessions vs 2,441 test sessions. Preserved exact 15.5% positive ratio in both partitions.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">C</div>
      <div class="step-content">
        <strong>ColumnTransformer Integration</strong>
        <p>Numerical scaled via <code>StandardScaler</code>; Categorical transformed via <code>OneHotEncoder(handle_unknown='ignore')</code>.</p>
      </div>
    </div>
  </div>

  <div>
    <div class="step-row">
      <div class="step-badge">D</div>
      <div class="step-content">
        <strong>Class Imbalance Compensation</strong>
        <p>Employed inverse class frequency penalties inside loss functions: $w_j = \frac{N}{2 \times N_j}$. Prevents models from ignoring the rare positive class.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">E</div>
      <div class="step-content">
        <strong>Stratified 5-Fold Cross Validation</strong>
        <p>All hyperparameter stability tested with 5-fold CV before evaluating against holdout test data.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 5: Benchmark Results Table -->
## Benchmark Results on Holdout Test Set

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1-Score</th>
      <th>ROC-AUC</th>
      <th>PR-AUC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Logistic Regression</strong></td>
      <td>84.60%</td>
      <td>0.5050</td>
      <td>0.7958</td>
      <td>0.6179</td>
      <td>0.9097</td>
      <td>0.6627</td>
    </tr>
    <tr>
      <td><strong>K-Nearest Neighbors (k=7)</strong></td>
      <td>87.67%</td>
      <td><strong>0.6901</strong></td>
      <td>0.3848</td>
      <td>0.4941</td>
      <td>0.8270</td>
      <td>0.5717</td>
    </tr>
    <tr>
      <td><strong>Decision Tree (CART, d=6)</strong></td>
      <td>83.78%</td>
      <td>0.4892</td>
      <td><strong>0.8272</strong></td>
      <td>0.6148</td>
      <td>0.9119</td>
      <td>0.6673</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>★ Random Forest (150 trees)</strong></td>
      <td><strong>87.96%</strong></td>
      <td>0.5894</td>
      <td>0.7592</td>
      <td><strong>0.6636</strong></td>
      <td><strong>0.9258</strong></td>
      <td><strong>0.7096</strong></td>
    </tr>
    <tr>
      <td><strong>SVM (RBF Kernel)</strong></td>
      <td>86.89%</td>
      <td>0.5589</td>
      <td>0.7696</td>
      <td>0.6476</td>
      <td>0.9095</td>
      <td>0.6695</td>
    </tr>
  </tbody>
</table>

<div class="footer-clean">
  <strong>Key Insight:</strong> Random Forest wins across F1-Score (0.6636), ROC-AUC (0.9258), and PR-AUC (0.7096).
</div>

---

<!-- Slide 6: Visual Comparison & Metrics -->
## Multi-Metric Performance Overview

<div class="split">
  <div>
    <img src="../outputs/model_comparison_bar.png" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />
  </div>

  <div>
    <div class="step-row">
      <div class="step-badge" style="background: #10b981;">✓</div>
      <div class="step-content">
        <strong>Random Forest: The Balanced Leader</strong>
        <p>Strikes the ideal sweet spot: high recall (75.9%) without collapsing precision (58.9%).</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #ef4444;">✗</div>
      <div class="step-content">
        <strong>KNN: The Dimensionality Victim</strong>
        <p>Highest precision (69.0%) but catastrophic recall (38.5%). Misses over 61% of buyers because Euclidean distance breaks down in 68-dimension sparse space.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #3b82f6;">ℹ</div>
      <div class="step-content">
        <strong>Decision Tree: Maximum Sensitivity</strong>
        <p>Highest raw recall (82.7%) but lowest precision (48.9%). High false alarm rate.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 7: ROC and PR Discrimination Curves -->
## ROC & Precision-Recall Trajectories

<div class="split-even">
  <div>
    <img src="../outputs/roc_curves.png" style="width: 100%; border-radius: 8px;" />
    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 6px;">
      <strong>ROC Curves:</strong> Random Forest leads with AUC = 0.93, followed by Decision Tree and SVM.
    </div>
  </div>

  <div>
    <img src="../outputs/pr_curves.png" style="width: 100%; border-radius: 8px;" />
    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 6px;">
      <strong>PR Curves (Sensitive to Imbalance):</strong> Random Forest maintains superior precision across high recall thresholds (AP = 0.71).
    </div>
  </div>
</div>

---

<!-- Slide 8: Confusion Matrix Breakdown -->
## Operational Trade-Offs in Confusion Matrices

<div style="text-align: center;">
  <img src="../outputs/confusion_matrices.png" style="width: 95%; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);" />
</div>

<div class="split-even" style="margin-top: 18px; font-size: 14px;">
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 14px;">
    <strong style="color: #0f172a;">Decision Tree & Logistic:</strong> High False Positives (~250-310). Good when missing a customer is catastrophic, but sends too many unnecessary discounts.
  </div>
  <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 10px 14px;">
    <strong style="color: #166534;">Random Forest:</strong> Capped False Positives at 202 while capturing 290 out of 382 true buyers. Lowest overall commercial cost.
  </div>
</div>

---

<!-- Slide 9: Feature Importance & Explainability -->
## What Actually Drives the Purchase?

<div class="split">
  <div>
    <img src="../outputs/rf_feature_importance.png" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />
  </div>

  <div>
    <h3 style="color: #0f172a; margin-top: 0;">Top Predictors Decoded</h3>
    <div class="step-row">
      <div class="step-badge" style="background: #0d9488;">1</div>
      <div class="step-content">
        <strong>PageValues (Dominant >38%)</strong>
        <p>Users visiting pages with historical monetary association exhibit overwhelming conversion probability.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #0d9488;">2</div>
      <div class="step-content">
        <strong>ExitRates & BounceRates</strong>
        <p>Strong negative indicators. High bounce rates signal casual window shoppers.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #0d9488;">3</div>
      <div class="step-content">
        <strong>Month of November (Month_Nov)</strong>
        <p>Highest categorical rank. Direct reflection of Black Friday and holiday promotional rushes.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 10: Conclusion & Recommendations -->
## Conclusion & Business Recommendations

<div class="split-even">
  <div>
    <h3 style="color: #0f172a;">Key Takeaways</h3>
    <ul style="font-size: 15px; color: #475569; line-height: 1.7; padding-left: 20px;">
      <li><strong>Best Model:</strong> Random Forest is decisively superior for tabular e-commerce clickstreams (F1: 0.6636, ROC-AUC: 0.9258).</li>
      <li><strong>Tree Ensembles > Metric Models:</strong> Bagging trees effortlessly absorb non-linear combinations and one-hot sparsity that crippled KNN.</li>
      <li><strong>Class Balancing is Mandatory:</strong> Unweighted models fail to generate actionable business alerts.</li>
    </ul>
  </div>

  <div>
    <h3 style="color: #0369a1;">Next Steps & Extensions</h3>
    <div class="stat-hero">
      <div style="font-size: 15px; font-weight: 700; color: #0c4a6e;">Production Deployment:</div>
      <div style="font-size: 14px; color: #334155; margin-top: 4px;">
        Deploy Random Forest as a streaming inference microservice (sub-50ms latency) triggered when PageValues > 0.
      </div>
    </div>
    <div class="stat-hero" style="border-color: #8b5cf6;">
      <div style="font-size: 15px; font-weight: 700; color: #5b21b6;">Future Algorithms:</div>
      <div style="font-size: 14px; color: #334155; margin-top: 4px;">
        Benchmark XGBoost, LightGBM, and CatBoost with Bayesian Hyperparameter Tuning.
      </div>
    </div>
  </div>
</div>

<div style="margin-top: 36px; text-align: center; font-size: 16px; font-weight: 700; color: #0f172a;">
  Thank you! Q & A Session.
</div>
