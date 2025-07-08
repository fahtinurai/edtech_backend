# train_model_anomali.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# 1. Load dataset
df = pd.read_csv("data/edtech_combined_dataset.csv")

# 2. Fitur yang digunakan
X = df[["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"]]

# 3. Latih model Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# 4. Simpan model
joblib.dump(model, "app/model_anomali.pkl")
print("✅ Model anomali disimpan ke app/model_anomali.pkl")
