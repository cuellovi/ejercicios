empleado1 =[]
empleado2 =[]
empleado3 =[]
empleado4 =[]
empleado5 =[]

def CargarDatos(lista):
    nombre = input("Ingrese Nombre: ")
    lista.append(nombre)
    hijos = int(input("Ingrese cantidad de hijos: "))
    lista.append(hijos)
    antiguedad = int(input("Ingrese antiguedad: "))
    lista.append(antiguedad)
    estado_civil=input("Esta usted casado/a? s/n: ")
    lista.append(estado_civil)

#def Sueldo(lista):
    

CargarDatos(empleado1)
CargarDatos(empleado2)
CargarDatos(empleado3)
CargarDatos(empleado4)
CargarDatos(empleado5)

#Sueldo(empleado1)
#Sueldo(empleado2)
#Sueldo(empleado3)
#Sueldo(empleado4)
#Sueldo(empleado5)

sueldo_e1 = 100000 + (2000 * empleado1[1]) + (2000 * empleado1[2])
    if empleado1[3] == "s":
        sueldoe_e1 = sueldo_e1 + 5000
    print("El sueldo de ", empleado1[0], "es: ", sueldo_e1)

