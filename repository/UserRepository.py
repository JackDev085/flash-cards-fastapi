
from sqlalchemy.orm import Session
from models.users import Users

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str):
        return self.db.query(Users).filter(Users.username == username).first()

    def create_user(self, user:Users):
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        except:
            self.db.rollback()
            raise
        return user
    
    def get_user_by_email(self, email: str):
        return self.db.query(Users).filter(Users.email == email).first()