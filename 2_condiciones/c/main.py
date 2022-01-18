primer_palabra = input("Ingrese una palabra: ")
segunda_palabra = input("Ingrese otra palabra: ")

if len(primer_palabra) > len (segunda_palabra):
    print("La palabra ", primer_palabra, "es la mayor, tiene ", len(primer_palabra), "cantidad de letras")
elif len(primer_palabra) < len (segunda_palabra):
    print("La palabra ", segunda_palabra, "es la mayor, tiene ", len(segunda_palabra), "cantidad de letras")
else:
    print("Las palabras ", primer_palabra, "y", segunda_palabra, "tienen las mismas cantidad de letras")    