from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import predict_metode
from app.models import Metode
from app.schemas.metode import MetodeInput, MetodeOutput

router = APIRouter()

@router.post("/rekomendasi-metode", response_model=MetodeOutput)
def create_metode(data: MetodeInput, db: Session = Depends(get_db)):
    print("📩 Input data:", data)
    hasil = predict_metode([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])
    print("✅ Rekomendasi metode:", hasil)

    metode = Metode(**data.dict(), hasil_metode=hasil)
    db.add(metode)
    db.commit()
    db.refresh(metode)
    return metode

@router.get("/rekomendasi-metode", response_model=list[MetodeOutput])
def get_all_metode(db: Session = Depends(get_db)):
    return db.query(Metode).all()

@router.put("/{id}", response_model=MetodeOutput)
def update_metode(id: int, data: MetodeInput, db: Session = Depends(get_db)):
    record = db.query(Metode).filter(Metode.id == id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Metode tidak ditemukan")
    
    hasil = predict_metode([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])
    for field, value in data.dict().items():
        setattr(record, field, value)
    record.hasil_metode = hasil
    db.commit()
    db.refresh(record)
    return record

@router.delete("/{id}")
def delete_metode(id: int, db: Session = Depends(get_db)):
    record = db.query(Metode).filter(Metode.id == id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Metode tidak ditemukan")
    db.delete(record)
    db.commit()
    return {"detail": "Metode berhasil dihapus"}
