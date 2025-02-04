from app.db.base_class import APIBase
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4, UUID
from typing import List
from permission import Permission
from users import User


class Role(APIBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    users: List["User"] = Relationship(back_populates="roles", link_model="UserRole")
    permissions: List["Permission"] = Relationship(back_populates="roles", link_model="RolePermission")