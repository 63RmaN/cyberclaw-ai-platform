import os

from fastapi import UploadFile


STORAGE_DIRECTORY = "storage"



def save_uploaded_document(
    file: UploadFile
):

    if not os.path.exists(
        STORAGE_DIRECTORY
    ):

        os.makedirs(
            STORAGE_DIRECTORY
        )


    file_path = os.path.join(
        STORAGE_DIRECTORY,
        file.filename
    )


    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            file.file.read()
        )


    return file_path