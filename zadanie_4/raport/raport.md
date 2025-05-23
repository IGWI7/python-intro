# Raport z analizy wielokryterialnego podejmowania decyzji

## Cel analizy
Porównanie metod TOPSIS i SPOTIS do oceny zestawu alternatyw na podstawie trzech kryteriów o przypisanych wagach.

## Dane
- 4 alternatywy: A1, A2, A3, A4
- 3 kryteria (dwa minimalizowane, jedno maksymalizowane)
- Wagi kryteriów: 0.4, 0.4, 0.2

## Metody
- TOPSIS: metoda oparta na odległościach od rozwiązania idealnego i antyidealnego.
- SPOTIS: metoda wykorzystująca zakresy wartości kryteriów (bounds).

## Wyniki
Obie metody wskazały alternatywę A2 jako najlepszą, a A3 jako najgorszą.

## Wnioski
- Wyniki obu metod są spójne.
- Automatyczna normalizacja upraszcza proces analizy.
- SPOTIS wymaga podania zakresów kryteriów, co zwiększa precyzję oceny.

---

Analiza potwierdziła przydatność biblioteki pymcdm do wielokryterialnego podejmowania decyzji.
