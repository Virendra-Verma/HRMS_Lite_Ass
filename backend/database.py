import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Database credentials from .env
DB_NAME = os.getenv("DB_NAME", "hrms_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
NODE_ENV = os.getenv("NODE_ENV", "development")

# 3. Connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 4. Production settings (SSL for Render/Railway)
connect_args = {}
if NODE_ENV == "production":
    connect_args = {"sslmode": "require"}

# 5. Engine setup
# echo=True development mein saari SQL queries terminal par dikhayega
engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_args, 
    echo=(NODE_ENV == "development")
)

# 6. Session and Base setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 7. DB Dependency (Circular import se bachne ke liye import nahi, yahin define karein)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()