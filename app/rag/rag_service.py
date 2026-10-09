from app.rag.loader import load_document
from app.rag.chunker import chunk_text


def ask_question(question: str) -> str:
    document = load_document("data/documents/python.txt")

    chunks = chunk_text(
        document,
        chunk_size=100,
        overlap=20
    )

    return (
        f"Question: {question}\n"
        f"Document loaded successfully.\n"
        f"Number of chunks: {len(chunks)}"
    )