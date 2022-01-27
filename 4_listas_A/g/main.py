## Pregunta: Que hace el método EXTEND en una LISTA?
## Respuesta: Agrega elementos en una lista de forma iterable
##            
## Pregunta: Cual es la diferencia entre APPEND y EXTEND?
## Respuesta: APPEND agregá un elemento al final de la lista,
##            EXTEND agrega un iterable que se encuentra dentro
##            de una variable

lista = [3, "HOLA", True, [2, 3, 6], "Mundo", 8]

print (lista)

a = [10]
b = [7, 2]

lista.extend(a)

print (lista)

lista.extend(b)

print (lista)