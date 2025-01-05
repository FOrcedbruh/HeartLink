from pydantic import BaseModel



class SetttingsModelCreateSchema(BaseModel):
    color_theme: str = "light"
    dynamic_navbar: bool = True
    user_id: int

class SettingsModelReadSchema(SetttingsModelCreateSchema):
    id: int

class SettingsModelUpdateSchema(BaseModel):
    color_theme: str | None = None
    dynamic_navbar: bool | None = None