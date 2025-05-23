"""
Przykład użycia biblioteki Matplotlib do stworzenia prostego wykresu liniowego.
"""

import matplotlib.pyplot as plt

def main():
    # Dane do wykresu
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Tworzenie wykresu
    plt.plot(x, y, marker='o')
    plt.title("Wykres liniowy - Matplotlib")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    # Wyświetlenie wykresu
    plt.show()

if __name__ == "__main__":
    main()
