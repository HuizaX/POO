class libro():#objeto
    def __init__(self,isbn,titulo,autor,nro_copias):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.nro_copias = nro_copias

class historieta (libro):#herencia
    pass