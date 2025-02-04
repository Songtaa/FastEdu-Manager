from app.domains.auth.repository.role import RoleRepository
from sqlmodel import Session
from app.domains.auth.schemas.role import (RoleCreate, RoleRead)
from app.domains.auth.models.role import Role
from sqlmodel.ext.asyncio.session import AsyncSession


class RoleService:
    def __init__(self, session: AsyncSession):
        self.role_repo = RoleRepository(session)

    def create_role(self, role_data: RoleCreate) -> Role:
        return self.role_repo.create_role(role_data.name)
