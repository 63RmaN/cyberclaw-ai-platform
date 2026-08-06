from sqlalchemy.orm import Session

from backend.app.models.document_chunk import DocumentChunk


def create_document_chunks(
    db: Session,
    document_id: int,
    chunks: list
):

    db_chunks = []


    for chunk in chunks:

        db_chunk = DocumentChunk(
            document_id=document_id,
            chunk_number=chunk["chunk_number"],
            content=chunk["content"]
        )

        db.add(db_chunk)

        db_chunks.append(db_chunk)


    db.commit()


    for chunk in db_chunks:
        db.refresh(chunk)


    return db_chunks



def get_chunks_by_document(
    db: Session,
    document_id: int
):

    return db.query(DocumentChunk).filter(
        DocumentChunk.document_id == document_id
    ).all()

def has_chunks_for_document(
    db: Session,
    document_id: int
):

    count = db.query(DocumentChunk).filter(
        DocumentChunk.document_id == document_id
    ).count()


    return count > 0