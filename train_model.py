# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# 1. Data dummy
data = {
    "nilai_mtk": [80, 70, 60, 90, 75, 85, 95, 50, 78, 88, 69, 92, 55, 83, 77],
    "nilai_ipa": [85, 60, 70, 90, 80, 88, 98, 55, 82, 86, 74, 91, 60, 84, 76],
    "jam_belajar": [2, 1, 1.5, 3, 2.5, 3.5, 4, 1, 2, 2.5, 1, 3.2, 1.7, 2.8, 2.3],
    "klik_video": [4, 2, 3, 5, 6, 7, 10, 1, 5, 6, 3, 7, 2, 6, 4],
    "rekomendasi": [
        "Video Pembelajaran", "Artikel", "Artikel", "Video Pembelajaran", "Kuis",
        "Video Pembelajaran", "Kuis", "Artikel", "Kuis", "Artikel", "Artikel",
        "Video Pembelajaran", "Kuis", "Video Pembelajaran", "Kuis"
    ]
}


df = pd.DataFrame(data)

# 2. Fitur dan Label
X = df[["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"]]
y = df["rekomendasi"]

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# 4. Latih model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Simpan model ke file
joblib.dump(model, "app/model_rekomendasi.pkl")
print("Model disimpan ke app/model_rekomendasi.pkl")
