from sqlalchemy.orm import Session

from backend.app.models.document import Document
from backend.app.schemas.document import DocumentCreate



def create_document(
    db: Session,
    document: DocumentCreate
):

    db_document = Document(
        knowledge_base_id=document.knowledge_base_id,
        filename=document.filename,
        file_type=document.file_type,
        storage_path=document.storage_path,
        status="Uploaded"
    )


    db.add(db_document)

    db.commit()

    db.refresh(db_document)

    return db_document



def get_documents(
    db: Session
):

    return db.query(Document).all()



def get_documents_by_knowledge_base(
    db: Session,
    knowledge_base_id: int
):

    return db.query(Document).filter(
        Document.knowledge_base_id == knowledge_base_id
    ).all()



def get_document_by_id(
    db: Session,
    document_id: int
):

    return db.query(Document).filter(
        Document.id == document_id
    ).first()



def update_document_status(
    db: Session,
    document_id: int,
    status: str
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()


    if document:

        document.status = status

        if status == "Processed":

            from datetime import datetime

            document.processed_at = datetime.utcnow()


        db.commit()

        db.refresh(document)


    return document



def update_extracted_text(
    db: Session,
    document_id: int,
    extracted_text: str
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()


    if document:

        document.extracted_text = extracted_text

        db.commit()

        db.refresh(document)


    return document