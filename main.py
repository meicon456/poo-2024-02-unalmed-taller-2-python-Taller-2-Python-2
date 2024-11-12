class Motor:
  def __init__(self,numeroCilindros: int, tipo: str, registro: int):
    self.numCilindros = numeroCilindros
    self.tipo = tipo
    self.registro = registro
  def cambiarRegistro(self, registro:int):
      self.registro = registro
  def asignarTipo(self, tipo: str):
      if tipo == "gasolina" or tipo == "electrico":
        self.tipo = tipo
        
class Asiento:
  def __init__(self, color: str, precio: float, registro: int)->None:
    self.color = color 
    self.precio = precio
    self.registro = registro
  def cambiarColor(self, color: str):
      if color == "rojo" or color == "amarillo" or color == "verde" or color == "negro" or color == "blanco":
        self.color = color
      
class Auto:
  cantidadCreados=0
  def __init__(self, marca:  str, modelo: str, precio: float,asientos: list[Asiento],motor: Motor,registro: int):
    self.modelo = modelo
    self.precio = precio
    self.asientos = [asiento for asiento in asientos if isinstance(asiento, Asiento)] 
    self.marca = marca
    self.motor = motor
    self.registro = registro
    Auto.cantidadCreados += 1
  def cantidadAsientos(self):
    return len([asiento for asiento in asientos if isinstance(asiento, Asiento)])
  def verificarIntegridad(self)-> bool:
    if self.motor.registro != self.registro:
        return "Las piezas no son originales"
    
    for asiento in self.asientos:
        if asiento.registro != self.registro:
            return "Las piezas no son originales"
    return "Auto original"
