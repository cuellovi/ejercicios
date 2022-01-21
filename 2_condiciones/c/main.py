primer_palabra = input("Ingrese una palabra: ")
segunda_palabra = input("Ingrese otra palabra: ")

cant_letras1 = len(primer_palabra)
cant_letras2 = len(segunda_palabra)

# Ahí creo que lo mejoré, hago el conteo antes y los metí en 2 variables diferentes
# También corregí el enunciado, aparece como en el ejemplo

if cant_letras1 > cant_letras2:
    print("La palabra ", primer_palabra.upper(), "es la mayor y tiene ", cant_letras1, "caracteres")
elif cant_letras1 < cant_letras2:
    print("La palabra ", segunda_palabra.upper(), "es la mayor y tiene ", cant_letras2, "caracteres")
else:
    print("Las palabras ", primer_palabra.upper(), "y", segunda_palabra.upper(), "tienen las mismas cantidad de caracteres")    