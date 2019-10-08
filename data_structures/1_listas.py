"""Ejercicio 1: Manejo de listas

Objetivos de aprendizaje

* Aprender a declarar listas
* Acceder a los elementos de una lista
* Modificar elementos en una lista
* Eliminar elementos de una listas 
* Ordenar temporal y permanente elementos en una lista
* Obtener la reversa y la longitud de una lista
* Estadística básica con una lista
* Concatenar listas
* Slices de una lista
* Manejar una lista como matriz
"""

# 1. Llena la siguiente lista con al menos 3 personajes de tu película favorita

characters = ['Jackie Chan', 'Jack Black', 'Zack Mooneyham']

# 2. Accede al primer elemento de la lista, e imprímelo en pantalla
# OJO: El código debajo solo es una guía. Reemplazalo con el tuyo

first_character = characters[3]
print(first_character)
print(characters[0])


# 3. Accede al penúltimo elemento, esta vez con números negativos
# OJO: El código debajo solo es una guía. Reemplazalo con el tuyo

first_character = characters[-5]
print(first_character)
print(characters[-1])

# 4. Modifica un elemento de la lista, e imprime la lista
characters = ['Jackie Chan', 'Jack Black', 'Drake Bell'] #ño
print(characters)

# Reemplaza esta línea por la modificación en tu lista
print(characters)

# 5. Añade un nuevo elemento a la lista, al principio y al final, e imprime la lista
# HINT: Usa dos distintos métodos
characters = ['Jackie Chan', 'Jack Black', 'Drake Bell']
characters.append(0, 'Actor X')
characters.append(3, 'Actor Y')

# Reemplaza esta línea por tus dos lineas de código
print(characters)

# Hacer caso omiso a la siguiente línea de código
characters[2] = 'Batman'

# 6. Explica, con comentarios, qué hace cada una de las siguientes líneas de código

del characters[3]  #elimina el tercer elemento de la lista
popped = characters.pop() #elimina el ultimo elemento agregado
popped_params = characters.pop(0) 
characters.remove('Batman') #elimina el elemento 'Batman'

# 7. Ordena temporalmente la lista, guarda la lista temporal en una variable
# e imprime tu lista de personajes y la nueva lista. Estas deberían ser diferentes
characters = ['Jackie Chan', 'Jack Black', 'Drake Bell']
characters.sort()
print(characters)

# 8. Ordena para siempre tu lista, e imprímela

# 9. Ordena tu lista al revés (ojo, NO pedimos la reversa de tu lista)

# 10. Haz la reversa de la siguiente lista
numbers  = [17, 20, 5, 10, 7]
numbers.sort(reverse=True)

# 11. Guarda en una variable la longitud de la lista de números
numbers  = ['17', '20', '5', '10', '7']
len(numbers)
# 12. Saca el mínimo, máximo y la suma de la lista de númeris
min(numbers)
max(numbers)
sum(numbers)
# 13. Concatena la lista de personajes y de números
numbers  = ['17', '20', '5', '10', '7']
personajes = ['Jackie Chan', 'Jack Black', 'Drake Bell']
lista_final = numbers + personajes
