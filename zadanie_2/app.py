import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    """Sprawdza, czy adres e-mail jest poprawny."""
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def calculate_rectangle_area(length: float, width: float) -> float:
    """Zwraca pole prostokąta."""
    if length < 0 or width < 0:
        raise ValueError("Długość i szerokość muszą być nieujemne")
    return length * width

def filter_and_sort_numbers(numbers: list[int], threshold: int) -> list[int]:
    """Zwraca posortowaną listę liczb większych od progu."""
    return sorted([n for n in numbers if n > threshold])

def convert_date_format(date_str: str, input_format: str, output_format: str) -> str:
    """Konwertuje format daty."""
    dt = datetime.strptime(date_str, input_format)
    return dt.strftime(output_format)

def is_palindrome(text: str) -> bool:
    # Usuwa wszystkie znaki niealfanumeryczne (ale zachowuje polskie litery)
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
