from aves import *

class EntrenadorDeAves:
    def __init__(self, vacantes):
        self.vacantes = vacantes
        self.alumnos_aceptados = []
    
    def aceptar(self, alumno):
        if self.vacantes > 0:
            self.alumnos_aceptados.append(alumno)
            self.vacantes -= 1
    
    def entrenar(self):
        for alumno in self.alumnos_aceptados:
            for _ in range(0,20):
                alumno.volar_en_circulos()
            alumno.saciar()

hipo = EntrenadorDeAves(10)