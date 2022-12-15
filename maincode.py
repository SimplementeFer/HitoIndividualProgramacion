
# 3 principales listas

lista_clientes = [
        [1, 'Juanjo', 'Sanchez', '52367746U', 34, 'Español', 'Humanes', 28970, 674026722, 'juanjo@gmail.com', 200],
        [2, 'Fernando', 'Dorado', '12345678D', 19, 'Español', 'Griñon', 28971, 616554477, 'fernando.dorado@campuspf.es',40],
        [3, 'Vladislav', 'Slavev', 'No', 19, 'Búlgaro', 'Cubas', 28978, 678996822, 'vladislav.slavev@campusfp.es', 60 ]
                    ]

lista_productos = [
    [1, 'Batata', 'tubérculo', 2.20, 190, True],
    [2, 'Zanahoria', 'tubérculo', 3.90, 320, True],
    [3, 'Patata', 'tubérculo', 2.20, 590, True],
    [4, 'Lentejas', 'legumbre', 4.30, 20, True],
    [5, 'Limon', 'fruta', 3.75, 0, False]
                    ]
lista_pedidos = [
    [1,'11/05/2022', lista_clientes[0][1], lista_productos[1][1], 50, lista_productos[1][3]*50],
    [2, '12/05/2022', lista_clientes[1][1], lista_productos[2][1], 10, lista_productos[2][3] * 10]
]


# Datos a introducir en la lista de clientes

def CrearCliente(ID, Nombre, Apellidos, DNI, Edad, Nacionalidad, Domicilio, CP, tlf, Email, Presupuesto):
    return [int(ID), Nombre, Apellidos, DNI, int(Edad), Nacionalidad, Domicilio, int(CP), int(tlf), Email,
            float(Presupuesto)]


# Datos a introducir en la lista de productos

def Crear_productos(ID, Nombre, Tipo, Precio, Cantidad, Disponibilidad):
    if Cantidad == 0:
        Disponibilidad = False
    else:
        Disponibilidad = True
    return [int(ID), Nombre, Tipo, float(Precio), float(Cantidad), bool(Disponibilidad)]

#Datos a introducir en la lista de pedidos

def Crear_pedidos(IdPedido, FechaPedido, NombreCliente, NombreProducto, Cantidad, ImporteTotal):
    return [int(IdPedido),FechaPedido, NombreCliente, NombreProducto, Cantidad, ImporteTotal]


#Bucle while
i = True

