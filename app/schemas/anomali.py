# app/schemas/anomali.py
from pydantic import BaseModel
from datetime import datetime


class AnomaliInput(BaseModel):
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: float

# app/schemas/anomali.py
class AnomaliOutput(AnomaliInput):
    id: int
    hasil_anomali: str  # HARUS pakai nama field ini
    status_anomali: str
    timestamp: datetime

    class Config:
        from_attributes = True


