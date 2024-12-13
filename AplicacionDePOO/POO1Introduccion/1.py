import os
class Vehiculo():
    def __init__(self):
        pass    

    def calcular_tarifa():
        pass


class Autobus(Vehiculo):
    
    def calcular_tarifa():
        try:
            os.system('cls')
            print('Este el menu de la tarifa de bus')
            print('1. Itagui \n2. Prado \n3. Bello \n4. Volver')
            opcion = input('Digite su opcion: ')
            tarifas = {'Itagui': 3500, 'Prado': 4500, 'Bello': 5000 }
            if opcion == '1':
                os.system('cls')
                print('La tarifa a Itagui es de: %s' %tarifas['Itagui'])
            if opcion == '2':
                os.system('cls')
                print('La tarifa a Prado es de: %s' %tarifas['Prado'])
            if opcion == '3':
                os.system('cls')
                print('La tarifa a Bello es de: %s' %tarifas['Bello'])
            else:
                pass
        except ValueError:
            print('Dato Incorrecto: Ingrese un numero en el rango indicado')


class Metro(Vehiculo):
    def calcular_tarifa():
        try:
            os.system('cls')
            print('Este es el menu de la tarifa del metro \nEstos son los Tipos de perfil \n1. Frecuente \n2. Discapacitado \n3. Tercera Edad \n4. Eventual \n5. Estudiantil \n6. Bancarizado \n7. Salir')
            tarifas = {'1':3210, '2':2350, '3':2900, '4':3650, '5':1350, '6':4150}
            opcion = input('Digite su opcion: ')
            if opcion == '1':
                os.system('cls')
                print('La tarifa para usuario Frecuente es de: %s' %tarifas['1'])
            if opcion == '2':
                os.system('cls')
                print('La tarifa para usuario discapacitado es de: %s' %tarifas['2'])
            if opcion == '3':
                os.system('cls')
                print('La tarifa para usuario discapacitado es de: %s' %tarifas['3'])
            if opcion == '4':
                os.system('cls')
                print('La tarifa para usuario discapacitado es de: %s' %tarifas['4'])
            if opcion == '5':
                os.system('cls')
                print('La tarifa para usuario discapacitado es de: %s' %tarifas['5'])
            if opcion == '6':
                os.system('cls')
                print('La tarifa para usuario discapacitado es de: %s' %tarifas['6'])
            if opcion == '7':
                print('Hasta luego')
                exit()
        except ValueError:
            print('Dato Incorrecto: Ingrese un numero en el rango indicado')

class Taxi(Vehiculo):
    def calcular_tarifa():
        print('Bienvenido al menu para tarifa de taxi')
        tiempo = input('¿Cuanto tiempo duro el viaje(En minutos)?')
        tarifa_normal = tiempo * 350
        if tiempo < '2':
            os.system('cls')
            print('Banderazo pague: 4.900')
        if tiempo < '5':
            os.system('cls')
            print('Tarifa Minima: 7.000')
        else:
            os.sytem('cls')
            print('El viaje Costo: %s' %tarifa_normal)
        

def main():
    print('Bienvenido al contador de Tarifas \nA continuacion las opciones disponibles: \n1. Autobus \n2. Metro \n3. Taxi')
    eleccion = input('¿En que vehiculo va a viajar hoy?(Digite el numero de opcion o "salir"): ')
    try:
        if eleccion == 'salir':
            exit()
        elif eleccion == '1':
            Autobus.calcular_tarifa()
        elif eleccion == '2':
            Metro.calcular_tarifa()
        elif eleccion == '3':
            Taxi.calcular_tarifa()
    except ValueError as e:
        print('Tipo de dato Erroneo')
    

main()