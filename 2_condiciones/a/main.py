num_uno = int(input("Ingrese un número entero: "))
num_dos = int(input("Ingrese otro número entero: "))

if num_uno > num_dos:
    print(num_uno, "es mayor a ", num_dos)
elif num_uno < num_dos:
    print(num_dos, "es mayor a ", num_uno)
else:
    print("Los números son iguales")
