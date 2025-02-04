from app.db.base_class import APIBase
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4, UUID
from typing import List
from role import Role


class Permission(APIBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    roles: List["Role"] = Relationship(back_populates="permissions", link_model="RolePermission")
