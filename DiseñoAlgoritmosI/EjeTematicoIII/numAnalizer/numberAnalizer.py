#Solicite al usuario ingresar tres números enteros diferentes
numeros = []


def main():
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
    suma = numeros[0] + numeros[1] + numeros[2]
    promedio = suma / len(numeros)

    print(f'Mayor: {max} ')
    print(f'Menor: {min}')
    print(f'Suma: {suma} y Promedio: {promedio}')
    get_problability()


def get_problability():
    for i in numeros:
        if i % 2 == 0:
            print(f'Numero {numeros.index(i)+1} es par')
        # Odd = Impar

        else:
            print(f'Numero {numeros.index(i)+1} es impar')
    if numeros[0] % 2 == 0 and numeros[1]:
        print('Hay mas numeros pares')
    elif numeros[0] % 2 == 0 and numeros[2]:
        print('Hay mas numeros pares')
    elif numeros[1] % 2 == 0 and numeros[3]:
        print('Hay mas numeros pares')
    else:
        print('Hay mas numeros impares.')



if __name__ == '__main__':
    main()
#Verifique que los tres números sean únicos.
# Si se ingresa un número repetido, pida al usuario que ingrese otro número.
