
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from app.core.config import settings


# Gemini embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model=settings.EMBEDDING_MODEL,
    google_api_key=settings.GEMINI_API_KEY
)


# Connect to Pinecone
vector_store = PineconeVectorStore(
    index_name=settings.PINECONE_INDEX_NAME,
    embedding=embeddings,
    pinecone_api_key=settings.PINECONE_API_KEY
)


# Store document chunks
def store_chunks(chunks, investigation_id, file_id):

    ids = [f"{file_id}-{i}" for i in range(len(chunks))]

    vector_store.add_documents(
        documents=chunks,
        ids=ids,
        namespace=f"investigation-{investigation_id}"
    )


# Get a semantic retriever for one investigation
def semantic_retriever(investigation_id):

    return vector_store.as_retriever(
        search_kwargs={
            "k": 10,
            "namespace": f"investigation-{investigation_id}"
        }
    )
