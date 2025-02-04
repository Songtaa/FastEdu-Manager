from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings
from sqlalchemy.pool import NullPool
from contextlib import asynccontextmanager

# Database configuration
DATABASE_URI = str(settings.SQLALCHEMY_DATABASE_URI)
ECHO = True  # Enable SQL query logging for debugging
POOL_PRE_PING = True
POOL_CLASS = NullPool  # Use NullPool for async connections

# Create async SQLAlchemy engine
async_engine = create_async_engine(
    DATABASE_URI,
    echo=ECHO,
    pool_pre_ping=POOL_PRE_PING,
    poolclass=POOL_CLASS
)

# Create the async session factory
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get session
# @asynccontextmanager
async def get_session() -> AsyncSession:
    """
    Asynchronous context manager for database sessions.
    Yields a session and ensures it is properly closed after use.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Base class for SQLModel
class Base(SQLModel):
    """
    Base class for all SQLModel entities.
    """
    pass

# from sqlmodel import SQLModel
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
# from app.config.settings import settings
# from sqlalchemy.pool import NullPool

# # Create async SQLAlchemy engine
# async_engine = create_async_engine(
#     str(settings.SQLALCHEMY_DATABASE_URI),  # Database URI from settings
#     echo=True,  # Optional: enables logging of SQL queries, useful for debugging
#     pool_pre_ping=True,
#     poolclass=NullPool  # Adjust the pool type based on your needs
# )

# # Create the async session factory
# AsyncSessionLocal = sessionmaker(
#     bind=async_engine,
#     class_=AsyncSession,
#     expire_on_commit=False
# )

# # Dependency to get session
# async def get_session() -> AsyncSession:
#     async with AsyncSessionLocal() as session:
#         try:
#             yield session
#         finally:
#             await session.close()

# # Use SQLModel's base class
# class Base(SQLModel):
#     pass
