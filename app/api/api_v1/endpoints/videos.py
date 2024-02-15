from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/videos", response_model=List[schemas.Video])
def read_videos(
    db: Session = Depends(deps.get_db),
    skip: int = Query(0, alias="skip", ge=0),
    limit: int = Query(100, alias="limit", le=100),
    region_id: int | None = None,
    category_id: int | None = None,
) -> Any:
    """
    Retrieve videos with optional filters.
    """
    filters = {
        "region_id": region_id,
        "category_id": category_id,
    }

    videos = crud.video.get_multi(
        db=db,
        skip=skip,
        limit=limit,
        filters=filters,
    )
    return videos


@router.get("/videos/{video_id}", response_model=schemas.Video)
def read_video_by_id(
    video_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific video by id.
    """
    video = crud.video.get_by_id(db, video_id=video_id)
    return video


@router.put("/videos/{video_id}", response_model=schemas.Video)
def update_video(
    *,
    db: Session = Depends(deps.get_db),
    video_id: str,
    video_in: schemas.VideoUpdate,
) -> Any:
    """
    Update a video.
    """
    video = crud.video.update(db, video_id=video_id, obj_in=video_in)
    return video


@router.delete("/videos/{video_id}", response_model=schemas.Video)
def delete_video(
    video_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a video.
    """
    video = crud.video.remove(db, video_id=video_id)
    return video
