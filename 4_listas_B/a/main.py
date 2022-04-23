lista = []
sumar_letras = 0

cantidad_palabras=int(input("Ingrese cuantas palabras quiere agregar a la lista: "))

for x in range(1, cantidad_palabras + 1):
    palabra=input("Ingrese una palabra: ")
    sumar_letras= sumar_letras + len(palabra)
    lista.append(palabra)

print("La cantidad de letras en la lista: ", lista, "es: ", sumar_letras)