mes = input('Que mes?: ')
if mes in {"diciembre", "enero", "febrero"}:
    print('Estas en invierno')
elif mes in {"marzo", "abril", "mayo"}:
    print('Estas en primavera')
elif mes in {"junio", "julio", "agosto"}:
    print('Estas en verano')
elif mes in {"septiembre", "octubre", "noviembre"}:
    print('Estas en otoño')
else:
    print('Dato equivocado')
