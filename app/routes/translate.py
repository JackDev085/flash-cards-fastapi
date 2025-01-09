"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from repository.CardsRepository import CardsRepository
from gtts import gTTS 
from db.connection import Connection

conn = Connection("teste.db")
cards_repository = CardsRepository(conn)
router = APIRouter()

@router.get("/api/translate/{target}")
def translate():
        response = cards_repository.get_card_by_id(100)
        tts = gTTS(text=response["question"], lang='en-us')
        tts.save(f"audios/audio100.mp3")
        return {"message": "Audios created successfully"}"""
