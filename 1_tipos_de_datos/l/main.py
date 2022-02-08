## Que hace FIND en un string?
## Nos dice la posición en que se encuentra una letra
## o frase dentro de un string

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")

buscarpalabra = palabra1.find(palabra2)

print(buscarpalabra)

#Si pongo cualquier caracter y no está dentro de la palabra,
# me aparece en la posicion "-1"

##if buscarpalabra != "":
##    print(palabra2, "se encuentra en la posición: ", buscarpalabra, "de, ", palabra1)
##else:
 ##   print("No se encuentra", palabra2, "dentro de", palabra1)    
