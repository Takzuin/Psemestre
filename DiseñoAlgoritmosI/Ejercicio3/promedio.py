def main():
    notas = []  # Crear una lista vacia para las notas
    
    while True:
        nota_str = input("Ingresa una nota o (ingrese OK para terminar el programa)): ")
        
        if nota_str.upper() == 'OK':
            break  # Salir del programa cuando se ingrese 'ok'
        
        try:
            nota = float(nota_str)  # Try to convert input to a number
            notas.append(nota)      # Add the nota to the list
        except ValueError:
            print("Please enter a valid number.")
    
    if notas:
        promedio = sum(notas) / len(notas)  # Calculate the average
        print(f"Las notas ingresadas son: {notas}")
        print(f"El promedio es: {promedio:.2f}")
        if promedio >= 0 and promedio <= 2.99:
            print("Nota Baja")
        elif promedio >= 3 and promedio <= 3.99:
            print("Nota Media")
        elif promedio >= 4 and promedio <= 5:
            print(f"¡Felicidades! Obtuviste Una Nota Alta")
            print("Adicionalmente te has ganado un 20% de descuento de la matricula")
            precio_matricula = float(input("Ingresa el valor de la matricula: "))
            total = float(precio_matricula - (precio_matricula * 0.2))
            print(f"El precio de la matricula es {total}")
    else:
        print("Programa terminado.")


if __name__ == "__main__":
    main()