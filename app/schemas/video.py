from typing import Optional
from pydantic import BaseModel


class VideoBase(BaseModel):
    video_id: str
    title: str


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
