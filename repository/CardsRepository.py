from sqlalchemy.orm import Session
from random import randint
from models.cards import Cards
#from models.themes import Themes

class CardsRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_random_card(self):
        return self.db.query(Cards).filter(Cards.id == randint(1, 100)).first()
           
    def get_card_by_id(self, id:int):
        return self.db.query(Cards).filter(Cards.id == id).first()
    
    def response_of_card_by_id(self, id):
        card = self.db.query(Cards).filter(Cards.id == id).first()
        return {"answer": card.answer} if card else None
    
    def get_card_by_teme(self, theme):
        sql = "SELECT * FROM cards WHERE theme = (?)"
        return self.db.query(Cards).filter(Cards.theme == theme)
        
    