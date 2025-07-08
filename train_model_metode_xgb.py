import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import joblib

# 1. Data dummy metode belajar
data = {
    "nilai_mtk": [80, 70, 60, 90, 75, 85, 95, 50, 78, 88, 69, 92, 55, 83, 77],
    "nilai_ipa": [85, 60, 70, 90, 80, 88, 98, 55, 82, 86, 74, 91, 60, 84, 76],
    "jam_belajar": [2, 1, 1.5, 3, 2.5, 3.5, 4, 1, 2, 2.5, 1, 3.2, 1.7, 2.8, 2.3],
    "klik_video": [4, 2, 3, 5, 6, 7, 10, 1, 5, 6, 3, 7, 2, 6, 4],
    "metode": [
        "Visual", "Auditory", "Kinesthetic", "Visual", "Kinesthetic",
        "Visual", "Auditory", "Kinesthetic", "Visual", "Auditory",
        "Visual", "Visual", "Auditory", "Kinesthetic", "Auditory"
    ]
}

df = pd.DataFrame(data)

# 2. Fitur dan label
X = df[["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"]]
y = df["metode"]

# 3. Encode label
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, stratify=y_encoded, random_state=42)

# 5. Train model XGBoost
model = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
model.fit(X_train, y_train)

# 6. Simpan model dan label encoder
joblib.dump(model, "app/model_metode.pkl")
joblib.dump(label_encoder, "app/label_encoder_metode.pkl")
print("✅ Model & encoder berhasil disimpan ke 'app/'")
