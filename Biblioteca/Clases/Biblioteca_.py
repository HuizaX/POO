import Libro
class biblioteca():#objeto
    def __init__(self,nombre,direccion,telefono):#encapsuamiento
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    def buscar_libro(self):#polimorfismo
        pass
    def prestar_libro(self):
        pass
    def devolver_libro(self):
        pass