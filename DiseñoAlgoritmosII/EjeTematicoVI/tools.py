import json
import os

RUTA_DATOS = os.path.join(os.path.dirname(__file__), '..', 'datos', 'cuentas.json')

def cargar_datos():
    """Carga los datos de las cuentas desde el archivo JSON."""
    if os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_datos(cuentas):
    """Guarda los datos de las cuentas en el archivo JSON."""
    os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)
    with open(RUTA_DATOS, 'w') as archivo:
        json.dump(cuentas, archivo, indent=2)

def crear_cuenta():
    # Leer las cuentas existentes del archivo JSON
    try:
        with open(RUTA_DATOS, 'r') as archivo:
            cuentas = json.load(archivo)
    except FileNotFoundError:
        cuentas = []  # Si el archivo no existe, empezar con una lista vacía

    # Generar un número de cuenta único
    numeros_existentes = [int(cuenta['numero']) for cuenta in cuentas]
    nuevo_numero = None

    for i in range(1, 10000):  # De 0001 a 9999
        if i not in numeros_existentes:
            nuevo_numero = f"{i:04d}"  # Formato con 4 dígitos (0001, 0002, ..., 9999)
            break

    if nuevo_numero is None:
        print("Error: No se pueden crear más cuentas. Se ha alcanzado el límite máximo.")
        return

    # Pedir al usuario el PIN para la nueva cuenta
    print(f"Su número de cuenta es: {nuevo_numero}")
    pin = input("Ingrese un PIN para su cuenta: ")
    saldo = float(input("Ingrese el monto a ingresar a la cuenta: "))

    # Crear un diccionario para la nueva cuenta
    nueva_cuenta = {
        "numero": nuevo_numero,
        "pin": pin,
        "saldo": saldo
    }

    # Agregar la nueva cuenta a la lista de cuentas
    cuentas.append(nueva_cuenta)

    # Escribir la lista de cuentas actualizada de vuelta al archivo JSON
    with open(RUTA_DATOS, 'w') as archivo:
        json.dump(cuentas, archivo, indent=4)

    print(f"Cuenta creada exitosamente. Su número de cuenta es: {nuevo_numero}")

def verify():
    try:
        opcion = input('¿Tiene una cuenta creada(si/no)?')
        if opcion == 'si':
            pass
        else:
            crear_cuenta()

    except ValueError:
        print('Error: Dato ingresado Incorrecto')

        