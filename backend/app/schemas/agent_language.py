from pydantic import BaseModel


class AgentLanguageCreate(BaseModel):

    language: str

    is_default: bool = False


class AgentLanguageResponse(BaseModel):

    id: int

    agent_id: int

    language: str

    is_default: bool


    class Config:

        from_attributes = True