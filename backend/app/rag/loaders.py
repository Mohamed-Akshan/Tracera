
from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    JSONLoader
)


# Load evidence documents
def load_document(file_path):

    extension = Path(file_path).suffix.lower()

    if extension in [".log", ".txt"]:
        loader = TextLoader(file_path, encoding="utf-8")

    elif extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".json":
        loader = JSONLoader(
            file_path=file_path,
            jq_schema=".",
            text_content=False
        )

    else:
        raise ValueError("Unsupported file format")

    return loader.load()
