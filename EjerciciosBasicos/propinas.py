"""
•	Si el servicio fue excelente, la propina debe ser el 20% del total de la cuenta.
•	Si el servicio fue bueno, la propina debe ser el 15% del total de la cuenta.
•	Si el servicio fue regular, la propina debe ser el 10% del total de la cuenta.
•	Para cualquier otra calificación, no se sugiere propina.
Instrucciones:
1.	Solicita al usuario que ingrese el total de la cuenta.
2.	Pide al usuario que califique el servicio como
"excelente", "bueno" o "regular".
3.	Utiliza estructuras condicionales para calcular la propina según
la calidad del servicio.
4.	Muestra la cantidad de propina sugerida.

"""

def mostrar_menu():
    print("Bienvenido al calculador de propinas...")
    print("Seleccione una calificacion para la calidad del servicio")
    print("1. Excelente")
    print("2. Bueno")
    print("3. Regular")

while True:
    mostrar_menu()
    opcion = input("Ingrese el numero correspondiente a la operacion deseada: ")

    if opcion == '1':
        val = float(input("Ingrese el valor de la cuenta: "))
        i = 0.20
        total = val + (val * i)
        print("################################")
        print("################################")
        print("################################")
        print(f"El valor de tu cuenta es: {total}")
        print("################################")
        print("################################")
        print("################################")
    elif opcion == '2':
        val = float(input("Ingrese el valor de la cuenta: "))
        i = 0.20
        total = val + (val * i)
        print("################################")
        print("################################")
        print("################################")
        print(f"El valor de tu cuenta es: {total}")
        print("################################")
        print("################################")
        print("################################")

    elif opcion == '3':
        val = float(input("Ingrese el valor de la cuenta: "))
        i = 0.20
        total = val + (val*i)
        print("################################")
        print("################################")
        print("################################")
        print(f"El valor de tu cuenta es: {total}")
        print("################################")
        print("################################")
        print("################################")