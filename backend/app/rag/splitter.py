
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Create the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
)


# Split evidence into smaller chunks
def split_document(documents, investigation_id, file_id, filename):

    chunks = splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):

        chunk.metadata["investigation_id"] = investigation_id
        chunk.metadata["file_id"] = file_id
        chunk.metadata["filename"] = filename
        chunk.metadata["chunk_index"] = i

        # Unique ID for each chunk
        chunk.metadata["chunk_id"] = f"{file_id}-{i}"

    return chunks
