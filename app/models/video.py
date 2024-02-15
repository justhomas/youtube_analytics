from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Video(Base):
    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String)
    title = Column(String)
    trending_date = Column(String)
    channel_title = Column(String)
    publish_time = Column(String)
    tags = Column(String)
    views = Column(Integer)
    likes = Column(Integer)
    dislikes = Column(Integer)
    comment_count = Column(Integer)
    thumbnail_link = Column(String)
    comments_disabled = Column(Boolean)
    ratings_disabled = Column(Boolean)
    video_error_or_removed = Column(Boolean)
    description = Column(String)

    region_id = Column(Integer, ForeignKey("region.id"))
    region = relationship("Region", back_populates="videos")

    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category")


