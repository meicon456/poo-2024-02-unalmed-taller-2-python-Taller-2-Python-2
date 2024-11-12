class Motor:
  def __init__(self,numeroCilindros, tipo, registro):
    self.numCilindros = numeroCilindros
    self.tipo = tipo
    self.registro = registro
  def cambiarRegistro(self, registro):
      self.registro = registro
  def asignarTipo(self, tipo):
      if tipo == "gasolina" or tipo == "electrico":
        self.tipo = tipo
        
class Asiento:
  def __init__(self, color, precio, registro):
    self.color = color 
    self.precio = precio
    self.registro = registro
  def cambiarColor(self, color):
      if color == "rojo" or color == "amarillo" or color == "verde" or color == "negro" or color == "blanco":
        self.color = color
      
class Auto:
  cantidadCreados=0
  def __init__(self, marca, modelo, precio,asientos,motor,registro):
    self.modelo = modelo
    self.precio = precio
    self.asientos = asientos if isinstance(asientos, list) else [] 
    self.marca = marca
    self.motor = motor
    self.registro = registro
    Auto.cantidadCreados += 1
  def cantidadAsientos(self):
    return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))
  def verificarIntegridad(self):
    if self.motor.registro != self.registro:
        return "Las piezas no son originales"

    registro_asiento = None
    for asiento in self.asientos:
      if asiento is not None:
        if asiento.registro != self.registro:
          return "Las piezas no son originales"
        if registro_asiento is None:
          registro_asiento = asiento.registro
        elif asiento.registro != registro_asiento:
          return "Las piezas no son originales"
    return "Auto original"
