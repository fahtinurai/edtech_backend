import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Data dummy (dengan output performa berupa angka, misal skala 0–100)
data = {
    "nilai_mtk": [80, 70, 60, 90, 75, 85, 95, 50, 78, 88, 69, 92, 55, 83, 77],
    "nilai_ipa": [85, 60, 70, 90, 80, 88, 98, 55, 82, 86, 74, 91, 60, 84, 76],
    "jam_belajar": [2, 1, 1.5, 3, 2.5, 3.5, 4, 1, 2, 2.5, 1, 3.2, 1.7, 2.8, 2.3],
    "klik_video": [4, 2, 3, 5, 6, 7, 10, 1, 5, 6, 3, 7, 2, 6, 4],
    "performa": [75, 60, 63, 85, 70, 82, 95, 45, 72, 83, 67, 96, 50, 84, 71]  # skala 0–100
}

df = pd.DataFrame(data)

X = df[["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"]]
y = df["performa"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "app/model_performa.pkl")
print("✅ Model performa disimpan ke app/model_performa.pkl")
