from pydantic import BaseModel, Field, EmailStr




class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=20)
    

class UserRegistrationSchema(UserLoginSchema):
    username: str
    
class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    