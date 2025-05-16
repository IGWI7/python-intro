import re

def clean_text(text: str) -> str:
    """
    Usuwa znaki specjalne i zamienia tekst na małe litery.

    Args:
        text (str): Tekst wejściowy.

    Returns:
        str: Oczyszczony tekst.
    """
    return re.sub(r'[^\w\s]', '', text).lower()

def count_words(text: str) -> int:
    """
    Zlicza słowa w tekście.

    Args:
        text (str): Tekst wejściowy.

    Returns:
        int: Liczba słów.
    """
    return len(text.split())
