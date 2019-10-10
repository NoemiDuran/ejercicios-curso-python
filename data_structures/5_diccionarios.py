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
print(user['licenciatura'])

# 3. Modifica los lenguajes favoritos de Mauricio, quitando Java de la lista
del user['languages']
# 4. Elimina "username" y "birthday" del diccionario usando dos métodos distintos
#metodo 1
del user['username']
del user['birthday']
print(user)
#metodo 2
user_dos = user.pop('username')
user_tres = user.pop('birthday')
print(user_dos)
print(user_tres)
# 5. Declara un nuevo diccionario vacío
diccionario = { }
