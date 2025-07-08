# app/schemas/performa.py
from pydantic import BaseModel
from datetime import datetime

class PerformaInput(BaseModel):
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: float

class PerformaOutput(BaseModel):
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: int
    hasil_prediksi: float  
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
