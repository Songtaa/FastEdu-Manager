from sqlmodel import Session, select
from app.domains.auth.models.permission import Permission

class PermissionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_permission(self, name: str):
        if self.session.exec(select(Permission).where(Permission.name == name)).first():
            return {"error": "Permission already exists"}
        permission = Permission(name=name)
        self.session.add(permission)
        self.session.commit()
        return {"message": "Permission created"}
