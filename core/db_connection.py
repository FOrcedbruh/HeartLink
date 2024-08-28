from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from .settings import settings
from typing import AsyncGenerator


class DatabaseConnection():
    def __init__(self, db_url: str, db_echo: bool, echo_pool: bool, pool_size: int):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
            echo_pool=echo_pool,
            pool_size=pool_size
        ),
        self.session_factory: AsyncGenerator[AsyncSession, None] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        ),
    async def sesion_creation(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            


db_conn = DatabaseConnection(db_echo=settings.db.echo, db_url=settings.db.url, pool_size=settings.db.pool_size, echo_pool=settings.db.echo_pool)