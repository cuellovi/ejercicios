frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

for i in frase:
    contador_letras = frase.count(letra)
    print(contador_letras)


