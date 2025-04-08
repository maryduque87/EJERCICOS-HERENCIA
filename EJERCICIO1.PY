class Persona:
  def __init__(self, nombre, edad):
    self.nombre=nombre
    self.edad=edad

class Estudiante(Persona):
  def __init__(self, nombre, edad, grado):
    super().__init__(nombre, edad)
    self.grado=grado
    
maria=Estudiante("Maria", 18, "3ro")
print(maria.nombre)
print(maria.edad)
print(maria.grado)
