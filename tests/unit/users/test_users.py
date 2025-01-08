import pytest
from httpx import AsyncClient
from fastapi import status

class TestUsers:

    @pytest.mark.asyncio
    async def test_create_user(self, async_client: AsyncClient):
        data = {
            "username": "Ilya",
            "email": "ilya@gmail.com",
            "password": "qwerty"
        }
        res = await async_client.post("auth/registration", json=data)
        assert res.status_code == status.HTTP_200_OK

    @pytest.mark.asyncio
    async def test_create_exists_user(self, async_client: AsyncClient):
        data = {
            "username": "Lexa",
            "email": "lexa@gmail.com",
            "password": "qwerty"
        }
        res = await async_client.post("auth/registration", json=data)
        assert res.status_code == status.HTTP_400_BAD_REQUEST