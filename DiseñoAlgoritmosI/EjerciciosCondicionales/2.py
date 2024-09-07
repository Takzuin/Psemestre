#Comprueba si 'a' es mayor que 'b' o si 'c' es igual a 'd', pero no ambas condiciones:
a, b, c, d = 7, 5, 3, 3
if a >= b:
    print('A es mayor que B')
    if c == d:
        print('C es igual a D')
    else:
        print('C no es igual a D')
else:
    print('A no es mayor que B')