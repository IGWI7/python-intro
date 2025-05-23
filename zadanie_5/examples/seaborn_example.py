"""
Przykład użycia biblioteki Seaborn do stworzenia wykresu pudełkowego.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Załadowanie przykładowego zbioru danych 'tips'
    tips = sns.load_dataset("tips")

    # Tworzenie wykresu pudełkowego (boxplot)
    sns.boxplot(x="day", y="tip", data=tips)
    plt.title("Wykres pudełkowy - Seaborn")

    # Wyświetlenie wykresu
    plt.show()

if __name__ == "__main__":
    main()
