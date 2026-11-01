
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

from langchain_classic.retrievers.document_compressors import (
    CrossEncoderReranker
)


# Load reranking model
model = HuggingFaceCrossEncoder(
    model_name="cross-encoder/ms-marco-MiniLM-L6-v2"
)


# Create reranker
reranker = CrossEncoderReranker(
    model=model,
    top_n=5
)


# Rerank retrieved evidence
def rerank_documents(question, documents):

    if not documents:
        return []

    return reranker.compress_documents(
        documents,
        question
    )
