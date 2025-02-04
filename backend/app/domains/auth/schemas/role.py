from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

class RoleCreate(BaseModel):
    name: str

class RoleRead(BaseModel):
    id: UUID
    name: str

class PermissionCreate(BaseModel):
    name: str

class PermissionRead(BaseModel):
    id: UUID
    name: str

class RoleWithPermissions(RoleRead):
    permissions: List[PermissionRead] = []
