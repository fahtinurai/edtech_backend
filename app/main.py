from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.adaptasi import router as adaptasi_router
from app.routers.materi import router as materi_router
from app.routers.metode import router as metode_router
from app.routers.performa import router as performa_router
from app.routers.segmentasi import router as segmentasi_router
from app.routers.anomali import router as anomali_router
from app.init_db import init_db

app = FastAPI()

# ✅ CORS dulu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Daftarkan router
app.include_router(materi_router, tags=["Materi"])
app.include_router(metode_router, tags=["Metode"])
app.include_router(performa_router, prefix="/prediksi-performa", tags=["Performa"])
app.include_router(segmentasi_router, prefix = "/segmentasi", tags=["Segmentasi"])
app.include_router(anomali_router, tags=["anomali"])
app.include_router(adaptasi_router, prefix="/adaptasi-jalur", tags=["adaptasi"])

# ✅ Terakhir baru inisialisasi DB
init_db()
