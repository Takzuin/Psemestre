
nombres = []

# Pedir al usuario que ingrese nombres (vacío para terminar)
print("Introduce los nombres (deja en blanco para terminar):")
while True:
    nombre = input("Nombre: ")
    if nombre == "":
        break
    nombres.append(nombre)

# Ordenar la lista de nombres alfabéticamente
nombres_ordenados = sorted(nombres)

# Imprimir la lista de nombres ordenados
print("\nLista de nombres en orden alfabético:")
for nombre in nombres_ordenados:
    print(nombre)