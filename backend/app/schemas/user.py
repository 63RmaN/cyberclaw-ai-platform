from enum import Enum

from pydantic import BaseModel, EmailStr



class UserRole(str, Enum):

    admin = "admin"
    user = "user"



class UserCreate(BaseModel):

    username: str
    email: EmailStr
    password: str
    organization_id: int
    role: UserRole = UserRole.user



class UserResponse(BaseModel):

    id: int
    username: str
    email: EmailStr
    is_active: bool
    role: UserRole
    organization_id: int


    class Config:
        from_attributes = True