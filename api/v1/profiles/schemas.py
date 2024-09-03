from pydantic import BaseModel, Field



    
    
class ProfileSchema(BaseModel):
    user_id: int
    firstname: str = Field(min_length=2)
    surname: str
    gender: str
    age: int
    profileImage: list[str]
    hobbies: list[str]
    bio: str = Field(max_length=300)

class ProfileProtectSchema(ProfileSchema):
    id: int