"""Ejercicio 2: Slices de listas

Objetivos de aprendizaje

* Aprender a obtener slices de una lista
* Manejar el paso en slices
* Usar slices omitiendo parámetros
"""

superheroes = [
    'Batman',
    'Iron Man',
    'Thor',
    'Green Lantern',
    'Flash',
    'Wolverine'
]

# 1. Obten las siguientes listas a partir de slices
# Ojo: No puedes omitir parámetros

# a)  ['Iron Man', 'Thor', 'Green Lantern']
slice_1 = ['Wolverine', 'Iron Man', 'Thor', 'Green Lantern']
print(slice_1[1:4:2])

# b) ['Wolverine', 'Flash', 'Green Lantern', 'Thor']
#nose

# c) ['Batman', 'Thor', 'Flash']
#nose

# d) ['Iron Man', 'Thor', 'Green Lantern'] #este es el mismo que el a)



# 2. Omitiendo parámetros, obten las siguientes listas

# a) ['Batman', 'Iron Man', 'Thor']
slice_5 = superheroes[:]

# b) ['Green Lantern', 'Flash', 'Wolverine']
slice_6 = superheroes[:]

# c) ['Wolverine', 'Green Lantern', 'Iron Man']
slice_7 = superheroes[:]


print(slice_1)
print(slice_2)
print(slice_3)
print(slice_4)
print(slice_5)
print(slice_6)
print(slice_7)
