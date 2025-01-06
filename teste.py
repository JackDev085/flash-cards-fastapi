from gtts import gTTS
import os
from repository import CardsRepository
import sqlite3
from db.connection import Connection




# Conectar ao banco de dados
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

for i in range(100):
    sql = "SELECT question FROM cards where id=(?)"
    cursor.execute(sql, (i,)).fetchone()
        
    break

"""tts = gTTS(text=texto, lang='en-us')
tts.save("exemplo.mp3")

# Reproduzir o áudio (opcional)
os.system("start exemplo.mp3")  # Use 'xdg-open' no Linux e 'open' no macOS
"""
