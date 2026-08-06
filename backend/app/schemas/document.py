from datetime import datetime

from pydantic import BaseModel



class DocumentCreate(BaseModel):

    knowledge_base_id: int

    filename: str

    file_type: str

    storage_path: str



class DocumentResponse(BaseModel):

    id: int

    knowledge_base_id: int

    filename: str

    file_type: str

    storage_path: str

    status: str

    created_at: datetime

    processed_at: datetime | None = None


    class Config:

        from_attributes = True