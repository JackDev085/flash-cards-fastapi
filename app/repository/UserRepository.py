from app.db.connection import Connection
from app.models.user import User
class UserRepository:
    def __init__(self, cursor: Connection):
        self._cursor = cursor

    def get_user_by_username(self, username: str):
        sql = "SELECT * FROM users WHERE username = (?)"
        self._cursor.execute_query(sql, (username,))
        return self._cursor.fetch_one()
    
    def create_user(self, user:User):
        sql = "INSERT INTO users (username, full_name, email, hashed_password) VALUES (?, ?, ?, ?)"
        self._cursor.execute_query(sql, (user.username, user.full_name, user.email, user.hashed_password))
        return self._cursor.fetch_one()