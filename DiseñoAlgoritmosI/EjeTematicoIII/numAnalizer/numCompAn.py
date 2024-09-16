#Solicite al usuario ingresar tres números enteros diferentes
numeros = []

numeros.append(int(input('Ingrese el numero 1: ')))
numeros.append(int(input('Ingrese el numero 2: ')))
numeros.append(int(input('Ingrese el numero 3: ')))


max = numeros[0]
min = numeros[0]

if numeros[1] > max:
    max = numeros[1]

if numeros[2] > max:
    max = numeros[2]

if numeros[1] < min:
    min = numeros[1]

if numeros[2] < min:
    min = numeros[2]

medio = numeros[0] + numeros[1] + numeros[2] - max - min
suma = numeros[1] + numeros[2] + numeros[3]
promedio = suma / len(numeros)

print(f'Mayor: {max} ')
print(f'Menor: {min}')
print(f'Suma: {suma} y Promedio: {promedio}')


#Verifique que los tres números sean únicos.
# Si se ingresa un número repetido, pida al usuario que ingrese otro número.
