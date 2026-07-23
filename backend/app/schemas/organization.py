from pydantic import BaseModel

class OrganizationCreate(BaseModel):
    name: str
    description: str | None = None

class OrganizationResponse(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True