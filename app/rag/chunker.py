def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    """Split text into smaller chunks."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]