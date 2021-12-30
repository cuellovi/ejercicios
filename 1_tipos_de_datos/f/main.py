clavos = int(input("Ingrese cantidad de clavos que necesita: "))
tornillos = int(input("Ingrese cantidad de tornillos que necesita: "))

precio_clavos = float (clavos * 0.7)
precio_tornillos = float (tornillos * 1.25)

print("Cantidad de clavos vendidos: ", clavos)
print("Cantidad de tornillos vendidos: ", tornillos)
print("Dinero recaudado por la venta de clavos: ", precio_clavos)
print("Dinero recaudado por la venta de tornillos: ", precio_tornillos)