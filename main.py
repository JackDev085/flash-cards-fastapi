from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from fastapi.responses import HTMLResponse
from repository.CardsRepository import CardsRepository
from db.connection import Connection
from views.html import html_index, html_cards
from fastapi.staticfiles import StaticFiles
import dotenv
from gtts import gTTS

dotenv.load_dotenv()
ROOT_DIR = Path(__file__).resolve().parent

conn = Connection("teste.db")
cads_repository = CardsRepository(conn)

app = FastAPI(
    title="FastAPI flash cards API",
    description="API for flash cards",
    version="0.1.0",
)

#cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir qualquer origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#static files
app.mount("/static", StaticFiles(directory="views/static"), name="static")

@app.get("/")
async def html():
    return HTMLResponse(content=html_index, status_code=200)

@app.get("/flashcards/")
async def render_flashcards_page():
    # Adicione o tema no conteúdo HTML, se necessário
    return HTMLResponse(content=html_cards, status_code=200)

    
@app.get("/api/aleatory_card/")
async def aleatory_card():
    aleatory_card = cads_repository.get_random_card()
    return aleatory_card

@app.get("/api/search_response/{id}")
async def search_response_by_id(id:int):   
    response = cads_repository.response_of_card_by_id(id)
    return response

@app.get("/api/translate/")
def translate():
        response = cads_repository.get_card_by_id(100)
        tts = gTTS(text=response["question"], lang='en-us')
        tts.save(f"audios/audio100.mp3")
        return {"message": "Audios created successfully"}
        


"""if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)"""