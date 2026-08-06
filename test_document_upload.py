from io import BytesIO

from fastapi import UploadFile

from backend.app.services.document_upload_service import (
    save_uploaded_document
)


test_file = UploadFile(
    filename="test_document.pdf",
    file=BytesIO(
        b"This is a CyberClaw upload test document."
    )
)


path = save_uploaded_document(
    test_file
)


print("File saved:")
print(path)