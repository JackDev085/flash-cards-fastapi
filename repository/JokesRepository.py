from db.connection import Connection
from random import randint

class CardsRepository:
    def __init__(self, cursor: Connection):
        self._cursor = cursor

    def get_random_card(self):
        self._cursor.execute_query("SELECT * FROM cards ORDER BY RANDOM() LIMIT 1")
        return self._cursor.fetch_one()
    
    def response_of_card_by_id(self, id):
        self._cursor.execute_query("SELECT answer FROM cards WHERE id = ?", (id,))
        return self._cursor.fetch_one()
    