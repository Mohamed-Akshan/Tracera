
from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    JSONLoader
)


# Load evidence files
def load_document(file_path):

    file_type = Path(file_path).suffix.lower()

    if file_type in [".log", ".txt"]:
        loader = TextLoader(file_path, encoding="utf-8")

    elif file_type == ".pdf":
        loader = PyPDFLoader(file_path)

    elif file_type == ".json":
        loader = JSONLoader(
            file_path=file_path,
            jq_schema=".",
            text_content=False
        )

    else:
        raise ValueError("Unsupported file format")

    return loader.load()
