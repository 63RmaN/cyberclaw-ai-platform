from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal

from backend.app.services.document_service import (
    create_document,
    get_documents,
    get_documents_by_knowledge_base,
    get_document_by_id
)

from backend.app.schemas.document import (
    DocumentCreate,
    DocumentResponse
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.get(
    "",
    response_model=list[DocumentResponse]
)
def read_documents(
    db: Session = Depends(get_db)
):

    return get_documents(db)



@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_document(
    document: DocumentCreate,
    db: Session = Depends(get_db)
):

    return create_document(
        db,
        document
    )



@router.get(
    "/{document_id}",
    response_model=DocumentResponse
)
def read_document(
    document_id: int,
    db: Session = Depends(get_db)
):

    return get_document_by_id(
        db,
        document_id
    )



@router.get(
    "/knowledge-base/{knowledge_base_id}",
    response_model=list[DocumentResponse]
)
def read_documents_by_knowledge_base(
    knowledge_base_id: int,
    db: Session = Depends(get_db)
):

    return get_documents_by_knowledge_base(
        db,
        knowledge_base_id
    )