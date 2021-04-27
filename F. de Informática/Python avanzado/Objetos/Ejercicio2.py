#Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar
#si al hacerlo la energía toma el valor 0 o valor negativo.

class Golondrina:
  def _init_(self, energia): #constructor, define el estado inicial del objeto, atributos.
    self.energia = energia
                                    #Esto se denomina metodo, no es una funcion
  def comer_alpiste(self, gramos):  #que hace
    self.energia += 4 * gramos      #como lo hace

  def volar_en_circulos(self): 
    self.volar(0)

  def volar(self, kms):
    if self.energia > 10 + kms:
      self.energia -= 10 + kms
    else:
      print("No tengo energia suficiente, necesito comer alpiste")
