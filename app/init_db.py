from app.database import engine
from app import models

def init_db():
    try:
        print("🛠️ Inisialisasi database...")
        print("📌 Sebelum create_all")
        models.Base.metadata.create_all(bind=engine)
        print("✅ Setelah create_all")
        print("✅ Database berhasil diinisialisasi.")
    except Exception as e:
        print("❌ Gagal inisialisasi database:", e)
