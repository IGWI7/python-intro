import math

def calculate_mean(numbers: list) -> float:
    """
    Oblicza średnią arytmetyczną z listy liczb.

    Args:
        numbers (list): Lista liczb.

    Returns:
        float: Średnia arytmetyczna.

    Raises:
        ValueError: Jeśli lista jest pusta.
    """
    if not numbers:
        raise ValueError("Lista nie może być pusta.")
    return sum(numbers) / len(numbers)

def solve_quadratic(a: float, b: float, c: float) -> tuple:
    """
    Rozwiązuje równanie kwadratowe ax^2 + bx + c = 0.

    Args:
        a (float): Współczynnik a.
        b (float): Współczynnik b.
        c (float): Współczynnik c.

    Returns:
        tuple: Pierwiastki równania. Może być pusty, zawierać 1 lub 2 elementy.
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ()
    elif discriminant == 0:
        return (-b / (2*a),)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
