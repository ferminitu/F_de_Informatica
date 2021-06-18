class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#Interfaz, es el conjunto de mensajes de la clase Perro. [energia(), comer(), acariciar(), estaDebil()]
#Estado, es el conjunto de atributos del objeto. [_alimento, _caricias]