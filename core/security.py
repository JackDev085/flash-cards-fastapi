from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status,APIRouter
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic.types import Annotated
from repository.UserRepository import UserRepository
from models.user import User
from db.connection import Connection
from models.user import TokenData
from core.configs import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

import shutil
from pathlib import Path

# Caminho original do banco de dados (supondo que esteja no mesmo diretório que seu código)
ORIGINAL_DB_PATH = "teste.db"  # Caminho do banco de dados original

# Caminho temporário no Vercel
TEMP_DB_PATH = "/tmp/db.sqlite3"  # Vercel cria o diretório /tmp para dados temporários

# Copiar o banco de dados original para /tmp, se ele ainda não existir lá
if not Path(TEMP_DB_PATH).exists():
    shutil.copy(ORIGINAL_DB_PATH, TEMP_DB_PATH)

# Conectar ao banco de dados temporário
conn = Connection(TEMP_DB_PATH)

user_repository = UserRepository(conn)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user_repository = UserRepository(conn)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = user_repository.get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# funcao para saber se o usuario esta ativo
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# funcao para buscar o usuario atual


# função para criar o token de acesso
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Função de hash da senha
def hash_password(password: str):
    return pwd_context.hash(password)