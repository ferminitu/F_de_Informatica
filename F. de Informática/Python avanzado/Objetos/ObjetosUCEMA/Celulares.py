class Dispositivo:
    def cargar_a_tope(self):
        self.bateria = 100

    def descargado(self, bateria):
        self.bateria <= 20


class Celular(Dispositivo):
    def __init__(self):
        self.bateria = 100

    def utilizar(self, min):
        self.bateria -= min/2


class Notebook(Dispositivo):
    def __init__(self):
        self.bateria = 100

    def utilizar(self, min):
        self.bateria -= min


class CargadorNocturno:
    def __init__(self):
        self.dispositivos = []

    def agregar(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def cargar(self):
        for i in self.dispositivos:
            i.cargar_a_tope()


