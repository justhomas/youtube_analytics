from .base import CRUDBase
from app.models.video import Video
from app.schemas.video import VideoCreate, VideoUpdate

video = CRUDBase[Video, VideoCreate, VideoUpdate](Video)
