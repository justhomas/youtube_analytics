from typing import Optional
from pydantic import BaseModel


class VideoBase(BaseModel):
    video_id: str
    title: str
    trending_date : str
    title : str
    channel_title : str
    category_id : int
    publish_time : str
    tags : str
    views : int
    likes : int
    dislikes : int
    comment_count : int
    thumbnail_link : str
    comments_disabled : bool
    ratings_disabled : bool
    video_error_or_removed : bool
    description: str | None




class VideoCreate(VideoBase):
    pass


class VideoUpdate(VideoBase):
    pass


class VideoInDBBase(VideoBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Video(VideoInDBBase):
    pass


class VideoInDB(VideoInDBBase):
    pass
