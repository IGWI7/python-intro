import csv

def load_csv(filepath: str) -> list:
    """
    Wczytuje dane z pliku CSV jako listę słowników.

    Args:
        filepath (str): Ścieżka do pliku CSV.

    Returns:
        list: Lista słowników z danymi z CSV.
    """
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def filter_data(data: list, key: str, value: str) -> list:
    """
    Filtruje dane według wartości podanego klucza.

    Args:
        data (list): Lista słowników.
        key (str): Klucz do sprawdzenia.
        value (str): Wartość, którą musi mieć dany klucz.

    Returns:
        list: Przefiltrowana lista słowników.
    """
    return [row for row in data if row.get(key) == value]
