from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/regions", response_model=List[schemas.Region])
def read_regions(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve regions.
    """
    regions = crud.video.get_multi(db, skip=skip, limit=limit)
    return regions


@router.get("/regions/{video_id}", response_model=schemas.Region)
def read_video_by_id(
    video_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific video by id.
    """
    video = crud.video.get_by_id(db, video_id=video_id)
    return video


@router.put("/regions/{video_id}", response_model=schemas.Region)
def update_video(
    *,
    db: Session = Depends(deps.get_db),
    video_id: str,
    video_in: schemas.RegionUpdate,
) -> Any:
    """
    Update a video.
    """
    video = crud.video.update(db, video_id=video_id, obj_in=video_in)
    return video


@router.delete("/regions/{video_id}", response_model=schemas.Region)
def delete_video(
    video_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a video.
    """
    video = crud.video.remove(db, video_id=video_id)
    return video
