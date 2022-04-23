temperatura_maxima = []
temperatura_minima =[]
semana = 0

temp_max=float(input("Introduzca temperatura máxima: "))
temp_min=float(input("Introduzca temperatura mínima: "))

for x in range(1, 8):
    semana+= 1
    temperatura_maxima.append(temp_max)
    temperatura_minima.append(temp_min)
    temp_max=float(input("Introduzca temperatura máxima: "))
    temp_min=float(input("Introduzca temperatura mínima: "))


promedio_temp_maximas = sum(temperatura_maxima)/len(temperatura_maxima)
promedio_temp_minimas = sum(temperatura_minima)/len(temperatura_minima)

diferencia_promedio = promedio_temp_maximas - promedio_temp_minimas

print("La temperatura máxima mas alta es:" ,max(temperatura_maxima))
print("La temperatatura mínima mas baja es:" ,min(temperatura_minima))
print("La diferencia de promedios de las temperaturas max y min es: ", diferencia_promedio)