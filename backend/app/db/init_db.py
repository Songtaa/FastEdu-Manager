from app.config.settings import settings
from app.domains.auth.models.users import User
from app.domains.auth.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session
from app.domains.auth.services.user_service import UserService
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.db.base_class import APIBase
from sqlalchemy.future import select
from app.db.session import async_engine
from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from app.db.session import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.domains.auth.apis.users_router import create_user_Account



# engine = AsyncEngine(
#     create_engine(
#     str(settings.SQLALCHEMY_DATABASE_URI),  # From settings
#     pool_pre_ping=True,
#     poolclass=NullPool,  # Change the pool class based on your use case (e.g., QueuePool)
# ))

# async def init_db() -> None:
#     async with engine.begin() as conn:
#         # Create an AsyncSession instance
#         await conn.run_sync(APIBase.metadata.create_all)
#

# sessionDep = Annotated[AsyncSession, Depends(get_session)]

async def init_db() -> None:
    # Create tables
    async with async_engine.begin() as conn:
        # print(APIBase.metadata.tables.keys())
        await conn.run_sync(APIBase.metadata.create_all)

    # Create a default admin user
    async with AsyncSession(async_engine) as session:
        user_service = UserService(session)

        # Check if the admin user already exists
        if not await user_service.user_exists(settings.FIRST_SUPERUSER):
            # Create the admin user
            user_in = UserCreate(
                email=settings.FIRST_SUPERUSER,
                password=settings.FIRST_SUPERUSER_PASSWORD,
                full_name=settings.FIRST_SUPERUSER_NAME,
                user_role = settings.FIRST_SUPERUSER_ROLE,
                is_superuser=True,
            )
            await create_user_Account(user_data=user_in, session=session)
            await session.commit()


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28


# def init_db(db: Session) -> None:
#     # Tables should be created with Alembic migrations
#     # But if you don't want to use migrations, create
#     # the tables un-commenting the next lines
#     # from sqlmodel import SQLModel

#     # from app.core.engine import engine
#     # This works because the models are already imported and registered from app.models
#     # SQLModel.metadata.create_all(engine)

#     user = db.exec(
#         select(User).where(User.email == settings.FIRST_SUPERUSER)
#     ).first()
#     if not user:
#         user_in = UserCreate(
#             email=settings.FIRST_SUPERUSER,
#             password=settings.FIRST_SUPERUSER_PASSWORD,
#             is_superuser=True,
#         )
#         user = crud.create_user(session=db, user_create=user_in)
