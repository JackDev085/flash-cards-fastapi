from models.cards import Cards
from db.connection import Connection
class CardsRepository:
    def __init__(self, db:Connection):
        self.db = db

   
    def get_random_card(self,theme):
        """Get a random card from the database according to a theme"""
        return self.db.execute_query("SELECT * FROM cards WHERE theme = (?) ORDER BY RANDOM() LIMIT 1", (theme,))
    
    def get_categories(self):
        """Get all categories from the database"""
        return self.db.execute_query("SELECT * FROM categories")
    
    def get_themes_by_categories(self, category):
        """Get all themes from the database"""
        return self.db.execute_query("SELECT * FROM themes where category_id = (?)", (category,))
    