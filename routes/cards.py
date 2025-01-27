from fastapi import APIRouter
from repository.CardsRepository import CardsRepository
from db.connection import Connection
from fastapi import HTTPException
from models.models import Card

db = Connection("db.db")
router = APIRouter(tags=["Flashcards"])


@router.get("/api/aleatory_card/",response_model=Card)
async def aleatory_card_by_theme(theme:int):
    """Busca um cartão aleatório no banco de dados de acordo com o tema especificado"""
    cards_repository = CardsRepository(db)
    card = cards_repository.get_random_card(theme)
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

@router.get("/flashcards/categories/",response_model=list)
async def flash_cards_categories():
    """Busca todas as categorias no banco de dados"""
    cards_repository = CardsRepository(db)
    categories = cards_repository.get_categories()
    if not categories:
        raise HTTPException(status_code=404, detail="Categories not found")
    return categories

@router.get("/flashcards/category/{category_id}",response_model=list)
async def flash_cards_themes_by_category(category_id:int):
    """Busca todos os temas de uma categoria no banco de dados"""
    cards_repository = CardsRepository(db)
    cards = cards_repository.get_themes_by_categories(category_id)
    if not cards:
        raise HTTPException(status_code=404, detail="Themes not found")
    return cards

@router.get("/flashcards/themes/",response_model=list)
async def flash_cards_themes():
    """Busca todos os temas de uma categoria no banco de dados"""
    cards_repository = CardsRepository(db)
    cards = cards_repository.get_themes()
    if not cards:
        raise HTTPException(status_code=404, detail="Themes not found")
    return cards
    
'''
@router.get("/api/aleatory_card/")
async def aleatory_card(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user is None:
        return {"error": "Not authorized"}
    
    cards_repository = CardsRepository(db)
    aleatory_card = cards_repository.get_random_card()
    return aleatory_card

@router.get("/api/search_response/{id}")
async def search_response_by_id(id:int,current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user is None:
        return {"error": "Not authorized"}
    
    cards_repository = CardsRepository(db)
    response = cards_repository.response_of_card_by_id(id)
    return response

@router.get("/flashcards/{theme}")
async def render_flashcards_page(theme:str,current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user is None:
        return {"error": "Not authorized"}

    
    cards_repository = CardsRepository(Depends(db))
    #cards = cards_repository.get_cards_by_theme(theme)
'''  