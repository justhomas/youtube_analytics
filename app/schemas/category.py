from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str
    category_id: Optional[int]


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryInDBBase(CategoryBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Category(CategoryInDBBase):
    pass


class CategoryInDB(CategoryInDBBase):
    pass
