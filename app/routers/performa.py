from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Performa, Segmentasi, Anomali
from app.schemas.performa import PerformaInput, PerformaOutput
from app.schemas.segmentasi import SegmentasiInput, SegmentasiOutput
from app.schemas.anomali import AnomaliInput, AnomaliOutput
from app.model import predict_performa, segmentasi_gaya_belajar, deteksi_anomali

router = APIRouter()

# === PERFORMA ===
@router.post("/performa", response_model=PerformaOutput)
def create_performa(data: PerformaInput, db: Session = Depends(get_db)):
    try:
        print("✅ Data masuk:", data)
        hasil = predict_performa([
            data.nilai_mtk,
            data.nilai_ipa,
            data.jam_belajar,
            data.klik_video
        ])
        print("✅ Hasil prediksi:", hasil)

        prediksi = Performa(**data.dict(), hasil_prediksi=hasil)
        db.add(prediksi)
        db.commit()
        db.refresh(prediksi)
        print("✅ Data berhasil disimpan:", prediksi)
        return prediksi

    except Exception as e:
        print("❌ ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/performa", response_model=list[PerformaOutput])
def get_all_performa(db: Session = Depends(get_db)):
    return db.query(Performa).all()

@router.put("/performa/{id}", response_model=PerformaOutput)
def update_performa(id: int, data: PerformaInput, db: Session = Depends(get_db)):
    prediksi = db.query(Performa).filter(Performa.id == id).first()
    if not prediksi:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    hasil = predict_performa([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])
    for field, value in data.dict().items():
        setattr(prediksi, field, value)
    prediksi.hasil_performa = hasil
    db.commit()
    db.refresh(prediksi)
    return prediksi

@router.delete("/performa/{id}")
def delete_performa(id: int, db: Session = Depends(get_db)):
    prediksi = db.query(Performa).filter(Performa.id == id).first()
    if not prediksi:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    db.delete(prediksi)
    db.commit()
    return {"message": "Data berhasil dihapus"}
