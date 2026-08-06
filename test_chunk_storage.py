from backend.app.database import SessionLocal

from backend.app.services.knowledge_ingestion_service import (
    ingest_document
)


db = SessionLocal()


try:

    chunks = ingest_document(
        db=db,
        document_id=1,
        file_path="storage/NIST.pdf"
    )


    print("\nIngestion completed")

    print(
        f"Total chunks returned: {len(chunks)}"
    )


finally:

    db.close()