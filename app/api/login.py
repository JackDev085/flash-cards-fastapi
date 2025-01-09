from fastapi import APIRouter, Depends, HTTPException
from app.core.security import create_access_token, pwd_context, user_repository,hash_password
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi import Request
router = APIRouter()

# Rota de login
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(form_data.password, user['hashed_password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return RedirectResponse(url="flashcards/")


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(form_data.password, user['hashed_password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Gerar o token JWT
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=User)
async def register_user(user: User):
    # Verificando se o usuário já existe
    existing_user = user_repository.get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

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

