from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas import adaptasi as schemas
from app.model import adaptasi_jalur_belajar

router = APIRouter()

@router.post("/adaptasi", response_model=schemas.Adaptasi)
def create_adaptasi(data: schemas.AdaptasiCreate, db: Session = Depends(get_db)):
    hasil = adaptasi_jalur_belajar([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])
    db_data = models.Adaptasi(**data.dict(), hasil_jalur=hasil)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.get("/", response_model=list[schemas.Adaptasi])
def read_all_adaptasi(db: Session = Depends(get_db)):
    return db.query(models.Adaptasi).all()

@router.get("/{adaptasi_id}", response_model=schemas.Adaptasi)
def read_adaptasi(adaptasi_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Adaptasi).filter(models.Adaptasi.id == adaptasi_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    return result

@router.delete("/{adaptasi_id}")
def delete_adaptasi(adaptasi_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Adaptasi).filter(models.Adaptasi.id == adaptasi_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    db.delete(result)
    db.commit()
    return {"message": "Data berhasil dihapus"}
