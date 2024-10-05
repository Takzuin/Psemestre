

print('Bienvenido al contador de Vocales')
texto = str(input('Ingresa el texto a analizar: ')).lower()

vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for i in texto:
    if i in vocales:
        vocales[i] += 1

print(f'Total Vocales: {vocales}')
