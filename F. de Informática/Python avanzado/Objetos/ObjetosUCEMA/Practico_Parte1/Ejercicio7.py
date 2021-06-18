# Ejercicio 7
# Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas
# como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico”
# y “veces”). 
# El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que
# se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. 
# El CSSV es la misma división pero considerando solamente lo que voló la vez que más
# voló y lo que comió la vez que más comió. 
# El CSSP es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, 
# los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

class Gorrion:
    def __init__(self, kms=0, gramos=0):
        self.comidas = []
        self.vuelos = []
        self.kms = kms
        self.gramos = gramos

    def volar(self, longitud):
        self.vuelos.append(longitud)
        self.kms += longitud
    
    def comer(self, ingerido):
        self.comidas.append(ingerido)
        self.gramos += ingerido
    
    def CSS(self):
        return self.kms/self.gramos
    
    def CSSV(self):
        return (int(max(self.vuelos)) / int(max(self.comidas)))
    
    def CSSP(self):
        if self.gramos <= 0:
            return None
        else:
            return (int(max(self.vuelos)) / int(max(self.comidas)))
    
    def equilibrio(self):
        return 2 < self.CSS() > 0.5
    

from Ejercicio7 import Gorrion

pedro = Gorrion()
pedro.comer(100)
pedro.comer(200)
pedro.comer(300)
pedro.volar(10)
pedro.volar(20)
pedro.volar(30)
pedro.CSS()
pedro.CSSV()
pedro.CSSP()
print(pedro.equilibrio())