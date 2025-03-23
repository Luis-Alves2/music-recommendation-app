from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Database URL (update with your PostgreSQL credentials)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/music_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database models here (example: User)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    spotify_id = Column(String, unique=True)
    # Add more fields as needed

# Create tables (run this once)
def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()