from app.db.connection import Connection
from random import randint

class CardsRepository:
    def __init__(self, cursor: Connection):
        self._cursor = cursor

    def get_random_card(self):
        sql = "SELECT * FROM cards ORDER BY RANDOM() LIMIT 1"
        self._cursor.execute_query(sql, ())
        return self._cursor.fetch_one()
    
    def get_card_by_id(self, id:int):
        sql = "SELECT question FROM cards WHERE id = (?)"
        self._cursor.execute_query(sql, (id,))
        return self._cursor.fetch_one()
    
    def response_of_card_by_id(self, id):
        sql = "SELECT answer FROM cards WHERE id = (?)"
        self._cursor.execute_query(sql, (id,))
        return self._cursor.fetch_one()
    