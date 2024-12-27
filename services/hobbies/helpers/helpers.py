from config import DatabaseConnection, settings
from sqlalchemy.ext.asyncio import AsyncSession

db = DatabaseConnection(
    db_url=settings.db.url,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    db_echo=settings.db.echo
)

async def get_async_session() -> AsyncSession:
    return await db.sesion_creation()