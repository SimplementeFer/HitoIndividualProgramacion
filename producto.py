class Producto:

    #propiedades / atributos / campus / adjetivos calificativos
    def __init__(self, ID, Nombre, Tipo, Precio, Cantidad, Disponibilidad): #constructor
        self.ID = ID
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Precio = Precio
        self.Cantidad = Cantidad
        self. Disponibilidad = Disponibilidad

    def CrearProducto(self):
        list_producto = [self.ID, self.Nombre, self.Tipo, self.Precio, self.Cantidad, self.Disponibilidad]
        lista_productos.append(list_producto)
    def mostrarProducto(self):
        print(f'Producto {self.ID} -> Nombre:{self.Nombre}     Tipo: {self.Tipo}     Precio: {self.Precio}     Cantidad: {self.Cantidad}     Disponibilidad: {self.Disponibilidad}')

producto1=Producto(1, 'Batata', 'tubérculo', 2.20, 190, True)
producto2=Producto(2, 'Zanahoria', 'tubérculo', 0.90, 320, True)
producto3=Producto(3, 'Patata', 'tubérculo', 1.20, 590, True)

producto1.mostrarProducto()
#producto2.mostrarProducto()
#producto3.mostrarProducto()