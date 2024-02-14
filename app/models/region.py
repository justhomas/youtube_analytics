from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Region(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    name = Column(String)
