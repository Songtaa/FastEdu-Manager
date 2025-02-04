from app.db.base_class import APIBase
from pydantic import EmailStr
from sqlalchemy import Column, String
from sqlmodel import Field, Relationship
from uuid import uuid4, UUID
from typing import List



class UserRole(APIBase, table=True):
    user_id: UUID = Field(foreign_key="user.id", primary_key=True)
    role_id: UUID = Field(foreign_key="role.id", primary_key=True)
