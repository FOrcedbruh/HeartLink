import pytest
from httpx import AsyncClient
from tests.test_config import settings_test
from config import settings, DatabaseConnection
from main import app
from dependencies import get_db


def overrides_get_db_connection() -> DatabaseConnection:
    return DatabaseConnection(
        db_url=settings_test.db.url,
        echo_pool=True,
        db_echo=True,
        pool_size=10
    )

app.dependency_overrides[get_db] = overrides_get_db_connection


@pytest.fixture(autouse=True)
async def async_client():
    async with AsyncClient(base_url=f"http://localhost:{settings.run.port}/api/v2/") as client:
        yield client







