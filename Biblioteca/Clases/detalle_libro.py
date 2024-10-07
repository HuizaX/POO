import Libro
import editorial
class detalle_libro(Libro,editorial):
    
    def __init__(self,categorias,nro_paginas,editorial,ejemplares_disponibles,cantidad_ejemplares):#encapsulamiento
        self.categorias = categorias
        self.nro_paginas = nro_paginas
        self.editorial = editorial
        self.ejemplares_disponibles = ejemplares_disponibles
        self.cantidad_ejemplares = cantidad_ejemplares

