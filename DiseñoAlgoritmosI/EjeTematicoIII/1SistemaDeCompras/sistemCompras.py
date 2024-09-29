# Se define la clase del Articulo

class Articulo():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Artículo: {self.nombre}, Precio: {self.precio}"


def main():
    show_menu()


def show_menu():
    try:
        print('Bienvenido al menú de Pago')
        print('Usa "1" para Iniciar')
        print('Usa "2" para Salir')
        opcion = int(input('Elige: '))
        if opcion == 1:
            print('Elegiste la opción "1"')
            crear_articulos()
        else:
            exit()

    except ValueError:
        print('Error: Ingresa un dato numérico')


articulos = []


# Función para crear artículos y calcular descuentos
def crear_articulos():
    while True:
        nombre = input('Introduce el nombre del artículo: ')
        precio = float(input(f"Introduce el precio de {nombre}: "))
        nuevo_articulo = Articulo(nombre, precio) 
        articulos.append(nuevo_articulo)

        # Cierre de bucle
        use = input('¿Agregar otro artículo? (s/n): ')
        if use.lower() != 's':
            break

    cant_art = len(articulos)  # Recalcula la cantidad de artículos
    valor_total = sum([articulo.precio for articulo in articulos])  # Suma total de los precios

    # Aplicación de descuentos según la cantidad de artículos
    if cant_art < 3:
        print('No tienes descuento.')
    elif 3 <= cant_art <= 4:
        print('Descuento del 10% aplicado.')
        valor_total *= 0.9  # Aplica el 10% de descuento
    elif cant_art >= 5:
        print('Descuento del 20% aplicado.')
        valor_total *= 0.8  # Aplica el 20% de descuento

    # Muestra los artículos y el valor total después del descuento
    print(f"\nArtículos Totales({cant_art}):")
    for articulo in articulos:
        print(articulo)
    if cant_art >= 3:
        print('El metodo de pago debe ser Tarjeta')
    else:
        print('El metodo de pago debe ser Efectivo')
    print(f"\nValor total después del descuento: {valor_total:.2f}")
    exit()


metodo_pago = ''


main()
