# train_model_segmentasi.py

import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

# 1. Load data CSV
data_path = os.path.join("data", "edtech_combined_dataset.csv")
df = pd.read_csv(data_path)

# 2. Ambil fitur yang digunakan
X = df[["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"]]

# 3. Latih model KMeans (3 cluster)
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# 4. Simpan model
joblib.dump(model, "app/model_segmentasi.pkl")
print("✅ Model segmentasi disimpan ke app/model_segmentasi.pkl")
