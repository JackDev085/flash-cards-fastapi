from db.connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    category_name = Column(String, nullable=False)