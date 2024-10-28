import json

# Cargar inventario desde el archivo
def cargar_inventario():
    try:
        with open('inventory.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Guardar inventario en el archivo
def guardar_inventario(inventario):
    with open('inventory.json', 'w') as archivo:
        json.dump(inventario, archivo)

