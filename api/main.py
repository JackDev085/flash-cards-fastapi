from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from teste import search_card,search_response
from pathlib import Path
from fastapi.responses import HTMLResponse

BASE_ROOT = Path(__file__).resolve().parent
BASE_ROOT = Path(__file__).resolve().parent

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


@app.get("/api/aleatory_card")
async def aleatory_card():
    return search_card()

@app.get("/")
async def html():


    with open(f"{BASE_ROOT}/index.html", "r", encoding="utf8") as file:
        html = file.read()
        return HTMLResponse(content=html, status_code=200)

@app.get("/api/search_response/{id}")
async def search_response_by_id(id:int):   
    return search_response(id)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)