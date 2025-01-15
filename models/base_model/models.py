from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    
class User(BaseModel):
    username: str
    full_name: str
    email: str
    plain_password: str
    
class AuthToken(BaseModel):
    username: str
    password: str

class UserNoPassword(BaseModel):
    username: str
    full_name: str
    email: str
    
class UserInDB(BaseModel):
    hashed_password: str