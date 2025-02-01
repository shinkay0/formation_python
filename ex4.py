class Vehicule:
  def __init__(self, color, price):
    self.color = color
    self.price = price

  def afficher(self):
    print(f"Le véhicule est de couleur {self.color} et coûte {self.price} euros.")

class Voiture(Vehicule):
  def __init__(self, color, price, roues):
    super().__init__(color, price)
    self.roues = roues

class Camion(Vehicule):
  def __init__(self, color, price, roues):
    super().__init__(color, price)
    self.roues = roues


v1 = Voiture("rouge", 20000, 2)
v1.afficher()