import pytest
from fastapi.testclient import TestClient
from db.connection import engine, Base, SessionLocal
from models.users import Users
from api.main import app

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



# Fixture para configurar o banco de dados de teste
@pytest.fixture(scope="function")
def db_session():
    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)

    # Cria a sessão de teste
    db = SessionLocal()

    # Popula dados de teste
    user = Users(username="jack", hashed_password="hashed_jack123", email="jack@example.com", full_name="Jack Example")
    db.add(user)
    db.commit()
    db.refresh(user)

    yield db

    # Limpa o banco de dados após o teste
    db.close()
    Base.metadata.drop_all(bind=engine)


# Cliente de Teste
client = TestClient(app)


# Teste de registro de usuário bem-sucedido
def test_register_user_success(db_session):
    # Simula o registro de um novo usuário
    response = client.post(
        "/register",
        json={
            "username": "new_user1",
            "hashed_password": "Testamd123#",
            "full_name": "New User",
            "email": "teste1323@gmail.com"
        }
    )
    assert response.status_code == 200
    assert response.json()["username"] == "new_user1"
    assert response.json()["full_name"] == "New User"


# Teste de registro de usuário duplicado
def test_register_user_duplicate(db_session):
    # Simula o registro de um usuário já existente (que foi adicionado na fixture)
    response = client.post(
        "/register",
        json={
            "username": "jack",
            "hashed_password": "jack123",
            "full_name": "Existing User",
            "email": "string@gmail.com"
        }
    )
    assert response.status_code == 400
    assert response.json() in [{"detail": "Invalid user data"}, {"detail": "User already exists"}]

