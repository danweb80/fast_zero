from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str | None
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str | None
    email: EmailStr

class UserList(BaseModel):
    users: list[UserPublic]