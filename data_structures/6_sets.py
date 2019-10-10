"""Ejercicio 6: Conjuntos (sets)

Objetivos de aprendizaje

* Declaración de sets
* Definición de set
* Añadir y eliminar elementos del set
* Operar dos sets
"""

even = {2, 4, 6, 8, 10}

# 1. Dado el set, añade el 12 al conjunto
even.add(12)
# 2. Dado el siguiente set, une ambos conjuntos en una nueva variable
# e imprímela en pantalla (ocupa ambos métodos vistos en clase)

odds = {1, 3, 5, 7, 11, 13}
nueva_variable = even.union(odds)
print(nueva_variable)

# 3. Usando el conjunto de pares (even), haz la interseccion con el siguiente conjunto

numbers = {5, 4, 3, 2, 1}

interseccion = even.intersection(numbers)
print(interseccion)

# 4. Guarda el resultado de restar el conjunto numbers a even en una variable
# Ocupa ambos métodos vistos en clase

resta_sets = numbers.difference(even)
print(resta_sets)

# 5. Dado el siguiente conjunto, elimina "German" de él.
# Luego intenta eliminar "Spanish" sin generar un error.

languages = {'English', 'French', 'German'}

languages.remove('German')
print(languages)
