# Zadanie 2: Walidacja i Przekształcenia Operacji na Macierzach
# Stwórz system, który przyjmuje operacje na macierzach jako stringi i wykonuje je dynamicznie,zapewniając jednocześnie walidację poprawności operacji:
# • Operacje mogą obejmować dodawanie, mnożenie i transponowanie macierzy.
# • System powinien sprawdzać poprawność operacji (zgodność wymiarów) i zwracać wynik w postaci macierzy.
# • Wykorzystaj eval() i exec() do wykonywania operacji na macierzach, a także funkcje walidacyjne, które sprawdzają poprawność przed wykonaniem.
# Wskazówka: Zaimplementuj walidację operacji i użyj funkcji funkcyjnych do przekształceń i obliczeń na macierzach.

import pandas as pd
import numpy as np 

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print(matrix_a)

matrix_a = [[1,2],[3,5]]

print(matrix_a)

