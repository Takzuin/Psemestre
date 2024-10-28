def main():
    mostrar_menu()
    pass

def mostrar_menu():
    print('Hola Bienvenido a la calculadora')
    print('1. Sumar')
    print('2. Resta')
    print('3. Division')
    print('4. Multiplicacion')
    opcion()

def opcion():
    opcion_usuario = int(input('Digite una opcion para continuar: '))
    if opcion_usuario == 1:
        sumar()
    elif opcion_usuario == 2:
        resta()
    elif opcion_usuario == 3:
        division()
    elif opcion_usuario == 4:
        multiplicacion()
    else:
        pass
    
numeros = []

def agregar_numeros():
    while True:
        numero = int(input('Ingrese el numero que desea añadir: '))
        numeros.append(numero)
        print(f'Numero agregado {numero}')
        break

def sumar():
    while True:
        opcion = input('Desea agregar mas numeros?: ')
        if opcion == 's':
            agregar_numeros()
        else:
            break
    print(f'Resultado de la suma: {sum(numeros)}')
    

def resta():
    while True:
        opcion = input('Desea agregar mas numeros?: ')
        if opcion == 's':
            agregar_numeros()
        else:
            break
        if len(numeros) > 0:
            resultado = numeros[0]
            for num in numeros[1:]:
                resultado -= num
            print(f'Resultado de la resta: {resultado}')
        else:
            print('No hay suficientes números para realizar la resta.')
    


def division():
    while True:
        opcion = input('¿Desea agregar más números? (s/n): ')
        if opcion == 's':
            agregar_numeros()
        else:
            break
    if len(numeros) > 0:
        resultado = numeros[0]
        try:
            for num in numeros[1:]:
                resultado /= num
            print(f'Resultado de la división: {resultado}')
        except ZeroDivisionError:
            print('Error: No se puede dividir por cero.')
    else:
        print('No hay suficientes números para realizar la división.')


def multiplicacion():
    while True:
        opcion = input('¿Desea agregar más números? (s/n): ')
        if opcion == 's':
            agregar_numeros()
        else:
            break
    if len(numeros) > 0:
        resultado = 1
        for num in numeros:
            resultado *= num
        print(f'Resultado de la multiplicación: {resultado}')
    else:
        print('No hay suficientes números para realizar la multiplicación.')

main()