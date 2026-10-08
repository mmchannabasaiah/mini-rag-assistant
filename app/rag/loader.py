from pathlib import Path


def load_document(file_path: str) -> str:
    """Load a text document and return its contents."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {file_path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Currently only .txt files are supported")

    return path.read_text(encoding="utf-8")