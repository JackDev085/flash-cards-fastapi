from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.repository.CardsRepository import CardsRepository
from pathlib import Path
from app.db.connection import Connection
from fastapi import  Response
from fastapi import Depends
from app.core.security import get_current_user
from app.models.user import User
from fastapi.responses import RedirectResponse


BASE_ROOT = Path(__file__).resolve().parent.parent
conn = Connection("teste.db")
cards_repository = CardsRepository(conn)
router = APIRouter()


with open(BASE_ROOT / "templates" / "index.html", "r", encoding="utf8") as file:
    html_index = file.read()
with open(BASE_ROOT / "templates" / "cards.html", "r", encoding="utf8") as file:
    html_cards = file.read()
with open(BASE_ROOT / "templates" / "login.html", "r", encoding="utf8") as file:
    login = file.read()


@router.get("/login")
async def login_form():
    return HTMLResponse(content=login, status_code=200)


@router.get("/")
async def html():
    return HTMLResponse(content=html_index, status_code=200)

@router.get("/flashcards/")
async def render_flashcards_page(current_user: User = Depends(get_current_user)):
    if current_user:
        return HTMLResponse(content=html_cards, status_code=200)
    else:
        return RedirectResponse(url="/login")
    

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