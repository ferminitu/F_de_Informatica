# Ejercicio 4
# Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, 
# y de estos dos medios de transporte sabemos que:

# comienzan con una cantidad que podemos establecer de combustible

# los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible
#  por cada kilómetro recorrido

# las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

# pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

# saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al 
# máximo que pueden llevar.

# Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

class Vehiculos:
    def cargar_nafta(self, litros):
        self.combustible += litros
    
    def hay_espacio(self, cant_personas):
        return cant_personas <= self.lugares

class Moto(Vehiculos):
    def __init__(self, combustible = 0):
        self.combustible = combustible
        self.lugares = 2

    def andar(self, distancia):
        self.combustible -= distancia


class Auto(Vehiculos):
    def __init__(self, combustible = 0):
        self.combustible = combustible
        self.lugares = 5

    def andar(self, distancia):
        self.combustible -= distancia/2