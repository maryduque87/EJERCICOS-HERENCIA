class Animal:
  def __init__(self, nombre, especie):
    self.nombre=nombre
    self.especie=especie

class Perro(Animal):
  def __init__(self, nombre, especie, raza):
    super().__init__(nombre, especie)
    self.raza=raza
    
joey=Perro("Joey", "Canino", "Poodle")
print(joey.nombre)
print(joey.especie)
print(joey.raza)
