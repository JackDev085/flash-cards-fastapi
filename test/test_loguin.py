# tests/conftest.py

import pytest
from db.connection import engine, Base, SessionLocal
from models.users import Users
from fastapi.testclient import TestClient
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
    yield db

    # Limpa o banco de dados após o teste
    db.close()
    Base.metadata.drop_all(bind=engine)

    # Popula dados de teste
    user = Users(username="jack", hashed_password="hashed_jack123", email="jack@example.com", full_name="Jack Example")
    db.add(user)
    db.commit()
    db.refresh(user)

client = TestClient(app)

def test_login_success():
    # Simula o envio de dados corretos para login
    response = client.post(
        "/token",
        data={"username": "jack", "password": "jack123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_invalid_credentials():
    # Simula o envio de dados incorretos para login
    response = client.post(
        "/token",
        data={"username": "saocamilo", "password": "teste"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}
