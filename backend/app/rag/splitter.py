
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter


# Create text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
)


# Split documents and add source information
def split_document(documents, session_id):

    chunks = splitter.split_documents(documents)

    ready = []

    # Remove empty chunks
    for chunk in chunks:

        if not chunk.page_content.strip():
            continue

        # Get the original source path from the loader
        source = chunk.metadata.get("source", "unknown")

        # Get filename automatically from its path
        filename = Path(source).name

        # session_id identifies one investigation
        # Example: investigation-5
        chunk.metadata["session_id"] = session_id
        chunk.metadata["filename"] = filename

        ready.append(chunk)

    # Give each chunk a stable identifier
    for i, chunk in enumerate(ready):

        source = chunk.metadata.get("source", "unknown")
        page = chunk.metadata.get("page", 0)
        start = chunk.metadata.get("start_index", i)

        chunk.metadata["chunk_id"] = (
            f"{Path(source).stem}-{page}-{start}-{i}"
        )

    return ready
