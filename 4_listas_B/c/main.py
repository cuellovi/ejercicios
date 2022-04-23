notas_mujeres = []
notas_hombres = []

alumno = input("Introduzca sexo de alumno, 'm,' mujer, 'h' hombre o 'f' para finalizar programa: ")


while alumno != "f":
    
    if alumno == "m":
        nota= int(input("Introduzca nota: "))
        notas_mujeres.append(nota)
        alumno = input("Introduzca sexo de alumno, 'm,' mujer, 'h' hombre o 'f' para finalizar programa: ")
        
   
    elif alumno == "h":
        nota= int(input("Introduzca nota: "))
        notas_hombres.append(nota)
        alumno = input("Introduzca sexo de alumno, 'm,' mujer, 'h' hombre o 'f' para finalizar programa: ")
        
        
            
        
if len(notas_mujeres) > 0:
    promedio_mujeres= sum(notas_mujeres)/len(notas_mujeres)
    print("El promedio de notas de las alumnas mujeres es: ", promedio_mujeres)
else:
    print("No hay nota de mujeres para promediar")

if len(notas_hombres) > 0:
    promedio_hombres= sum(notas_hombres)/len(notas_hombres)
    print("El promedio de notas de los alumnos hombres es: ", promedio_hombres)
else:
    ("No hay notas de hommbrse para promediar")



