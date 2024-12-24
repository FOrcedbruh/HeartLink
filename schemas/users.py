from pydantic import BaseModel, Field, EmailStr
from datetime import datetime



class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=20)
    

class UserRegistrationSchema(UserLoginSchema):
    username: str
    
class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserReadSchema(UserSchema):
    registered_at: datetime