from pydantic import BaseModel, Field



    
    
class ProfileSchema(BaseModel):
    user_id: int
    firstname: str = Field(min_length=2)
    surname: str
    gender: str | None
    age: int | None
    profileImages: list[str] | None
    hobbies: list[str] | None
    bio: str | None = Field(max_length=300) 
    currentStage: int

class ProfileProtectSchema(ProfileSchema):
    id: int

class ProfileUpdateSchema(BaseModel):
    bio: str | None = None
    hobbies: list[str] | None = None
    age: int | None = None
    surname: str | None = None
