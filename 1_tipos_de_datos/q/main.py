## Como se cortar variabkes string?
## Poniendo corchetes detras de la variable indicando
## el número de posición del caracter en dicho string

saludo = "Hola como te va, el jueves jugamos al futbol y al tenis"

encontrarFutbol = saludo.find("futbol")
encontrarTenis = saludo.find("tenis")

print(encontrarFutbol)
print(encontrarTenis)


#No se si hay una forma de utilizar una sola variable

cortarFubol = saludo[38:44]
cortarTenis = saludo[50:55]
print(cortarFubol, cortarTenis)