from models.models import Card,Category,Theme
from db.connection import Connection
class CardsRepository:
    def __init__(self, db:Connection):
        self.db = db

    def get_card_by_id(self, id:int)->Card:
        """Busca um cartão no banco de dados de acordo com o id especificado""" 
        card = self.db.execute_query("SELECT * FROM cards WHERE id = (?)",(id,)).fetchone()
        if not card:
            return None
        return Card(**card)
    
    def get_random_card(self,theme:id)->Card:
        """Busca um cartão aleatório no banco de dados de acordo com o tema especificado""" 

        card = self.db.execute_query("SELECT * FROM cards WHERE theme_id = (?) ORDER BY RANDOM() LIMIT 1",(theme,)).fetchone()
        if not card:
            return None
        return Card(**card)
        

    def get_categories(self)->list:
        """Busca todas as categorias no banco de dados"""
        categories = self.db.execute_query("SELECT * FROM category").fetchall()
        categories = [Category(**category) for category in categories]
        return categories
        
    def get_themes(self)->list:
        """Busca todos os temas de uma categoria específica"""
        themes = self.db.execute_query("SELECT * FROM themes").fetchall()
        if not themes:
            return None
        return [Theme(**theme) for theme in themes]
    
    def get_themes_by_categories(self, category:int)->list:
        """Busca todos os temas de uma categoria específica"""
        themes = self.db.execute_query("SELECT * FROM themes where category_id = (?)", (category,)).fetchall()
        if not themes:
            return None
        return [Theme(**theme) for theme in themes]

    