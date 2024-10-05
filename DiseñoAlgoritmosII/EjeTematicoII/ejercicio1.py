# Pedir al usuario que ingrese una palabra o frase
frase = input("Ingresa una palabra o frase: ").lower()

# Inicializar un diccionario para contar las vocales
conteo_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Usar un ciclo for para contar las vocales
for letra in frase:
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

# Mostrar el conteo de cada vocal
for vocal, conteo in conteo_vocales.items():
    print(f"La vocal '{vocal}' aparece {conteo} veces.")