while i == True:

    print(        '                                                               _____________________________________________________________________')
    print(        '\n                                                               | 1. Introducir la secuencia de datos correspondiente a un cliente  |')
    print(        '\n                                                               | 2. Mostrar los clientes recogidos en la base de datos             |')
    print(        '\n                                                               | 3. Introducir la secuencia de datos correspondiente a un producto |')
    print(        '\n                                                               | 4. Mostrar los productos recogidos en la base de datos            |')
    print(        '\n                                                               | 5. Introducir la secuencia de datos correspondiente a un pedido   |')
    print(        '\n                                                               | 6. Mostrar los pedidos existentes en la base de datos             |')
    print(        '\n                                                               | 7. Procesar un pedido                                             |')
    print(        '\n                                                               |              Pulsa cualquier otro numero para salir               |')
    print(        '                                                               _____________________________________________________________________')

    opc = input('\n\n¿Qué quieres hacer? (elige una opción): ')
    iopc = int(opc)

    if iopc == 1:

        # Ciclo de 11 vueltas para clientes
        print(
            "\nPara los clientes necesitamos 1.ID 2.Nombre 3.Apellidos 4.DNI 5.Edad 6.Nacionalidad 7.Domicilio 8.Código Postal 9.Nº de tlf 10.Email y 11.Presupuesto\n")
        contador = 0
        prepforcliente = ['ID', 'Nombre', 'Apellidos', 'DNI', 'Edad', 'Nacionalidad', 'Domicilio', 'CP', 'TLF', 'Email',
                          'Presupuesto']
        tmpclientes = []
        for cliente in range(11):
            contador += 1
            if (contador == 1 or contador == 5 or contador == 8 or contador == 9):
                valor = (int(input(f"Introduce el campo {prepforcliente[contador - 1]}: ")))
                tmpclientes.append(valor)
            elif contador == 11:
                valor = (float(input(f"Introduce el campo {prepforcliente[contador - 1]}: ")))
                tmpclientes.append(valor)
            else:
                valor = (input(f"Introduce el campo {prepforcliente[contador - 1]}: "))
                tmpclientes.append(valor)
        lista_clientes.append(tmpclientes)
    elif iopc == 2:

        for cliente in lista_clientes:
            print(cliente)

        opc = input('Enter para continuar: ')

    elif iopc == 4:

        for producto in lista_productos:
            print(producto)

        opc = input('Enter para continuar: ')

    elif iopc == 3:

        # Ciclo de 6 vueltas para producto
        print("------Para los productos necesitamos 1.ID, 2.Nombre, 3.Tipo, 4.Precio y 5.Cantidad------")
        contador = 0
        prepforproducto = ['ID', 'Nombre', 'Tipo', 'Precio', 'Cantidad', 'Disponibilidad']
        tmpproductos = []
        for producto in range(5):
            contador += 1
            if (contador == 1):
                valor = (int(input(f"Introduce el campo {prepforproducto[contador - 1]}: ")))
                tmpproductos.append(valor)
            elif contador == 4:
                valor = (float(input(f"Introduce el campo {prepforproducto[contador - 1]}: ")))
                tmpproductos.append(valor)
            elif contador == 5:
                valor = (int(input(f"Introduce el campo {prepforproducto[contador - 1]}: ")))
                if (valor == 0):
                    tmpproductos.append(valor)

                    tmpproductos.append(False)

                else:
                    tmpproductos.append(valor)

                    tmpproductos.append(True)


            else:
                valor = (input(f"Introduce el campo {prepforproducto[contador - 1]}: "))
                tmpproductos.append(valor)
        lista_productos.append(tmpproductos)
        opc = input('Enter para continuar: ')
    elif iopc == 6:
        print('Aquí se muestra el registro de todos los pedidos')
        for pedido in lista_pedidos:
            print(f'\n{pedido}\n')
        opc = input('Enter para continuar: ')

    elif iopc == 5:
        # Ciclo de 6 vueltas para producto
        print("------Para los pedidos necesitamos 1.ID, 2.Fecha, 3.Nombre del cliente, 4.Nombre del producto, 5.Cantidad y 6.Precio del producto (para calcular el importe sin iva)------")
        contador = 0
        prepforpedido = ['ID', 'Fecha', 'Nombre del cliente', 'Nombre del producto', 'Cantidad', 'Precio del producto']
        tmppedidos = []
        for pedido in range(5):
            contador += 1
            if (contador == 1):
                valor = (int(input(f"Introduce el campo {prepforpedido[contador - 1]}: ")))
                tmppedidos.append(valor)
            elif contador == 5:
                valor = (int(input(f"Introduce el campo {prepforpedido[contador - 1]}: ")))
                tmppedidos.append(valor)
                valor2 = (float(input(f"Introduce el campo {prepforpedido[contador]}: ")))
                tmppedidos.append(valor*valor2)
            else:
                valor = (input(f"Introduce el campo {prepforpedido[contador - 1]}: "))
                tmppedidos.append(valor)
        lista_pedidos.append(tmppedidos)
        opc = input('Enter para continuar: ')

    elif iopc == 7:
        print("-----------¿Qué pedido quieres procesar?-----------")
        for pedido in lista_pedidos:
            print(f'\n{pedido}\n')
        opc=input(f'Escoge el pedido escribiendo el ID:')

        iopc = int(opc)
        if iopc == 1:
            if 'Español' in lista_clientes [0] :
                lista_pedidos[0][5]=lista_pedidos[0][5]*1.21
                print('Esto es el pago que debe hacer el cliente con el impuesto sobre el valor adquirido ya aplicado:')
                print(f'{lista_pedidos[0][5]}')
                opc = input('Enter para continuar: ')
                resultado1 = lista_clientes[0][10] - lista_pedidos[0][5]
                if resultado1 >= 0 :
                    lista_clientes[0][10] = lista_clientes[0][10] - lista_pedidos[0][5]
                    print('****Se han aplicado cambios en los datos que hay almacenados**** \n\n\n Esto es el saldo que le queda al cliente después de hacer el pedido:')

                    print(f'{lista_clientes[0][10]}')
                    opc = input('Enter para continuar: ')
                else:
                    print(f'El cliente {lista_pedidos[0][2]} no puede realizar su pedido porque no tiene saldo')
                    opc = input('Enter para continuar: ')


            else:
                print('No se suma iva')
                print('Esto es el saldo que le queda al cliente después de hacer el pedido:')
                lista_clientes[0][10] = lista_clientes[0][10] - lista_pedidos[0][5]
                print(f'{lista_clientes[0][10]}')
                opc = input('Enter para continuar: ')
        elif iopc == 2:
            if 'Español' in lista_clientes[1]:
                lista_pedidos[1][5] = lista_pedidos[1][5] * 1.21
                print('Esto es el pago que debe hacer el cliente con el impuesto sobre el valor adquirido ya aplicado:')
                print(f'{lista_pedidos[1][5]}')
                opc = input('Enter para continuar: ')
                resultado2 = lista_clientes[1][10] - lista_pedidos[1][5]
                if resultado2 >= 0:
                    lista_clientes[1][10] = lista_clientes[1][10] - lista_pedidos[1][5]
                    print(
                        '****Se han aplicado cambios en los datos que hay almacenados**** \n\n\n Esto es el saldo que le queda al cliente después de hacer el pedido:')

                    print(f'{lista_clientes[1][10]}')
                    opc = input('Enter para continuar: ')
                else:
                    print(f'El cliente {lista_pedidos[1][2]} no puede realizar su pedido porque no tiene saldo')
                    opc = input('Enter para continuar: ')
            else:
                print('No se suma iva')
                print('Esto es el saldo que le queda al cliente después de hacer el pedido:')
                lista_clientes[1][10] = lista_clientes[1][10] - lista_pedidos[1][5]
                print(f'{lista_clientes[1][10]}')
                opc = input('Enter para continuar: ')
        elif iopc == 3:
            if 'Español' in lista_clientes[2]:
                lista_pedidos[2][5] = lista_pedidos[2][5] * 1.21
                print('Esto es el pago que debe hacer el cliente con el impuesto sobre el valor adquirido ya aplicado:')
                print(f'{lista_pedidos[2][5]}')
                opc = input('Enter para continuar: ')
                resultado2 = lista_clientes[2][10] - lista_pedidos[2][5]
                if resultado2 >= 0:
                    lista_clientes[2][10] = lista_clientes[2][10] - lista_pedidos[2][5]
                    print(
                        '****Se han aplicado cambios en los datos que hay almacenados**** \n\n\n Esto es el saldo que le queda al cliente después de hacer el pedido:')

                    print(f'{lista_clientes[2][10]}')
                    opc = input('Enter para continuar: ')
                else:
                    print(f'El cliente {lista_pedidos[2][2]} no puede realizar su pedido porque no tiene saldo')
                    opc = input('Enter para continuar: ')
            else:
                print('No se suma iva')
                print('Esto es el saldo que le queda al cliente después de hacer el pedido:')
                lista_clientes[2][10] = lista_clientes[2][10] - lista_pedidos[2][5]
                print(f'{lista_clientes[2][10]}')
                opc = input('Enter para continuar: ')
        elif iopc == 4:
            if 'Español' in lista_clientes[3]:
                lista_pedidos[3][5] = lista_pedidos[3][5] * 1.21
                print('Esto es el pago que debe hacer el cliente con el impuesto sobre el valor adquirido ya aplicado:')
                print(f'{lista_pedidos[3][5]}')
                opc = input('Enter para continuar: ')
                resultado2 = lista_clientes[3][10] - lista_pedidos[3][5]
                if resultado2 >= 0:
                    lista_clientes[3][10] = lista_clientes[3][10] - lista_pedidos[3][5]
                    print(
                        '****Se han aplicado cambios en los datos que hay almacenados**** \n\n\n Esto es el saldo que le queda al cliente después de hacer el pedido:')

                    print(f'{lista_clientes[3][10]}')
                    opc = input('Enter para continuar: ')
                else:
                    print(f'El cliente {lista_pedidos[3][2]} no puede realizar su pedido porque no tiene saldo')
                    opc = input('Enter para continuar: ')
            else:
                print('No se suma iva')
                print('Esto es el saldo que le queda al cliente después de hacer el pedido:')
                lista_clientes[3][10] = lista_clientes[3][10] - lista_pedidos[3][5]
                print(f'{lista_clientes[3][10]}')
                opc = input('Enter para continuar: ')
        else:
            print('')

    elif opc == " ":

        print("--------------PROCESO FINALIZADO--------------")


    else:
        i = False


