import math

class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    area = math.pi * self.radio**2
    return area

  def calcular_perimetro(self):
    perimetro = 2 * math.pi * self.radio
    return perimetro
  
class Rectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    area = self.base * self.altura
    return area