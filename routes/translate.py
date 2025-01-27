"""
from fastapi import APIRouter
from repository.CardsRepository import CardsRepository
from gtts import gTTS 
from db.connection import Connection
import os

BASE_ROOT = os.path.dirname(os.path.abspath(__file__))


conn = Connection("db.db")
cards_repository = CardsRepository(conn)
router = APIRouter()

@router.get("/api/translate/{target}")
def translate():

            response = cards_repository.get_card_by_id(274)
            tts = gTTS(text=response.question, lang='en-us')
            audio_dir = os.path.join(BASE_ROOT, "static", "audios")
            os.makedirs(audio_dir, exist_ok=True)
            tts.save(os.path.join(audio_dir, f"audio{274}.mp3"))

"""