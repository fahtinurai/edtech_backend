from pydantic import BaseModel
from datetime import datetime

class SegmentasiInput(BaseModel):
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: float  # atau int jika kamu ingin validasi ketat

class SegmentasiOutput(SegmentasiInput):
    id: int
    hasil_segmentasi: str  # sesuaikan dengan field di model SQLAlchemy
    timestamp: datetime

    class Config:
        orm_mode = True
