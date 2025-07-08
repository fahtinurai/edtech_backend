import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base
import pandas as pd

# --- Load model untuk rekomendasi materi
model_materi = joblib.load("app/model_rekomendasi.pkl")

# --- Load model untuk rekomendasi metode belajar
model_metode = joblib.load("app/model_metode.pkl")
label_encoder_metode = joblib.load("app/label_encoder_metode.pkl")

# --- Load model untuk rekomendasi performa
model_performa = joblib.load("app/model_performa.pkl")

# Load model segmentasi
model_segmentasi = joblib.load("app/model_segmentasi.pkl")

# --- Load model deteksi anomali
model_anomali = joblib.load("app/model_anomali.pkl")

# --- Fungsi prediksi materi
def predict_materi(data):
    arr = np.array(data).reshape(1, -1)
    hasil = model_materi.predict(arr)[0]
    return hasil

# --- Fungsi prediksi metode belajar
def predict_metode(data):
    arr = np.array(data).reshape(1, -1)
    pred_num = model_metode.predict(arr)[0]
    pred_label = label_encoder_metode.inverse_transform([pred_num])[0]
    return pred_label

# --- Fungsi prediksi performa
def predict_performa(data):
    print("📦 Data untuk model_performa:", data)
    arr = np.array(data).reshape(1, -1)
    hasil = model_performa.predict(arr)[0]
    print("✅ Model_performa result:", hasil)
    return hasil


# Fungsi segmentasi gaya belajar
def segmentasi_gaya_belajar(data):
    arr = np.array(data).reshape(1, -1)
    cluster = model_segmentasi.predict(arr)[0]
    
    if cluster == 0:
        return "Visual"
    elif cluster == 1:
        return "Auditory"
    else:
        return "Kinesthetic"

# Fungsi deteksi anomali
# Menggunakan model Isolation Forest untuk mendeteksi anomali
def deteksi_anomali(input_data):
    df = pd.DataFrame([input_data], columns=["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"])
    pred = model_anomali.predict(df)
    return "❗Anomali Terdeteksi" if pred[0] == -1 else "✅ Tidak Ada Anomali"


# Load model DQL
class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
    
# Load model dari file
model_dql = DQN(input_dim=4, output_dim=2)
model_dql.load_state_dict(torch.load("app/model_dql.pth"))
model_dql.eval()

# Fungsi untuk prediksi jalur belajar
def adaptasi_jalur_belajar(data):
    x = torch.tensor(data, dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        q_values = model_dql(x)
        action = torch.argmax(q_values, dim=1).item()
    
    if action == 0:
        return "Fokus ke Materi Dasar"
    elif action == 1:
        return "Tingkatkan Latihan Soal"
    else:
        return "Ikuti Pembelajaran Mandiri"

