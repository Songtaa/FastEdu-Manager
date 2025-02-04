from sqlmodel import Session, select
from models import Role, RolePermission
from uuid import UUID
from sqlalchemy.ext.asyncio.session import AsyncSession


class RoleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    def create_role(self, name: str):
        if self.session.exec(select(Role).where(Role.name == name)).first():
            return {"error": "Role already exists"}
        role = Role(name=name)
        self.session.add(role)
        self.session.commit()
        return {"message": "Role created"}

    def grant_permission(self, role_id: UUID, permission_id: UUID):
        role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
        self.session.add(role_permission)
        self.session.commit()
        return {"message": "Permission granted"}

    def revoke_permission(self, role_id: UUID, permission_id: UUID):
        role_permission = self.session.exec(select(RolePermission)
            .where(RolePermission.role_id == role_id)
            .where(RolePermission.permission_id == permission_id)).first()
        if not role_permission:
            return {"error": "Permission not found in role"}
        self.session.delete(role_permission)
        self.session.commit()
        return {"message": "Permission revoked"}
