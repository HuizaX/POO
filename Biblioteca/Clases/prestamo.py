import detalle_libro
import Usuario


class prestamo():
    def __init__(self,isbn,nro_ident,fecha_prestamo,fecha_entrega,fecha_devolucion):
        self.isbn = isbn
        self.nro_ident = nro_ident
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
