# app/models.py
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base

class LogPrediksi(Base):
    __tablename__ = "log_prediksi"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    nilai_mtk = Column(Float)
    nilai_ipa = Column(Float)
    jam_belajar = Column(Float)
    klik_video = Column(Integer)
    hasil_prediksi = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Adaptasi(Base):
    __tablename__ = "adaptasi"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    nilai_mtk = Column(Float)
    nilai_ipa = Column(Float)
    jam_belajar = Column(Float)
    klik_video = Column(Integer)  # atau Float jika kamu ingin
    hasil_jalur = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)

class Materi(Base):
    __tablename__ = "materi"

    id = Column(Integer, primary_key=True, index=True)
    nilai_mtk = Column(Float)
    nilai_ipa = Column(Float)
    jam_belajar = Column(Float)
    klik_video = Column(Integer)
    hasil = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)

# Tambahkan ini di bawah model-model lain di models.py
class Metode(Base):
    __tablename__ = "metode"

    id = Column(Integer, primary_key=True, index=True)
    nilai_mtk = Column(Float)
    nilai_ipa = Column(Float)
    jam_belajar = Column(Float)
    klik_video = Column(Integer)
    hasil_metode = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)


class Performa(Base):
    __tablename__ = "performa"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    nilai_mtk = Column(Float)
    nilai_ipa = Column(Float)
    jam_belajar = Column(Float)
    klik_video = Column(Integer)
    hasil_prediksi = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Segmentasi(Base):
    __tablename__ = "segmentasi"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    nilai_mtk = Column(Float)
    nilai_ipa = Column(Float)
    jam_belajar = Column(Float)
    klik_video = Column(Integer)
    hasil_segmentasi = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)


# app/models.py
class Anomali(Base):
    __tablename__ = "anomali"
    id = Column(Integer, primary_key=True, index=True)
    nilai_mtk = Column(Float)
    nilai_ipa = Column(Float)
    jam_belajar = Column(Float)
    klik_video = Column(Integer)
    hasil_anomali = Column(String(100))  # WAJIB ADA
    status_anomali = Column(String(100))  # WAJIB ADA
    timestamp = Column(DateTime, default=datetime.utcnow)
