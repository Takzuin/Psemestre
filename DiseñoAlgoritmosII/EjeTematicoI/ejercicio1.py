lista = []
lista_pares = []


def add_bro():
    try:
        while True:
            lista.append(input('Ingresa un numero: '))
            opcion = input('¿Desea continuar añadiendo numeros?(S/N): ')
            if opcion == 'S':
                continue
            else:
                break
    except ValueError:
        print('Error: Ingresa un Dato numerico')


def add_pares():
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
            

def main():
    add_bro()
    print(f'La lista es = {lista}')
    a = sum(lista_pares)
    print(f'La lista de pares es: {lista_pares}')
    print(f'La suma de la lista es: {a}')



main()