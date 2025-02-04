from app.db.base_class import APIBase
from pydantic import EmailStr
from sqlalchemy import Column, String
from sqlmodel import Field, Relationship
from uuid import uuid4, UUID
from typing import List
from role import Role


class User(APIBase, table=True):
    email: EmailStr = Field(sa_column=Column(String(255), nullable=False, unique=True))
    password: str = Field(nullable=False, max_length=255)
    is_active: bool = Field(default=True)
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)
    # role: str =Field(sa_column=Column(String(255), nullable=False, server_default="user"))
    # role_id: UUID = Field(foreign_key="role.id")
    roles: List["Role"] = Relationship(back_populates="users", link_model="UserRole")


