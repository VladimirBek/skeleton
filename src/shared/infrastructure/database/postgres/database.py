"""
    Sql alchemy database adapter
"""
from asyncio import shield
from typing import Iterator, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from src.shared.config import Settings
from src.shared.dependencies import get_settings

__SETTINGS: Settings = get_settings()

__SQLALCHEMY_DATABASE_URL = 'postgresql://{PG_DB_USER}:{PG_DB_PASS}@{PG_DB_HOST}:{PG_DB_PORT}/{PG_DB_NAME}'.format(
    **dict(__SETTINGS)
)

__SQLALCHEMY_DATABASE_URL_ASYNC = 'postgresql+asyncpg://{PG_DB_USER}:{PG_DB_PASS}@{PG_DB_HOST}:{PG_DB_PORT}/{PG_DB_NAME}'.format(
    **dict(__SETTINGS)
)

engine = create_engine(
    __SQLALCHEMY_DATABASE_URL,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

async_engine = create_async_engine(url=__SQLALCHEMY_DATABASE_URL_ASYNC,
                                   pool_pre_ping=True,
                                   # Настройки таймаутов
                                   pool_timeout=60,  # Увеличить timeout получения соединения
                                   pool_recycle=7200,  # Пересоздавать каждые 2 часа вместо 1
                                   # Размеры пула
                                   pool_size=10,
                                   max_overflow=20
                                   )
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, autocommit=False, autoflush=False,
    expire_on_commit=False
)


def get_session() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    db = AsyncSessionLocal()
    try:
        yield db
        await db.commit()
    except Exception:
        await db.rollback()
        raise
    finally:
        if db:
            await shield(db.close())
