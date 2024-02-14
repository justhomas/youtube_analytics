from typing import Optional
from pydantic import BaseModel


class RegionBase(BaseModel):
    code: str
    name: str


class RegionCreate(RegionBase):
    pass


class RegionUpdate(RegionBase):
    pass


class RegionInDBBase(RegionBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Region(RegionInDBBase):
    pass


class RegionInDB(RegionInDBBase):
    pass
