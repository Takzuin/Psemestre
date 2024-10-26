# Definimos cada operación como una función lambda
suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b if b != 0 else "Error: División por cero"

# Función principal de la calculadora
def calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elige una opción (1/2/3/4): ")

    # Validamos la entrada
    if opcion in ['1', '2', '3', '4']:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        # Ejecutamos la operación seleccionada usando la función lambda correspondiente
        if opcion == '1':
            print(f"Resultado: {suma(a, b)}")
        elif opcion == '2':
            print(f"Resultado: {resta(a, b)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == '4':
            print(f"Resultado: {division(a, b)}")
    else:
        print("Opción inválida")

# Llamamos a la función calculadora
calculadora()
