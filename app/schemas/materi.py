# app/schemas/materi.py

from pydantic import BaseModel
from datetime import datetime

class MateriInput(BaseModel):
    nilai_mtk: float
    nilai_ipa: float
    jam_belajar: float
    klik_video: int

class MateriOutput(MateriInput):
    id: int
    hasil: str
    timestamp: datetime

    class Config:
        from_attributes = True  # untuk SQLAlchemy ORM
