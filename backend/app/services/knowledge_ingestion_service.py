from sqlalchemy.orm import Session

from backend.app.services.document_processor import (
    extract_text_from_pdf
)

from backend.app.services.document_chunker import (
    chunk_text
)

from backend.app.services.document_chunk_service import (
    create_document_chunks,
    has_chunks_for_document,
    get_chunks_by_document
)

from backend.app.services.document_service import (
    update_document_status
)


def ingest_document(
    db: Session,
    document_id: int,
    file_path: str
):

    if has_chunks_for_document(
        db,
        document_id
    ):

        print(
            "Document already processed. Returning existing chunks..."
        )

        return get_chunks_by_document(
            db,
            document_id
        )


    print("Extracting document text...")

    text = extract_text_from_pdf(
        file_path
    )


    print(
        f"Characters extracted: {len(text)}"
    )


    print("Creating chunks...")

    chunks = chunk_text(
        text
    )


    print(
        f"Chunks created: {len(chunks)}"
    )


    print("Saving chunks...")


    saved_chunks = create_document_chunks(
        db=db,
        document_id=document_id,
        chunks=chunks
    )


    print(
        f"Chunks saved: {len(saved_chunks)}"
    )


    update_document_status(
        db=db,
        document_id=document_id,
        status="Processed"
    )


    return saved_chunks