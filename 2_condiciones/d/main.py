peso = float(input("Ingrese su peso en kgs: "))
altura = float(input("Ingrese su altura en mts: "))

# Hecho

imc = peso / (altura) ** 2

if imc < 18.5:
    print("Según su índice de masa corporal:",round(imc, 2),", su peso es inferior al normal.")
elif imc >= 18.5 and imc < 24.9:
    print("Según su índice de masa corporal: ",round(imc, 2),", su peso es normal.")
elif imc >= 25 and imc < 29.9:
    print("Según su índice de masa corporal: ",round(imc, 2),", su peso es superior al normal.")
else:
    print("Según su índice de masa corporal: ",round(imc, 2),", su peso es obeso.")
