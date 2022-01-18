dosis = int(input("Ingrese cantidad de dósis aplicadas: "))

if dosis == 0:
    print("Su inmunización es baja")
elif dosis > 0 and dosis <= 1:
    print("Su inmunización es media")
elif dosis > 1 and dosis <= 2:
    print("Su inmunización es alta")
elif dosis > 2 and dosis <= 3:
    print("Su inmunización es óptima")
else:
    print("Categoría inválida")