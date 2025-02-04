from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.domains.auth.repository.role import RoleRepository
from app.domains.auth.repository.permission  import PermissionRepository
from app.domains.auth.repository.user_repository import UserRepository
from app.db.session import get_session
from uuid import UUID
from typing import Annotated
from sqlalchemy.ext.asyncio.session import AsyncSession


router = APIRouter()

sessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.post("/role")
async def create_role(name: str, session: sessionDep):
    return RoleRepository(session).create_role(name)


@router.post("/permission")
async def create_permission(name: str, session: sessionDep):
    return PermissionRepository(session).create_permission(name)


@router.post("/assign-role")
async def assign_role(user_id: UUID, role_id: UUID, session: sessionDep):
    return UserRepository(session).assign_role(user_id, role_id)


@router.post("/grant-permission")
async def grant_permission(role_id: UUID, permission_id: UUID, session: sessionDep):
    return RoleRepository(session).grant_permission(role_id, permission_id)


@router.post("/revoke-permission")
async def revoke_permission(role_id: UUID, permission_id: UUID, session: sessionDep):
    return RoleRepository(session).revoke_permission(role_id, permission_id)
