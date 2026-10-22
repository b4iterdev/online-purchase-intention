import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

os.makedirs('data', exist_ok=True)
print("Fetching Online Shoppers Purchasing Intention dataset (ID: 468)...")
online_shoppers = fetch_ucirepo(id=468)

X = online_shoppers.data.features
y = online_shoppers.data.targets

df = pd.concat([X, y], axis=1)
csv_path = 'data/online_shoppers_intention.csv'
df.to_csv(csv_path, index=False)
print(f"Saved dataset to {csv_path}")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Target distribution:\n", df['Revenue'].value_counts(normalize=True))
