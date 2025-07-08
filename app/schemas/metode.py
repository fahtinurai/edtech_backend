from pydantic import BaseModel
from datetime import datetime

class MetodeInput(BaseModel):
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: int

class MetodeOutput(MetodeInput):
    id: int
    hasil_metode: str
    timestamp: datetime

    class Config:
        orm_mode = True
