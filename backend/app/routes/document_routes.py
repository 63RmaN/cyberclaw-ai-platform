from fastapi import (
    APIRouter,
    Depends,
    status,
    UploadFile,
    File,
    HTTPException
)

from sqlalchemy.orm import Session

from backend.app.database import SessionLocal


from backend.app.services.document_service import (
    create_document,
    get_documents,
    get_documents_by_knowledge_base,
    get_document_by_id,
    get_document_by_hash
)


from backend.app.services.document_upload_service import (
    save_uploaded_document
)


from backend.app.services.document_hash_service import (
    calculate_file_hash
)


from backend.app.services.knowledge_ingestion_service import (
    ingest_document
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



@router.post(
    "/upload",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED
)
def upload_document(
    knowledge_base_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = save_uploaded_document(
        file
    )


    document_hash = calculate_file_hash(
        file_path
    )


    existing_document = get_document_by_hash(
        db,
        document_hash
    )


    if existing_document:

        raise HTTPException(
            status_code=409,
            detail="Document already exists"
        )


    document = DocumentCreate(
        knowledge_base_id=knowledge_base_id,
        filename=file.filename,
        file_type=file.content_type,
        storage_path=file_path,
        document_hash=document_hash
    )


    db_document = create_document(
        db,
        document
    )


    ingest_document(
        db=db,
        document_id=db_document.id,
        file_path=file_path
    )


    return db_document



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