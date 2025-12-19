from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MovieDB(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genre = Column(String)

Base.metadata.create_all(bind=engine)

class MovieCreate(BaseModel):
    title: str
    genre: str

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/movies")
def list_movies(db: Session = Depends(get_db)):
    logger.info("Filmlista lekérése az adatbázisból")
    return db.query(MovieDB).all()

@app.post("/movies")
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    logger.info(f"Új film hozzáadása: {movie.title}")
    new_movie = MovieDB(title=movie.title, genre=movie.genre)
    db.add(new_movie)
    db.commit()
    return new_movie

@app.get("/scrape")
def scrape_example():
    res = requests.get("https://hvg.hu")
    soup = BeautifulSoup(res.text, 'html.parser')
    headers = [h.get_text().strip() for h in soup.find_all('h1')[:3]]
    return {"status": "Automation active", "latest_titles": headers}