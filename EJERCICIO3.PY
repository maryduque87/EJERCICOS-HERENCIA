class Vehiculos:
  def __init__(self, marca, año):
    self.marca=marca
    self.año=año

class Coche(Vehiculos):
  def __init__(self, marca, año, modelo):
    super().__init__(marca, año)
    self.modelo=modelo
  
toyota=Coche("Toyota", 2022, "Corolla")
print(toyota.marca)
print(toyota.año)
print(toyota.modelo)
