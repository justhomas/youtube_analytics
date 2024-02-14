from .base import CRUDBase
from app.models.region import Region
from app.schemas.region import RegionCreate, RegionUpdate

region = CRUDBase[Region, RegionCreate, RegionUpdate](Region)
