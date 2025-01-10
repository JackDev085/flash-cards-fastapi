from db.connection import Base
from sqlalchemy import Column, Integer, String,ForeignKey

class Cards(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    theme = Column(String,nullable=False)