import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Data dummy: output performa dalam bentuk angka (misalnya skor 0–100)
data = {
    "nilai_mtk": [80, 70, 60, 90, 75, 85, 95, 50, 78, 88, 69, 92, 55, 83, 77],
    "nilai_ipa": [85, 60, 70, 90, 80, 88, 98, 55, 82, 86, 74, 91, 60, 84, 76],
    "jam_belajar": [2, 1, 1.5, 3, 2.5, 3.5, 4, 1, 2, 2.5, 1, 3.2, 1.7, 2.8, 2.3],
    "klik_video": [4, 2, 3, 5, 6, 7, 10, 1, 5, 6, 3, 7, 2, 6, 4],
    "performa": [80, 65, 60, 85, 70, 90, 95, 50, 72, 88, 66, 96, 55, 89, 75]  # Skor performa numerik
}

df = pd.DataFrame(data)

# Fitur dan target
X = df[["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"]]
y = df["performa"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Model regresi
model = LinearRegression()
model.fit(X_train, y_train)

# Simpan model
joblib.dump(model, "app/model_performa_regresi.pkl")
print("✅ Model regresi performa disimpan ke app/model_performa_regresi.pkl")
