import json
import os

# Función para cargar contactos desde el archivo JSON
def cargar_contactos():
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as archivo:
            try:
                contenido = archivo.read().strip()  # Leemos el contenido y eliminamos espacios en blanco
                if contenido:  # Si el archivo no está vacío
                    return json.loads(contenido)
                else:
                    return {}  # Si está vacío, retornamos un diccionario vacío
            except json.JSONDecodeError:
                print("Error: El archivo JSON está corrupto.")
                return {}
    else:
        return {}

def guardar_contactos(contactos):
    with open('contacts.json', 'w') as archivo:
        json.dump(contactos, archivo, indent=4)


def añadir_contacto(contactos):
    nombre = input('Ingrese el nombre del contacto: ')
    if nombre in contactos:
        print('El contacto ya existe.')
    else:
        telefono = input('Ingrese el telefono del contacto: ')
        email = input('Ingrese el correo electronico del contacto: ')
        contactos[nombre] = {'telefono': telefono, 'email': email}
        guardar_contactos(contactos)
        print('Contacto añadido exitosamente.')


def actualizar_contacto(contactos):
    nombre = input('Ingrese el nombre del contacto que desea actualizar: ')
    if nombre in contactos:
        telefono = input(f'Nuevo telefono (actual: {contactos[nombre]['telefono']}): ')
        email = input(f'Nuevo correo (actual: {contactos[nombre]['email']}): ')
        contactos[nombre] = {'telefono': telefono, 'email': email}
        guardar_contactos(contactos)
        print('Contacto actualizado exitosamente. ')
    else:
        print('El contacto no existe.')


def eliminar_contacto(contactos):
    nombre = input('Ingrese el nombre del contacto que desea eliminar: ')
    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
        print('Contacto eliminado exitosamente.')
    else:
        print('El contacto no existe.')
    

def mostrar_contactos(contactos):
    if contactos:
        for nombre, info in contactos.items():
            print(f'Nombre: {nombre}, Telefono: {info['telefono']}, Correo: {info['email']}')
    else:
        print('No hay tantos contactos registrados.')

# Función principal con el menú
def menu():
    contactos = cargar_contactos()
    
    while True:
        print("\n--- Menú de Gestión de Contactos ---")
        print("1. Añadir contacto")
        print("2. Actualizar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            añadir_contacto(contactos)
        elif opcion == '2':
            actualizar_contacto(contactos)
        elif opcion == '3':
            eliminar_contacto(contactos)
        elif opcion == '4':
            mostrar_contactos(contactos)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
