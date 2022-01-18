edad = int(input("Ingrese su edad: "))
dosis = int(input("Ingrese cantidad de dósis aplicadas: "))

if edad >= 18 and dosis >= 2:
    print("Persona habilitada para ingresar")
elif edad > 18 and dosis >= 2:
    print("Personsa no cumple requisito de edad")
elif dosis < 2 and edad >= 18:
    print("Persona no cumple con requisito de vacunación")
elif edad < 18 and dosis < 2:
    print("Persona no cumple requisito de edad ni vacunación")