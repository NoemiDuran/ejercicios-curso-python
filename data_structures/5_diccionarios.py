"""Ejercicio 5: Diccionarios

Objetivos de aprendizaje

* Declaración de diccionarios
* Diferencia entre listas y diccionarios
* Leer, añadir, modificar y eliminar elementos
"""

user = {
    'name': 'Mauricio',
    'username': '@mauriciochavez_',
    'birthday': '21-12-98',
    'languages': ['javascript', 'python', 'java', 'dart'],
}

# 1. Imprime en pantalla el nombre del usuario

# 2. Añade un nuevo par llave-valor al diccionario, por ejemplo: licenciatura
user['licenciatura'] = 'cienciascompu'

# 3. Modifica los lenguajes favoritos de Mauricio, quitando Java de la lista

# 4. Elimina "username" y "birthday" del diccionario usando dos métodos distintos
#metodo 1
del user['username']
del user['birthday']

# 5. Declara un nuevo diccionario vacío
diccionario = { }
