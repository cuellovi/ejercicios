print("Seleccione la fruta a llevar")
print("1- Banana")
print("2- Frutilla")
fruta = int(input("Coloque un número según la fruta que va a llevar: "))
kilos = float(input("Ingrese cantidad de kgs a llevar, mínimo 1kg: "))
precio_banana = 100
precio_frutilla = 120

if fruta == 1:
    if kilos == 1:
        print("El precio total es: $", precio_banana)
    elif kilos >= 2 and kilos < 3:
        precio_banana = 10 * 100 / 100
        precio_banana = 100 - precio_banana
        precio_banana = kilos * precio_banana
        print("El precio total es: $", precio_banana)
    else: 
        precio_banana = 20 * 100 / 100
        precio_banana = 100 - precio_banana
        precio_banana = kilos * precio_banana
        print("El precio total es: $", precio_banana)

if fruta == 2:
    if kilos == 1:
        precio_frutilla = 5 * 120 / 100
        precio_frutilla = 120 - precio_frutilla
        precio_frutilla = kilos * precio_frutilla
        print("El precio total es: $", precio_frutilla)
    elif kilos >= 2 and kilos < 3:
        precio_frutilla = 15 * 120 / 100
        precio_frutilla = 120 - precio_frutilla
        precio_frutilla = kilos * precio_frutilla
        print("El precio total es: $", precio_frutilla)
    else: 
        precio_frutilla = 25 * 120 / 100
        precio_frutilla = 120 - precio_frutilla
        precio_frutilla = kilos * precio_frutilla
        print("El precio total es: $", precio_frutilla)



        
        