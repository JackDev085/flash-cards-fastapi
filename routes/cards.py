from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from repository.CardsRepository import CardsRepository
from db.connection import Connection
from fastapi import Depends
from core.security import get_current_user
from models.user import User

conn = Connection("teste.db")
cards_repository = CardsRepository(conn)
router = APIRouter()

@router.get("/api/aleatory_card/")
async def aleatory_card(current_user: User = Depends(get_current_user)):
    if current_user is None:
        return {"error": "Not authorized"}
    aleatory_card = cards_repository.get_random_card()
    return aleatory_card

@router.get("/api/search_response/{id}")
async def search_response_by_id(id:int,current_user: User = Depends(get_current_user)):
    if current_user is None:
        return {"error": "Not authorized"}
    response = cards_repository.response_of_card_by_id(id)
    return response

@router.get("/flashcards/{theme}")
async def render_flashcards_page(theme:str,current_user: User = Depends(get_current_user)):
    if current_user is None:
        return {"error": "Not authorized"}
    cards = cards_repository.get_cards_by_theme(theme)