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
    id: int

class ProfileProtectSchema(ProfileSchema):
    id: int

class ProfileUpdateSchema(BaseModel):
    bio: str | None = None
    hobbies: list[str] | None = None
    age: int | None = None
    surname: str | None = None
    firstname: str | None = None

class ProfileCreateSchema(BaseModel):
    user_id: int
    firstname: str = Field(min_length=2)
    surname: str
    gender: str | None = None
    age: int | None = None
    profileImages: list[str] | None = None
    hobbies: list[str] | None = None
    bio: str | None = None
