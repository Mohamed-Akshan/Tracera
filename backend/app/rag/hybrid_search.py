
import json
from pathlib import Path

from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever

from app.rag.vector_store import vector_store


# Folder for storing BM25 evidence
BM25_DIR = Path(__file__).resolve().parents[2] / "data" / "bm25"


# 1. Save chunks for BM25 retrieval
def save_bm25(chunks, session_id):

    BM25_DIR.mkdir(parents=True, exist_ok=True)

    path = BM25_DIR / f"{session_id}.json"

    # Load previously saved chunks
    records = []

    if path.exists():
        with open(path, "r", encoding="utf-8") as file:
            records = json.load(file)

    # Keep existing chunks using their unique IDs
    saved = {}

    for record in records:
        chunk_id = record["metadata"]["chunk_id"]
        saved[chunk_id] = record

    # Add the new chunks
    for chunk in chunks:

        saved[chunk.metadata["chunk_id"]] = {
            "text": chunk.page_content,
            "metadata": chunk.metadata
        }

    # Save the evidence
    temporary = path.with_suffix(".tmp")

    with open(temporary, "w", encoding="utf-8") as file:
        json.dump(
            list(saved.values()),
            file,
            ensure_ascii=False
        )

    temporary.replace(path)


# 2. Create our hybrid retriever
def hybrid_search(question, session_id, k=10):

    # Semantic retriever using Pinecone
    vector_retriever = vector_store.as_retriever(
        search_kwargs={
            "k": k,
            "namespace": session_id
        }
    )

    # Load BM25 evidence for the current investigation
    path = BM25_DIR / f"{session_id}.json"

    if not path.exists():
        return vector_retriever.invoke(question)

    with open(path, "r", encoding="utf-8") as file:
        records = json.load(file)

    documents = []

    # Convert saved evidence into LangChain Documents
    for record in records:

        document = Document(
            page_content=record["text"],
            metadata=record["metadata"]
        )

        documents.append(document)

    if not documents:
        return vector_retriever.invoke(question)

    # BM25 Retriever - same as your reference
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = k

    # Hybrid Retriever - same as your reference
    hybrid_retriever = EnsembleRetriever(
        retrievers=[vector_retriever, bm25_retriever],
        weights=[0.7, 0.3],
        id_key="chunk_id"
    )

    # Retrieve documents using both methods
    retrieved_chunks = hybrid_retriever.invoke(question)

    return retrieved_chunks[:k]
