## Pregunta: Que hace el método REMOVE en una LISTA?
## Respuesta: Remueve un elemento de la lista cuyo valor
##            sea igual al del argumento pasado

lista = [3, "HOLA", True, [2, 3, 6], "Mundo", 8]

lista.remove(True)

print(lista)

lista.remove([2, 3, 6])

print(lista)
