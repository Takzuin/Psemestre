"""Ejercicio 1: Sistema de Transporte Público

Descripción: Diseña un sistema de transporte público que calcule la tarifa para diferentes tipos de vehículos. 
Implementa las clases Autobus, Metro y Taxi, cada una con su propio método calcular_tarifa(). 
Cada método debe calcular la tarifa enfunción de diferentes criterios, como la distancia recorrida, 
el tiempo de viaje o la tarifa base.

Requisitos:

· Implementar las clases Autobus, Metro y Taxi.

· Cada clase debe tener un método calcular_tarifa() que devuelva el costo del viaje.

· Utilizar polimorfismo de instancia para que la función calcular_tarifa() se comporte de manera diferente según el 
tipo de vehículo.

· Considerar diferentes criterios para calcular la tarifa, como la distancia recorrida, el tiempo de viaje o 
la tarifa base.

· Validar las entradas de los métodos para garantizar la seguridad y consistencia de las operaciones. """

class Vehiculo:
    def __init__(self, tarifa, distancia_recorrida):
        self.tarifa = tarifa
        self.distancia_recorrida = distancia_recorrida

    def calcular_tarifa(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Usa super().__init__ en las subclases:
# Esto permite que las subclases aprovechen el constructor de la clase base y reduces redundancia.
class Autobus(Vehiculo):
    def __init__(self, tarifa, distancia_recorrida):
        super().__init__(tarifa, distancia_recorrida)
        self.tarifa = tarifa
        self.distancia_recorrida = distancia_recorrida

    
    def calcular_tarifa(self):
        precio_total = self.tarifa * self.distancia_recorrida
        return precio_total

class Metro(Vehiculo):
    def __init__(self, tarifa, distancia_recorrida):
        super().__init__(tarifa, distancia_recorrida)
        self.tarifa = tarifa
        self.distancia_recorrida = distancia_recorrida

    def calcular_tarifa(self):
        precio_total = self.tarifa * self.distancia_recorrida
        return precio_total

class Taxi(Vehiculo):
    def __init__(self, tarifa, distancia_recorrida):
        self.tarifa = tarifa
        self.distancia_recorrida = distancia_recorrida
    
    
    def calcular_tarifa(self):
        precio_total = self.tarifa * self.distancia_recorrida
        return precio_total

def main():
    vehiculos = [
        Autobus(2, 10),
        Metro(1.5, 5),
        Taxi(3, 8)
    ]
    for vehiculo in vehiculos:
        print(f"Tarifa {type(vehiculo).__name__}: {vehiculo.calcular_tarifa()}")


if __name__ == '__main__':
    main()

