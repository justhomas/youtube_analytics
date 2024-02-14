from .base import CRUDBase
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

category = CRUDBase[Category, CategoryCreate, CategoryUpdate](Category)
