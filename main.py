from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from teste import search_card


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


@app.get("/")
async def root():
    return search_card()