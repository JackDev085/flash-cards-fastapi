from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_active_user
from app.models.user import User
router = APIRouter()

@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    try:
        return current_user
    except Exception as e:
        raise HTTPException(status_code=400, detail="User not found")

    