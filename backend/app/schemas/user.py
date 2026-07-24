from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    organization_id: int


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    organization_id: int

    class Config:
        from_attributes = True