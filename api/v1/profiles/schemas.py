from pydantic import BaseModel, Field



    
    
class ProfileSchema(BaseModel):
    user_id: int
    firstname: str = Field(min_length=2)
    surname: str
    gender: str
    age: int
    profileImage: list[str]
    hobbies: list[str]
    

class ProfileProtectSchema(ProfileSchema):
    id: int