from fastapi import APIRouter, Depends, HTTPException
from core.security import get_current_active_user
from models.users import Users
from fastapi.responses import RedirectResponse
router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int, current_user: Users = Depends(get_current_active_user)):
    if current_user:
        # Logic to retrieve the item
        item = {"item_id": item_id, "owner": current_user.username}
        return item
    else:
        return RedirectResponse(url="/login")
