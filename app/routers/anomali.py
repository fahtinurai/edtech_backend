from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Anomali
from app.schemas.anomali import AnomaliInput, AnomaliOutput
from app.model import deteksi_anomali  # fungsi prediksi dari model ML

router = APIRouter(
    prefix="/AnomalyNotification",
    tags=["anomali"]
)

# Endpoint untuk deteksi anomali
@router.post("/anomali", response_model=AnomaliOutput)
def create_anomali(data: AnomaliInput, db: Session = Depends(get_db)):
    hasil = deteksi_anomali([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])

    det = Anomali(
        **data.dict(),
        hasil_anomali=hasil,
        status_anomali="Terdeteksi" if "Anomali" in hasil else "Normal"
    )
    db.add(det)
    db.commit()
    db.refresh(det)
    return det



@router.get("/anomali", response_model=list[AnomaliOutput])
def get_all_anomali(db: Session = Depends(get_db)):
    return db.query(Anomali).all()

@router.put("/anomali/{id}", response_model=AnomaliOutput)
def update_anomali(id: int, data: AnomaliInput, db: Session = Depends(get_db)):
    det = db.query(Anomali).filter(Anomali.id == id).first()
    if not det:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    
    hasil = deteksi_anomali([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])
    status = "Anomali" if "Anomali" in hasil else "Normal"

    for field, value in data.dict().items():
        setattr(det, field, value)

    det.hasil_anomali = hasil
    det.status_anomali = status

    db.commit()
    db.refresh(det)
    return det

@router.delete("/anomali/{id}")
def delete_anomali(id: int, db: Session = Depends(get_db)):
    det = db.query(Anomali).filter(Anomali.id == id).first()
    if not det:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    db.delete(det)
    db.commit()
    return {"message": "Data berhasil dihapus"}
