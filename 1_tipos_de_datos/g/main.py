monto_prestamo = int(input("Ingrese monto de prestamo: "))

cuota = float (monto_prestamo / 3)
resto_cuota1 = monto_prestamo - cuota
porc_cuota1 = 8 * resto_cuota1 / 100
cuota1 = cuota + porc_cuota1
resto_cuota2 = monto_prestamo - cuota1
porc_cuota2 = 8 * resto_cuota2 / 100
cuota2 = cuota + porc_cuota2
resto_cuota3 = resto_cuota2 - cuota2
porc_cuota3 = 8 * resto_cuota3 / 100
cuota3 = cuota + porc_cuota3

interes_total = porc_cuota1 + porc_cuota2 + porc_cuota3

print("El monto total del prestamo es: $",monto_prestamo)
print("El monto de la primer cuota es: $",cuota1)
print("El monto de la segunda cuota es: $",cuota2)
print("El monto de la tercera cuota es: $",cuota3)
print("El interes total pagado es: $",interes_total)
