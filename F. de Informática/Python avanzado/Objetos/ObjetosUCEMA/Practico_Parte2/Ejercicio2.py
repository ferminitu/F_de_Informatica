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

    def esta_en_equilibrio(self):
        return self.energia > 150 and self.energia < 300

pepita = Golondrina(100)
anastasia = Golondrina(200)