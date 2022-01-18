edad = int(input("Ingrese su edad: "))
dosis = int(input("Ingrese cantidad de dósis aplicadas: "))

# TODO: No informa que no deja ingresar a menores
# Teniendo en cuento lo anterior cambiar la lógica 
# La lógica actual está mal

if edad >= 18 and dosis >= 2:
    print("Persona habilitada para ingresar")
elif edad > 18 and dosis >= 2:
    print("Personsa no cumple requisito de edad")
elif dosis < 2 and edad >= 18:
    print("Persona no cumple con requisito de vacunación")
elif edad < 18 and dosis < 2:
    print("Persona no cumple requisito de edad ni vacunación")