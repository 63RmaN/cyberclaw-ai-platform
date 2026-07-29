from pydantic import BaseModel


class AgentCreate(BaseModel):

    name: str

    description: str | None = None

    language: str

    industry: str

    role: str

    organization_id: int



class AgentResponse(BaseModel):

    id: int

    name: str

    description: str | None = None

    language: str

    industry: str

    role: str

    status: str

    organization_id: int

    class Config:
        from_attributes = True