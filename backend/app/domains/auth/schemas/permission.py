from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional


class PermissionCreate(BaseModel):
    name: str

class PermissionRead(BaseModel):
    id: UUID
    name: str


