matematica = []
quimica = []
fisica = []
historia = []

def NotaMasBaja(lista, materia):
    materia = materia
    print ("La nota mas baja de", materia, "es: ", min(lista))

def NotaMasAlta(lista, materia):
    materia= materia
    print("La nota mas alta de", materia, "es: ", max(lista))

def aprobados(lista, materia):
    materia = materia
    alumnos_aprobados = 0
    
    for i in lista:
        if i >= 4:
            alumnos_aprobados+=1
    print("La cantidad de alumnos aprobados en", materia, "es:", alumnos_aprobados)


alumno = input("Ingrese nombre de alumno: ")

while alumno != "":
    nota_mat = float(input("Ingrese nota de matemática: "))
    nota_qui = float(input("Ingrese nota de química: "))
    nota_fis = float(input("Ingrese nota de física: "))
    nota_his = float(input("Ingrese nota de historia: "))
    matematica.append(nota_mat)
    quimica.append(nota_qui)
    fisica.append(nota_fis)
    historia.append(nota_his)
    alumno = input("Ingrese nombre de alumno, si ya no hay alumnos presione enter: ")

NotaMasBaja(matematica, "Matematica")
NotaMasBaja(quimica, "Quimica")
NotaMasBaja(fisica, "Fisica")
NotaMasBaja(historia, "Historia")

NotaMasAlta(matematica, "Matematica")
NotaMasAlta(quimica, "Quimica")
NotaMasAlta(fisica, "Fisica")
NotaMasAlta(historia, "Historia")

aprobados(matematica, "Matemática")
aprobados(quimica, "Química")
aprobados(fisica, "Física")
aprobados(historia, "Historia")

prom_matematica = sum(matematica)/len(matematica)
prom_quimica = sum(quimica)/len(quimica)
prom_fisica = sum(fisica)/len(fisica)
prom_historia = sum(historia)/len(historia)

if prom_matematica > prom_quimica and prom_matematica > prom_fisica and prom_matematica > prom_historia:
    print("La materia que saco mayores notas es Matemática")
elif prom_quimica > prom_matematica and prom_quimica > prom_fisica and prom_quimica > prom_historia:
    print("La materia que saco mayores notas es Química")
elif prom_fisica > prom_matematica and prom_fisica > prom_quimica and prom_fisica > prom_historia:
    print("La materia que saco mayores notas es Física")
elif prom_historia > prom_matematica and prom_historia > prom_fisica and prom_historia > prom_quimica:
    print("La materia que saco mayores notas es Historia")
    