from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.cards import router as cards_router
from routes.html import router as html_router
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
#from routes.translate import router as translate_router

BASE_ROOT = Path(__file__).resolve().parent

@asynccontextmanager
async def lifespan(app: FastAPI):

    data_hoje = datetime.now()

    log_file = BASE_ROOT / f"logs/logs{data_hoje.date()}.txt"
    #criate the log file

    # Início da aplicação
    with open (log_file, "a") as file:
        file.write(f"{data_hoje.time()} Starting the application\n")

    yield # Pausa aqui enquanto a aplicação está rodando
    
    # Fim da aplicação
    with open (log_file, "a") as file:
        file.write(f"{data_hoje.time()} - Stopping the application\n")

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
#app.include_router(translate_router)
