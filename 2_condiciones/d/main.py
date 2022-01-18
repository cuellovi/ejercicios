peso = float(input("Ingrese su peso en kgs: "))
altura = float(input("Ingrese su altura en mts: "))

imc = peso / (altura) ** 2

if imc < 18.5:
    print("Según su índice de masa corporal: ", imc, ", su peso es inferior al normal.")
elif imc >= 18.5 and imc < 24.9:
    print("Según su índice de masa corporal: ",imc, ", su peso es normal.")
elif imc >= 25 and imc < 29.9:
    print("Según su índice de masa corporal: ", imc, ", su peso es superior al normal.")
else:
    print("Según su índice de masa corporal: ", imc, ", su peso es obeso.")
