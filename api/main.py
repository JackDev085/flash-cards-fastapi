from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from repository.CardsRepository import CardsRepository
from db.connection import Connection
from fastapi.staticfiles import StaticFiles
from routes.cards import router as cards_router
from routes.translate import router as translate_router
from routes.html import router as html_router

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
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(cards_router)
app.include_router(translate_router)
app.include_router(html_router)