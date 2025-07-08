# schemas/adaptasi.py

from pydantic import BaseModel
from datetime import datetime

# ⛔ base class hanya untuk field input
class AdaptasiCreate(BaseModel):
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: float

# ✅ response model / model untuk output
class Adaptasi(BaseModel):
    id: int
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: float
    hasil_jalur: str
    timestamp: datetime

    class Config:
        orm_mode = True
