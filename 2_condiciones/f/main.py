edad = int(input("Ingreso permitido solo para mayores de edad, ingrese su edad: "))
if edad < 18:
    print("Usted es menor de edad no puede ingresar")
else:
    dosis = int(input("Ingrese cantidad de dósis aplicadas: "))
    if dosis >= 2:
        print("Persona habilitada para ingresar")
    else:
         print("Prohibido su ingreso por ser fan de milei")
   


