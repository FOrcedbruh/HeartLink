from fastapi import status
import pytest

class TestHobbies:
    
    @pytest.mark.asyncio
    async def test_get_hobbies(self, async_client):
        res = await async_client.get("hobbies/")
        assert res.status_code == status.HTTP_200_OK