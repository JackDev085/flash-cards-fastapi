import sqlite3
from random import randint

conn = sqlite3.connect('teste.db', autocommit=True)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()




def search_card():
    aleatorio = randint(1, 100)
    sql = """
    select id,question,answer from cards
    where id = (?)
    """
    cursor.execute(sql,(aleatorio,))
    return cursor.fetchone()

def search_response(id):
    sql = """
    select answer from cards
    where id = (?)
    """
    cursor.execute(sql,(id,))
    return cursor.fetchone()




