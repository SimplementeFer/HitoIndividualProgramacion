from producto import  Producto
from cliente import Cliente
class Pedido:
    # propiedades / atributos / campus / adjetivos calificativos
    def __init__(self, IdPedido, FechaPedido, NombreCliente, NombreProducto, Cantidad, ImporteTotal):  # constructor
        self.IdPedido = IdPedido
        self.FechaPedido = FechaPedido
        self.IdCliente = NombreCliente
        self.IdProducto = NombreProducto
        self.Cantidad = Cantidad
        self.ImporteTotal = ImporteTotal

    def mostrarPedido(self):
            print(f'PEDIDO-> El día {self.FechaPedido} el cliente {self.IdCliente} solicita {self.Cantidad} unidades del producto {self.IdProducto} y le cuesta {self.ImporteTotal} en total')


cliente1=Cliente(1, 'Juanjo', 'Sanchez', '52367746U', 34, 'Español', 'Humanes', 28970, 674026722, 'juanjo@gmail.com', 1500)
cliente2=Cliente (2, 'Fernando', 'Dorado', '12345678D', 19, 'Español', 'Griñon', 12345, 616554477, 'fernando.dorado@campuspf.es', 4000)

producto1=Producto(1, 'Batata', 'tubérculo', 2.20, 190, True)
producto2=Producto(2, 'Zanahoria', 'tubérculo', 0.90, 320, True)
producto3=Producto(3, 'Patata', 'tubérculo', 1.20, 590, True)

pedido1=Pedido(1,'11/05/2022',cliente1.Nombre,producto2.Nombre,50, producto2.Precio*50) #tablas relacionadas

pedido1.mostrarPedido()




