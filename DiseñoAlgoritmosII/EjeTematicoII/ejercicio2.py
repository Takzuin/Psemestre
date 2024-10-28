
nombres = []

print("Introduce los nombres (deja en blanco para terminar):")
while True:
    nombre = input("Nombre: ")
    if nombre == "":
        break
    nombres.append(nombre)

nombres_ordenados = sorted(nombres)


print("\nLista de nombres en orden alfabético:")
for nombre in nombres_ordenados:
    print(nombre)