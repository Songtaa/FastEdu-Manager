from uuid import UUID
from app.domains.auth.models.permission import Permission
from app.domains.auth.models.users import User
from sqlmodel import Field, Relationship
from typing import Optional
from app.db.base_class import APIBase


class UserPermission(APIBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    permission_id: int = Field(foreign_key="permission.id")

    user: Optional["User"] = Relationship(back_populates="user_permissions")
    permission: Optional["Permission"] = Relationship(back_populates="permission_users")