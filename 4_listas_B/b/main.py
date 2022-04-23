lista = []
contador_letras = 0

letra = input("introduzca una letra: ")
contador_letras = contador_letras + 1
lista.append(letra)
opcion =input("Desea agregar otra letra, presione 's' para si y 'n' para no: ")

while opcion == "s":
    if contador_letras == 10:
        break
    else:
        letra= input("Introduza otra letra: ")
        contador_letras= contador_letras + 1
        lista.append(letra)
        opcion =input("Desea agregar otra letra, presione 's' para si y 'n' para no: ")

buscar_letra=input("Ingrese una letra para buscarla dentro de la lista: ")

if buscar_letra in lista:
   print ("la letra aparece", lista.count(buscar_letra),"vez/veces")
else:
    print("La letra no aparece")
   
    
    

