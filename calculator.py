def main():
    print("Select 1 para sumar ")
    print("Select 2 para resta ")
    print("Select 3 para division ")
    print("Select 4 para multiplicacion ")
    election = int(input("Enter election(1-4): "))

    match election:
        case 1:
            num1 = int(input("Numero 1: "))
            num2 = int(input("Numero 2: "))
            suma(num1, num2)
        case 2:
            num1 = int(input("Numero 1: "))
            num2 = int(input("Numero 2: "))
            resta(num1, num2)
        case 3:
            num1 = int(input("Numero 1: "))
            num2 = int(input("Numero 2: "))
            division(num1, num2)
        case 4:
            num1 = int(input("Numero 1: "))
            num2 = int(input("Numero 2: "))
            multiplication(num1, num2)
        case _:
            print("Invalid")



def suma(a, b):
    resultado =  a + b
    print(resultado)

def resta(a, b):
    resultado = a - b
    print(resultado)

def division(a, b):
    resultado = a / b
    print(resultado)

def multiplication(a, b):
    resultado = a * b
    print(resultado)

main()