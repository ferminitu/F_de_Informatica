from aves import Golondrina
from aves import Gorrion

class Ornitologo:
    def __init__(self):
        self.aves = []

    def estudiarAve(self, ave):
        if ave not in self.aves:
            self.aves.append(ave)
    
    def avesEnEstudio(self):
        print(self.aves)
    
    def realizarRutinaSobreAves(self):
        for i in self.aves:
            i.comer(80)
            i.volar(70)
            i.comer(10)

    def avesEnEquilibrio(self):
        for i in self.aves:
            print(i)
            return i.equilibrio()

from Ejercicio3 import Ornitologo

eugenio = Ornitologo()
alma = Golondrina(200)
maria = Golondrina(50)
juan = Gorrion(20, 50)
pedro = Gorrion(30, 80)
print(pedro.vuelos)
print(pedro.comidas)
print(maria.energia)

eugenio.estudiarAve(juan)
eugenio.estudiarAve(pedro)
eugenio.estudiarAve(maria)
print(eugenio.avesEnEstudio())
eugenio.realizarRutinaSobreAves()
print(eugenio.avesEnEquilibrio())

print(pedro.vuelos)
print(pedro.comidas)
print(maria.energia)