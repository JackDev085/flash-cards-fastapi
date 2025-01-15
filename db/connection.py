from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import shutil
import tempfile

BASE_ROOT = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
# Ensure the source database file exists before copying
source_db = os.path.join(BASE_ROOT, "teste.db")  # Ensure this file exists in the 'db' directory

# Use a temporary directory suitable for Windows
destination_db = os.path.join(tempfile.gettempdir(), "temp.db")

# Ensure the destination directory exists
os.makedirs(os.path.dirname(destination_db), exist_ok=True)

if not os.path.exists(source_db):
    raise FileNotFoundError(f"Source database file '{source_db}' does not exist.")

# Copy the existing database file to a new location
db_temporary = shutil.copyfile(source_db, destination_db)

DATABASE_URL = f"sqlite:///{db_temporary}"
Base = declarative_base()
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()