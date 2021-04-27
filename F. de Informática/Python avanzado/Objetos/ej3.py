# Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método
# que le aplique un descuento al precio, el cual tiene que recibir un número entero
# (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se
# aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, numero):
        self.precio *= 1 - numero/100

mac = Notebook('Apple', 'Air', 1000)