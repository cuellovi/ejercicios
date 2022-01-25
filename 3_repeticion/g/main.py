suma_pares = 0
edad = int(input("Ingrese su edad: "))
 
for x in range(1,edad + 1):
    if x % 2 == 0:
        suma_pares = suma_pares + x
 
print(suma_pares)