# Calculadora básica usando funciones lambda
calculadora = {
    '1': lambda a, b: a + b,
    '2': lambda a, b: a - b,
    '3': lambda a, b: a * b,
    '4': lambda a, b: a / b if b != 0 else "Error: División por cero"
}

# Muestra el menú y ejecuta la operación
def ejecutar_calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion in calculadora:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = calculadora[opcion](a, b)
        print(f"Resultado: {resultado}")
    else:
        print("Opción inválida")

# Ejecuta la calculadora
ejecutar_calculadora()
