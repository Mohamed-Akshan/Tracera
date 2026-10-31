
import re

from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever

from app.db.database import SessionLocal
from app.db.models import EvidenceFile

from app.rag.loaders import load_document
from app.rag.splitter import split_document
from app.rag.vectorstore import semantic_retriever


# Split technical text into searchable terms
def tokenize(text):
    return re.findall(r"[a-zA-Z0-9_.-]+", text.lower())


# Create BM25 retriever from uploaded evidence
def keyword_retriever(investigation_id):

    chunks = []

    with SessionLocal() as db:

        files = db.query(EvidenceFile).filter_by(
            investigation_id=investigation_id,
            status="ready"
        ).all()

        for file in files:

            documents = load_document(file.file_path)

            chunks.extend(
                split_document(
                    documents,
                    investigation_id,
                    file.id,
                    file.filename
                )
            )

    if not chunks:
        return None

    retriever = BM25Retriever.from_documents(
        chunks,
        preprocess_func=tokenize
    )

    retriever.k = 10

    return retriever


# Combine semantic search and BM25
def hybrid_search(question, investigation_id):

    vector_retriever = semantic_retriever(investigation_id)

    bm25_retriever = keyword_retriever(investigation_id)

    if not bm25_retriever:
        return []

    # Weighted Reciprocal Rank Fusion
    hybrid_retriever = EnsembleRetriever(
        retrievers=[vector_retriever, bm25_retriever],
        weights=[0.7, 0.3],
        id_key="chunk_id"
    )

    return hybrid_retriever.invoke(question)
