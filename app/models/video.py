from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Video(Base):
    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String)
    title = Column(String)
