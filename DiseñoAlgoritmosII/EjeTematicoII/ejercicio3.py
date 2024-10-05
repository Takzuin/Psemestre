palabras = []


print("Introduce las palabras (deja en blanco para terminar):")
while True:
    palabra = input("Palabra: ")
    if palabra == "":
        break
    palabras.append(palabra)

letra = input("\nLetra por la que deben comenzar las palabras: ").lower()


print(f"\nPalabras que comienzan con '{letra}':")
for palabra in palabras:
    if palabra.lower().startswith(letra):
        print(palabra)
