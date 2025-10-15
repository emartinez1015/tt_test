from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class ProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    name: str

class ProjectUpdate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
