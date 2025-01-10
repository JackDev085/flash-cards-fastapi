"""from db.connection import Base
from sqlalchemy import Column, Integer, String


class Themes(Base):
    __tablename__ = "themes"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    theme_name = Column(String, nullable=False)
    """