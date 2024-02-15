from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from .region import region_categories

class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category_id = Column(Integer, unique=True)
    regions = relationship("Region", secondary=region_categories, back_populates="categories")

