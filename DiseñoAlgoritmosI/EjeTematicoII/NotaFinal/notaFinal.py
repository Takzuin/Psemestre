def main():
    while True:
        try:
            # Solicitar las notas
            taller1 = float(input('Ingresa la nota del Taller 1: '))  
            taller2 = float(input('Ingresa la nota del Taller 2: '))
            cuestionario1 = float(input('Ingresa la nota del Cuestionario 1: '))
            cuestionario2 = float(input('Ingresa la nota del Cuestionario 2: '))
            proyecto_final = float(input('Ingresa la nota del Proyecto Final: '))
            
            # Calcular la nota final
            nota_final = (taller1 * peso_taller1 +
                          taller2 * peso_taller2 +
                          cuestionario1 * peso_cuestionario1 +
                          cuestionario2 * peso_cuestionario2 +
                          proyecto_final * peso_proyecto_final)
            
        except ValueError:
            print('Error: Dato Inválido')
            continue  # Continuar con la siguiente iteración si hay un error
        
        if 1.0 <= nota_final <= 2.9:
            print('Calificaion: Bajo')
            print(f'Nota final: {nota_final:.2f}')
        elif 2.9 <= nota_final <= 4.0:
            print("Calificacion: Basico")
            print(f'Nota final: {nota_final:.2f}')
        elif 4.0 <= nota_final <= 5.0:
            print("Calificacion: Superior")
            print(f'Nota final: {nota_final:.2f}')
        else:
            print('Ingresa notas entre el rango de 1.0 a 5.0')

        # Preguntar si desea realizar otro cálculo
        continuar = input('¿Deseas ingresar otro conjunto de notas? (s/n): ').strip().lower()
        if continuar != 's':
            print('Programa terminado.')
            break  # Salir del bucle

# Pesos para el cálculo de la nota final
peso_taller1 = 0.20
peso_taller2 = 0.15
peso_cuestionario1 = 0.22
peso_cuestionario2 = 0.10
peso_proyecto_final = 0.36

# Llamar a la función principal
main()
