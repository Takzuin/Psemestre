def sistema_de_compras():
    articulos = {}
    while True:
        nombre = input("Artículo ('fin' para terminar): ").strip()
        if nombre.lower() == 'fin': break
        try:
            precio = float(input(f"Precio de '{nombre}': "))
            cantidad = int(input(f"Cantidad de '{nombre}': "))
        except ValueError:
            print("Entrada no válida."); continue
        articulos[nombre] = {'precio': precio, 'cantidad': cantidad + articulos.get(nombre, {}).get('cantidad', 0)}

    total_articulos = sum(a['cantidad'] for a in articulos.values())
    total_sin_descuento = sum(a['precio'] * a['cantidad'] for a in articulos.values())
    descuento = 0.20 if total_articulos >= 5 else 0.10 if total_articulos >= 3 else 0
    total_final = total_sin_descuento * (1 - descuento) * (1.02 if total_articulos >= 3 else 1)

    print(f"\nTotal artículos: {total_articulos}\nTotal sin descuento: ${total_sin_descuento:.2f}\n"
          f"Descuento aplicado: ${total_sin_descuento * descuento:.2f}\n"
          f"Método de pago: {'Tarjeta' if total_articulos >= 3 else 'Efectivo'}\nTotal final: ${total_final:.2f}")

if __name__ == "__main__":
    sistema_de_compras()
