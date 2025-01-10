from fastapi import APIRouter, Depends, HTTPException
from core.security import create_access_token, pwd_context,hash_password,verify_user
from repository.UserRepository import UserRepository
from models.base_model.models import User
from fastapi.security import OAuth2PasswordRequestForm
from db.connection import get_db
from sqlalchemy.orm import Session
router = APIRouter()

# Rota de login
@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    user = user_repository.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Gerar o token JWT
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=User)
async def register_user(user: User,db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    # Verificações quanto aos dados enviados pelo usuário
    if not verify_user(user):
        raise HTTPException(status_code=400, detail="Invalid user data")
    
    # Gerar o hash da senha
    hashed_password = hash_password(user.hashed_password)

    # Criar o novo usuário

    new_user = User(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        hashed_password=hashed_password,
    )

    # Salvar o usuário no banco de dados
    user_repository.create_user(new_user)

    return new_user

