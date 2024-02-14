from fastapi import APIRouter

from app.api.api_v1.endpoints import videos
from app.api.api_v1.endpoints import categories
from app.api.api_v1.endpoints import regions

api_router = APIRouter()

api_router.include_router(videos.router, prefix="/videos", tags=["videos"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(regions.router, prefix="/regions", tags=["regions"])
