nombre = str(input('Ingresa el nombre: ')).capitalize()
edad = int(input('Ingresa la edad: '))

if edad >= 18:
    print(f'Nombre : {nombre} Edad:{edad} tienes edad para votar')
else:
    print(f'Nombre : {nombre} Edad:{edad} no tiene edad para votar')