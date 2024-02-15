from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base

region_categories = Table(
    "region_categories",
    Base.metadata,
    Column("region_id", Integer, ForeignKey("region.id")),
    Column("category_id", String, ForeignKey("category.id")),
)

class Region(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    categories = relationship("Category", secondary=region_categories, back_populates="regions")
    videos = relationship("Video", back_populates="region")
