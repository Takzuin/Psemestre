# Tarifas por minuto
tarifas = {
    "usa": 900,
    "ca": 800,
    "eu": 950,
    "Rest": 1250
}

# Solicitar datos al usuario
destino = input("Ingrese el destino de la llamada: ")
duracion = int(input("Ingrese la duración de la llamada en minutos: "))

# Calcular el costo total
if destino in tarifas:
    costo_total = tarifas[destino] * duracion
    # Aplicar descuento si la duración es mayor a 15 minutos
    if duracion > 15:
        costo_total *= 0.8
    print(f"El costo total de la llamada es: {costo_total} pesos")
else:
    print("Destino no válido")
