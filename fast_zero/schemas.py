
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str | None
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    username: str | None
    email: EmailStr
