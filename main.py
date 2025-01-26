from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.login import router as login_router
from api.users import router as users_router
from routes.cards import router as cards_router
from routes.html import router as html_router
#from routes.translate import router as translate_router
from contextlib import asynccontextmanager
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_ROOT = Path(__file__).resolve().parent

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Início da aplicação
    yield # Pausa aqui enquanto a aplicação está rodando
    # Fim da aplicação


app = FastAPI(
    title="FastAPI flash cards API",
    description="API for flash cards",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir qualquer origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rotas
app.include_router(cards_router)
app.include_router(html_router)
app.include_router(login_router)
app.include_router(users_router)
#app.include_router(translate_router)
