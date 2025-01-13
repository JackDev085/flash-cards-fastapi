from fastapi import APIRouter
router = APIRouter(tags=["Home"])


@router.get("/")
async def index():
    return {"message": "go to /docs to see the documentation"}



'''@router.get("/sitemap.xml", response_class=Response)
async def sitemap():
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://flash-cards-fastapi.vercel.app/</loc>
            <priority>1.0</priority>
        </url>
    </urlset>
    """
    return Response(content=sitemap_content, media_type="application/xml")'''