"""Ejercicio 3: Matrices (listas de listas)

Objetivos de aprendizaje

* Comprender el concepto de matriz
* Acceder a los datos de una matriz

Obten el determinante de la siguiente matriz

Recuerda que el determinante se hace de la siguiente

    | n1 n2 |
    | n3 n4 |  = n1*n4 - n3*n2
"""

matrix = [
    [17, 49],
    [10, 13]
]

determinant = 0

d1 = matrix[0][0]* matrix[1][1]
d2 = matrix[0][1]* matrix[1][0]
determinante= 17*13 - 10*49
determinante= d1-d2
