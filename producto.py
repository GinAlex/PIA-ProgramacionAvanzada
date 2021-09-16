class Producto:
    def __init__(self, precio, upc, nombre, cantidad):
        self.precio = precio
        self.upc = upc
        self.nombre = nombre
        self.cantidad = cantidad

    def aplicarDescuento(self):
        print('metodo no implementado')
    def comprar(self,cantidad):
        self.cantidad=self.cantidad+cantidad
    def vender(self,cantidad):
        if cantidad>self.cantidad:
            raise Exception("no existe suficiente producto")
        self.cantidad=self.cantidad-cantidad


class Comida(Producto):
    def __init__(self, precio, upc, nombre, fechacad,cantidad):
        super().__init__(precio, upc,nombre,cantidad)
        self.fechacad = fechacad
    
class Ropa(Producto):
    def __init__(self, precio, upc, nombre, talla,cantidad):
        super().__init__(precio, upc,nombre,cantidad)
        self.talla = talla

class Electronicos(Producto):
    def __init__(self, precio, upc, nombre, modelo,cantidad):
        super().__init__(precio, upc,nombre,cantidad)
        self.modelo = modelo

class Entretenimiento(Producto):
    def __init__(self, precio, upc, nombre, anoprod,cantidad):
        super().__init__(precio, upc,nombre,cantidad)
        self.anoprod = anoprod