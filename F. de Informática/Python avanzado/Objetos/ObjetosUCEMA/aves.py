class Ave:
  def esta_feliz(self):
    return self.energia >= 500 # hacemos esto ya que este def
                               # afecta a dragones y golodrinas
  
  def arranca_en(self, ciudad):
    self.ciudad_actual = ciudad

  def volar_por_panamericana(self, ciudad_destino):
    kms = abs(self.ciudad_actual - ciudad_destino)
    self.volar(kms)
    self.ciudad_actual = ciudad_destino

ushuaia == ciudad(0)
buenos_aires == ciudad(3078)
valparaiso == ciudad(4533)
bahía_prudhoe == ciudad(17958)

class Golondrina(Ave): # a quien afecta (hereda de Ave)
  def __init__(self, energia): 
    self.energia = energia 

  def comer_alpiste(self, gramos): # que, y es un METODO, NO una funcion
    self.energia += 4 * gramos # como

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia <= 10

  def saciar(self):
    self.comer_alpiste(100)


class Dragon(Ave):  # () = hereda de Ave
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def saciar(self):
    self.comer_peces(3)

  def esta_debil(self):
    return self.energia <= 10

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
maria = Golondrina(42)
chimuelo = Dragon(200, 1000)


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