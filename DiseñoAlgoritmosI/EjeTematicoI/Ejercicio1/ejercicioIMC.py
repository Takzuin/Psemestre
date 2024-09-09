peso = float(input('Digite su peso en KG: '))
estatura = float(input('Digite su estatura en metros: '))
IMC = peso / estatura ** 2

# Hacemos las distintas validaciones
if IMC >= 0 and IMC <= 15.99:
    print("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99:
    print("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
    print("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99:
    print("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
    print("Obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
    print("Obesidad media")
elif IMC >= 40.00:
    print("Obesidad morbida")
