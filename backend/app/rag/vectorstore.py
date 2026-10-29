
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from app.core.config import settings


# Gemini converts text into vectors
embeddings = GoogleGenerativeAIEmbeddings(
    model=settings.EMBEDDING_MODEL,
    google_api_key=settings.GEMINI_API_KEY
)


# Connect to our Pinecone index
vector_store = PineconeVectorStore(
    index_name=settings.PINECONE_INDEX_NAME,
    embedding=embeddings,
    pinecone_api_key=settings.PINECONE_API_KEY
)


# Store chunks in the correct investigation
def store_chunks(chunks, investigation_id, file_id):

    ids = []

    # Generate IDs like 12-0, 12-1, 12-2
    for i, chunk in enumerate(chunks):
        ids.append(f"{file_id}-{i}")

    return vector_store.add_documents(
        documents=chunks,
        ids=ids,
        namespace=f"investigation-{investigation_id}"
    )


# Semantic search using Gemini embeddings + Pinecone
def semantic_search(question, investigation_id, k=10):

    return vector_store.similarity_search(
        query=question,
        k=k,
        namespace=f"investigation-{investigation_id}"
    )


# Remove vectors belonging to one evidence file
def delete_file_vectors(investigation_id, file_id, chunk_count):

    ids = []

    for i in range(chunk_count):
        ids.append(f"{file_id}-{i}")

    if ids:
        vector_store.delete(
            ids=ids,
            namespace=f"investigation-{investigation_id}"
        )
