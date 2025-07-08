from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.materi import MateriInput, MateriOutput
from app.database import get_db
from app.models import Materi

router = APIRouter(
    prefix="/rekomendasi-materi",
    tags=["Materi"]
)

@router.get("/", response_model=list[MateriOutput])
def get_all_materi(db: Session = Depends(get_db)):
    return db.query(Materi).all()

@router.post("/", response_model=MateriOutput)
def create_materi(input_data: MateriInput, db: Session = Depends(get_db)):
    materi = Materi(**input_data.dict())
    db.add(materi)
    db.commit()
    db.refresh(materi)
    return materi

@router.put("/{materi_id}", response_model=MateriOutput)
def update_materi(materi_id: int, input_data: MateriInput, db: Session = Depends(get_db)):
    materi = db.query(Materi).filter(Materi.id == materi_id).first()
    if not materi:
        raise HTTPException(status_code=404, detail="Materi not found")
    for key, value in input_data.dict().items():
        setattr(materi, key, value)
    db.commit()
    db.refresh(materi)
    return materi

@router.delete("/{materi_id}")
def delete_materi(materi_id: int, db: Session = Depends(get_db)):
    materi = db.query(Materi).filter(Materi.id == materi_id).first()
    if not materi:
        raise HTTPException(status_code=404, detail="Materi not found")
    db.delete(materi)
    db.commit()
    return {"message": "Materi deleted"}

@router.post("/rekomendasi")
def rekomendasi_materi(input_data: MateriInput, db: Session = Depends(get_db)):
    if input_data.jam_belajar > 2 and input_data.klik_video > 3:
        hasil = "Visual"
    elif input_data.nilai_ipa > input_data.nilai_mtk:
        hasil = "Kinesthetic"
    else:
        hasil = "Auditory"

    materi = Materi(**input_data.dict(), hasil=hasil)
    db.add(materi)
    db.commit()

    return {"rekomendasi_materi": hasil}  # ⬅ kembalikan hanya hasil

