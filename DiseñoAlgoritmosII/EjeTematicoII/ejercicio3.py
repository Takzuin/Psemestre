lista_frutas = ['Avocado', 'Apple', 'Manzana']



def fitrar_palabras(lista):
    letra = input("Introduce la letra con la que deben comenzar las palabras: ").strip().lower()
    nueva_lista = []
    for i in lista:
        if i.startswith(letra):
            nueva_lista.append(i)
    print(nueva_lista)

fitrar_palabras(lista_frutas)