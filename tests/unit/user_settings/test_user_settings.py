import pytest
from fastapi import status


class TestUserSettings:

    @pytest.mark.asyncio
    async def test_get_user_settings_by_id(self, async_client):
        res = await async_client.get("user_settings/1")
        assert res.status_code == status.HTTP_200_OK

    @pytest.mark.asyncio
    async def test_get_not_found_user_settings_by_id(self, async_client):
        res = await async_client.get("user_settings/999")
        assert res.status_code == status.HTTP_404_NOT_FOUND