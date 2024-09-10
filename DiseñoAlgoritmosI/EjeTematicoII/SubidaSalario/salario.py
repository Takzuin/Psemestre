
salario = float(input("Introduce el salario mínimo actual: "))

# Definir el porcentaje de incremento
porcentaje_incremento = 4.2 / 100  # Convertir porcentaje a decimal

# Calcular el incremento
incremento = salario * porcentaje_incremento

# Calcular el nuevo salario mínimo
nuevo_salario = salario+ incremento

# Mostrar el nuevo salario mínimo
print(f"El nuevo salario mínimo para el próximo año es: {nuevo_salario:.2f}")
