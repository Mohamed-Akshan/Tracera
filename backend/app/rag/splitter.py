from langchain_text_splitters import RecursiveCharacterTextSplitter


# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
)


# Split documents and add metadata
def split_document(documents, investigation_id, file_id, filename):

    chunks = text_splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):
        chunk.metadata["investigation_id"] = investigation_id
        chunk.metadata["file_id"] = file_id
        chunk.metadata["filename"] = filename
        chunk.metadata["chunk_index"] = i

    return chunks