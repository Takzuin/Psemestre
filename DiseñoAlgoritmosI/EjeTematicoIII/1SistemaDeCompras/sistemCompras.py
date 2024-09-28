# Se define la clase del Articulo
class Articulo():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Articulo: {self.nombre}, Precio: {self.precio}"


def main():
    mostrar_menu()


def mostrar_menu():
    try:
        print('Bienvenido al menu de Pago')
        print('Usa "1" para Ingresar los articulos')
        print('Usa "2" para ')
        print('Usa "3" para ')
        opcion = int(input('Elige: '))
        if opcion == 1:
            print('Elegiste la opcion "1"')

    except ValueError:
        print('Ingresa un dato Numerico')


# Funcion para crear Articulos
def crear_articulos():
    articulos = []

    while True:
        nombre = input('Introduce el nombre del articulo: ')
        precio = float(input(f"Introduce el precio de {nombre}"))
        nuevo_articulo = Articulo(nombre, precio) 
        articulos.append(nuevo_articulo)

        #Cierre de bucle
        use = input('¿Agregar otro articulo(s/n)')
        if use != 's':
            break

    print("\nArticulos: ")
    for articulo in articulos:
        print(articulo)

        

main()