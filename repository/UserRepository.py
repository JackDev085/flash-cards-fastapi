
from models.models import User
from db.connection import Connection
class UserRepository:
    def __init__(self, db:Connection):
        self.db = db

    def get_user_by_username(self, username: str)->User:
        return self.db.execute_query("SELECT * FROM users WHERE username = ?",(username,)).fetchone()

    def create_user(self, user:User)->User:
        try:
            self.db.execute_query("INSERT INTO users (username,full_name,email,hashed_password) VALUES (?,?,?,?)",(user.username,user.full_name,user.email,user.hashed_password))
            self.db.commit()
            self.db.refresh(user)
        except:
            self.db.rollback()
            raise Exception("Erro ao inserir usuário no banco de dados")
        return user
    
    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()