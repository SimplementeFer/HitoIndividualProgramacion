class Cliente:

    #propiedades / atributos / campus / adjetivos calificativos

    # Datos a introducir en la lista de clientes

    def __init__(self, ID, Nombre, Apellidos, DNI, Edad, Nacionalidad, Domicilio, CP, tlf, Email, Presupuesto): #constructor
        self.ID = ID
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.DNI = DNI
        self.Edad = Edad
        self.Nacionalidad = Nacionalidad
        self.Domicilio = Domicilio
        self.CP = CP
        self.tlf = tlf
        self.Email = Email
        self.Presupuesto = Presupuesto

    def CrearCliente(self):

        list_cliente=[self.ID, self.Nombre, self.Apellidos, self.DNI, self.Edad, self.Nacionalidad, self.Domicilio, self.CP, self.tlf, self.Email, self.Presupuesto]
        lista_clientes.append(list_cliente)

    def mostrarCliente(self):
        print(f'ALUMNO {self.ID} -> Nombre:{self.Nombre}     Apellidos:{self.Apellidos}     DNI:{self.DNI}     Edad:{self.Edad}     Nacionalidad:{self.Nacionalidad}     Domicilio:{self.Domicilio}     CP:{self.CP}     NºTeléfono:{self.tlf}     Correo:{self.Email}     Presupuesto:{self.Presupuesto}')


cliente1=Cliente(1, 'Juanjo', 'Sanchez', '52367746U', 34, 'Español', 'Humanes', 28970, 674026722, 'juanjo@gmail.com', 1500)
cliente2=Cliente (2, 'Fernando', 'Dorado', '12345678D', 19, 'Español', 'Griñon', 12345, 616554477, 'fernando.dorado@campuspf.es', 4000)

cliente1.mostrarCliente()
#cliente2.mostrarCliente()