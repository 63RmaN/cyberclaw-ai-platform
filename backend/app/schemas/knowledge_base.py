from pydantic import BaseModel


class KnowledgeBaseCreate(BaseModel):

    name: str

    description: str | None = None

    type: str = "General"

    organization_id: int



class KnowledgeBaseResponse(BaseModel):

    id: int

    name: str

    description: str | None = None

    type: str

    status: str

    organization_id: int


    class Config:
        from_attributes = True