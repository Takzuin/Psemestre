# Leer las notas para cada actividad
while True:
    try:
        taller1 = float(input("Nota del Taller 1: "))
        if 1.0 <= taller1 <= 5.0:
            break
        print("Error: La nota debe estar entre 1.0 y 5.0.")
    except ValueError:
        print("Error: Entrada inválida. Ingresa un número válido.")

while True:
    try:
        taller2 = float(input("Nota del Taller 2: "))
        if 1.0 <= taller2 <= 5.0:
            break
        print("Error: La nota debe estar entre 1.0 y 5.0.")
    except ValueError:
        print("Error: Entrada inválida. Ingresa un número válido.")

while True:
    try:
        cuestionario1 = float(input("Nota del Cuestionario 1: "))
        if 1.0 <= cuestionario1 <= 5.0:
            break
        print("Error: La nota debe estar entre 1.0 y 5.0.")
    except ValueError:
        print("Error: Entrada inválida. Ingresa un número válido.")

while True:
    try:
        cuestionario2 = float(input("Nota del Cuestionario 2: "))
        if 1.0 <= cuestionario2 <= 5.0:
            break
        print("Error: La nota debe estar entre 1.0 y 5.0.")
    except ValueError:
        print("Error: Entrada inválida. Ingresa un número válido.")

while True:
    try:
        proyecto_final = float(input("Nota del Proyecto Final: "))
        if 1.0 <= proyecto_final <= 5.0:
            break
        print("Error: La nota debe estar entre 1.0 y 5.0.")
    except ValueError:
        print("Error: Entrada inválida. Ingresa un número válido.")

# Calcular la nota final
peso_taller1 = 0.20
peso_taller2 = 0.15
peso_cuestionario1 = 0.22
peso_cuestionario2 = 0.10
peso_proyecto_final = 0.36

nota_final = (taller1 * peso_taller1 +
              taller2 * peso_taller2 +
              cuestionario1 * peso_cuestionario1 +
              cuestionario2 * peso_cuestionario2 +
              proyecto_final * peso_proyecto_final)

nota_final = round(nota_final, 2)

# Evaluar la nota final
if nota_final >= 4.5:
    evaluacion = "Excelente"
elif nota_final >= 3.5:
    evaluacion = "Bueno"
elif nota_final >= 2.5:
    evaluacion = "Regular"
else:
    evaluacion = "Insuficiente"

# Mostrar resultados
print(f"\nNota final calculada: {nota_final}")
print(f"Evaluación cualitativa: {evaluacion}")
