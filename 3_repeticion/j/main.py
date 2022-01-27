frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
total = 0
for i in frase:
    if i == letra:
       total += 1
print("La letra '%s' aparece %2i veces en la frase '%s'" % (letra, total, frase))

