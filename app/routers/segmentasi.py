from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Performa, Segmentasi, Anomali
from app.schemas.performa import PerformaInput, PerformaOutput
from app.schemas.segmentasi import SegmentasiInput, SegmentasiOutput
from app.schemas.anomali import AnomaliInput, AnomaliOutput
from app.model import predict_performa, segmentasi_gaya_belajar, deteksi_anomali

router = APIRouter()

@router.post("/segmentasi", response_model=SegmentasiOutput)
def create_segmentasi(data: SegmentasiInput, db: Session = Depends(get_db)):
    print("📩 Data diterima:", data)

    hasil = segmentasi_gaya_belajar([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])
    print("✅ Hasil segmentasi:", hasil)

    seg = Segmentasi(
        nilai_mtk=data.nilai_mtk,
        nilai_ipa=data.nilai_ipa,
        jam_belajar=data.jam_belajar,
        klik_video=int(data.klik_video),
        hasil_segmentasi=hasil
    )
    db.add(seg)
    db.commit()
    db.refresh(seg)
    return seg


@router.get("/segmentasi", response_model=list[SegmentasiOutput])
def get_all_segmentasi(db: Session = Depends(get_db)):
    return db.query(Segmentasi).all()

@router.put("/segmentasi/{id}", response_model=SegmentasiOutput)
def update_segmentasi(id: int, data: SegmentasiInput, db: Session = Depends(get_db)):
    seg = db.query(Segmentasi).filter(Segmentasi.id == id).first()
    if not seg:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    hasil = segmentasi_gaya_belajar([
        data.nilai_mtk,
        data.nilai_ipa,
        data.jam_belajar,
        data.klik_video
    ])
    for field, value in data.dict().items():
        setattr(seg, field, value)
    seg.hasil_segmentasi = hasil
    db.commit()
    db.refresh(seg)
    return seg

@router.delete("/segmentasi/{id}")
def delete_segmentasi(id: int, db: Session = Depends(get_db)):
    seg = db.query(Segmentasi).filter(Segmentasi.id == id).first()
    if not seg:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    db.delete(seg)
    db.commit()
    return {"message": "Data berhasil dihapus"}