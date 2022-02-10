## Que hace FIND en un string?
## Nos dice la posición en que se encuentra una letra
## o frase dentro de un string

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")

buscarpalabra = palabra1.find(palabra2)

if buscarpalabra == -1:
    print(palabra2, "no se encuentra dentro de ", palabra1)

else:
    print(palabra2, "se encuentra en la posición: ", buscarpalabra, "dentro de ", palabra1)