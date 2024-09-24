from fastapi import Body
from .schemas import HobbyCreateSChema

def hobbyForm(title: str = Body()) -> HobbyCreateSChema:
    
    return HobbyCreateSChema(
        title=title
    )