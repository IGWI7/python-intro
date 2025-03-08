# Tworzenie dwóch list i łączenie ich funkcją zip()
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip
lista1 = [10, 20, 30]
lista2 = ["a", "b", "c"]
polaczone = list(zip(lista1, lista2))  # Łączy listy w pary krotek
print("Połączone listy:", polaczone)

# Wykorzystanie funkcji sqrt() z modułu math
# Dokumentacja: https://docs.python.org/3/library/math.html#math.sqrt
import math

try:
    liczba = 25
    pierwiastek = math.sqrt(liczba)  # Oblicza pierwiastek kwadratowy
    print(f"Pierwiastek kwadratowy z {liczba} wynosi: {pierwiastek}")
except ValueError:
    print("Nie można obliczyć pierwiastka z liczby ujemnej!")

# Obsługa wyjątku ZeroDivisionError
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
try:
    wynik = 10 / 0  # Próba dzielenia przez zero
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
