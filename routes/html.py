from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from repository.CardsRepository import CardsRepository
from pathlib import Path
from db.connection import Connection
from fastapi import  Response

BASE_ROOT = Path(__file__).resolve().parent.parent
conn = Connection("teste.db")
cards_repository = CardsRepository(conn)
router = APIRouter()


with open(BASE_ROOT / "templates" / "index.html", "r", encoding="utf8") as file:
    html_index = file.read()
with open(BASE_ROOT / "templates" / "cards.html", "r", encoding="utf8") as file:
    html_cards = file.read()


@router.get("/")
async def html():
    return HTMLResponse(content=html_index, status_code=200)

@router.get("/flashcards/")
async def render_flashcards_page():
    # Adicione o tema no conteúdo HTML, se necessário
    return HTMLResponse(content=html_cards, status_code=200)

@router.get("/sitemap.xml", response_class=Response)
async def sitemap():
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://flash-cards-fastapi.vercel.app/</loc>
            <priority>1.0</priority>
        </url>
    </urlset>
    """
    return Response(content=sitemap_content, media_type="application/xml")