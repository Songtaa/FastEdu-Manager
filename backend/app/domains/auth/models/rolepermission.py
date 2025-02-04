from app.db.base_class import APIBase
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4, UUID
from app.domains.auth.models import role, permission

class RolePermission(SQLModel, table=True):
    role_id: UUID = Field(foreign_key="role.id", primary_key=True)
    permission_id: UUID = Field(foreign_key="permission.id", primary_key=True)