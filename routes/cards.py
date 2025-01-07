from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from repository.CardsRepository import CardsRepository
from db.connection import Connection

conn = Connection("teste.db")
cards_repository = CardsRepository(conn)
router = APIRouter()

@router.get("/api/aleatory_card/")
async def aleatory_card():
    aleatory_card = cards_repository.get_random_card()
    return aleatory_card

@router.get("/api/search_response/{id}")
async def search_response_by_id(id:int):   
    response = cards_repository.response_of_card_by_id(id)
    return response