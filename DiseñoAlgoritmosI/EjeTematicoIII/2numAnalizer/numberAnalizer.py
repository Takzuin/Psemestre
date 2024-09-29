# Solicitar al usuario ingresar tres números enteros diferentes
numeros = []

def main():
    # Solicitar los números al usuario
    numeros.append(int(input('Ingrese el número 1: ')))
    numeros.append(int(input('Ingrese el número 2: ')))
    numeros.append(int(input('Ingrese el número 3: ')))

    # Calcular el máximo, mínimo y el número medio
    max_num = max(numeros)
    min_num = min(numeros)
    medio = sum(numeros) - max_num - min_num

    # Calcular la suma y el promedio
    suma = sum(numeros)
    promedio = suma / len(numeros)

    # Mostrar resultados
    print(f'Mayor: {max_num}')
    print(f'Menor: {min_num}')
    print(f'Número medio: {medio}')
    print(f'Suma: {suma} y Promedio: {promedio:.2f}')

    # Llamar a la función que verifica pares e impares
    get_probability()


def get_probability():
    pares = 0
    impares = 0
    for i in numeros:
        if i % 2 == 0:
            pares += 1
            print(f'El número {i} es par')
        else:
            impares += 1
            print(f'El número {i} es impar')

    # Comparar cuántos pares e impares hay
    if pares > impares:
        print('Hay más números pares.')
    elif impares > pares:
        print('Hay más números impares.')
    else:
        print('Hay la misma cantidad de números pares e impares.')


main()
