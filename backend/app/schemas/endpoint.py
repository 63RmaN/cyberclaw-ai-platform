from datetime import datetime

from pydantic import BaseModel


class EndpointCreate(BaseModel):

    hostname: str

    operating_system: str

    ip_address: str

    agent_version: str

    language: str = "English"

    organization_id: int


class EndpointResponse(BaseModel):

    id: int

    hostname: str

    operating_system: str

    ip_address: str

    agent_version: str

    language: str

    status: str

    last_heartbeat: datetime

    organization_id: int


    class Config:

        from_attributes = True