def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
):

    chunks = []

    start = 0

    chunk_number = 1


    while start < len(text):

        end = start + chunk_size


        chunk = text[start:end]


        chunks.append(
            {
                "chunk_number": chunk_number,
                "content": chunk
            }
        )


        chunk_number += 1


        start = end - overlap


    return chunks