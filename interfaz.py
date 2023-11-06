import os
print("BIENVENIDO A HORMIGONERA -> JAMA <- ")
#region Funciones
def datos_cliente():
'''
Le pide los datos al usuario
'''
    print("Introduzca sus datos!!")
    nombre = str(input("Nombre y Apellido: "))
    nombre_cliente = nombre.title()
    while True:                                                                             
        telefono_cliente = input("Telefono de Contacto: ")
        if telefono_cliente.isdigit():
            break
        else:
            print("Numero ingresado no valido... intente nuevamente.")    
    mail_cliente = str(input("Email de Contacto: "))
    datos_cliente = ["Nombre:", nombre_cliente, "Tel:", telefono_cliente, "Email:", mail_cliente]
    return datos_cliente
def seleccion_tipo_cliente():
'''
Selecciona el tipo de cliente (Monotributista, Responsable Inscripto, etc)
'''
    categoria_de_clientes = ["Monotributista","Responsable Inscripto","Consumidor Final"]
    factura = ["C","A","C"]
    while True:
        try:
            cat_cliente = int(input("seleccione el tipo de cliente: \n 1. monotributista \n 2. responsable inscripto \n 3. consumidor final \n Elija (1/2/3): "))
            if cat_cliente >=1 and cat_cliente <=3:
                tipo_cliente = categoria_de_clientes[cat_cliente-1]
                tipo_factura = factura[cat_cliente-1]
                break
            else:
                os.system("cls")
                print("elija 1 para monotributista, 2 para responsable inscripto o 3 para consumidor final.")
        except ValueError:
            os.system("cls")
            print("Seleccione una opcion numerica")
    return tipo_cliente, tipo_factura
def calculo_de_volumen():
'''
Indica la unidad y Calcula el Volumen Requerido de los materiales
'''
    while True:
        try:
            unidad = int(input("Indica unidad de medida [1] Metros - [2] Pies: "))
            if unidad == 1 or unidad == 2:
                break
            else:
                os.system("cls")
                print("Opcion seleccionada no reconocida, por favor vuelva a intentarlo.")
        except ValueError:
            os.system("cls")
            print("Seleccione una opcion numerica")
    while True:
        try:
            ancho = float(input("Ingrese el ancho del terreno: "))
            break
        except ValueError:
            os.system("cls")
            print("Ingrese un valor numerico")
    while True:
        try:
            largo = float(input("Ingrese el largo del terreno: "))
            break
        except ValueError:
            os.system("cls")
            print("Ingrese un valor numerico")
    while True:
        try:
            altura = float(input("Ingrese la altura deseada del hormigon: "))
            if altura < 1:
                print("Altura no valida, la misma debe ser mayor a 1")
            else:
                break
        except ValueError:
            os.system("cls")
            print("Ingrese un valor numerico")
    volumen = ancho * largo * (altura/100)
    return volumen, unidad
def Resistencia(volumen, unidad):
'''
Selecciona y Calcula el tipo de Resistencia requerido
'''
    if unidad == 1:
        while True:
            try:
                print("Tipos de resistencias:","Tipo 1 [105 kg]","Tipo 2 [140 kg]","Tipo 3 [175 kg]","Tipo 4 [210 kg]","Tipo 5 [246 kg]")
                eleccion_de_resistencia = int(input("Seleccione el tipo que desea utilizar: "))
                if eleccion_de_resistencia >=1 and eleccion_de_resistencia <=5:
                    cemento = [210, 260, 300, 350, 420]
                    arena   = [0.5, 0.63, 0.48, 0.56, 0.67]
                    grava   = [1, 0.84, 0.96, 0.84, 0.67]
                    agua    = [160, 170, 170, 180, 220]
                    cant_cemento = ((cemento[eleccion_de_resistencia-1] * volumen) / 50)
                    cant_arena   = arena[eleccion_de_resistencia-1] * volumen
                    cant_grava   = grava[eleccion_de_resistencia-1] * volumen
                    cant_agua    = agua[eleccion_de_resistencia-1] * volumen
                    cant_cemento = round(cant_cemento,2)
                    cant_arena = round(cant_arena,2)
                    cant_grava = round(cant_grava,2)
                    cant_agua = round(cant_agua,2)
                    materiales = [
                        f"Cantidad cemento {cant_cemento} bolsas",
                        f"Cantidad de arena {cant_arena} m3",
                        f"Cantidad de grava {cant_grava} m3",
                        f"Cantidad de agua {cant_agua} Lts"]
                    break
                else:
                    os.system("cls")
                    print("Seleccion no reconocida, por favor intÃ©ntelo nuevamente.")
            except ValueError:
                os.system("cls")
                print("Seleccion no reconocida, por favor intÃ©ntelo nuevamente.")            
    else:
        while True:
            print("Tipos de resistencias:","Tipo 1 [1500 psi]","Tipo 2 [2000 psi]","Tipo 3 [2500 psi]","Tipo 4 [3000 psi]","Tipo 5 [3500 psi]")
            eleccion_de_resistencia = int(input("Seleccione el tipo que desea utilizar: "))
            if eleccion_de_resistencia >=1 and eleccion_de_resistencia <=5:
                cemento = [462.97, 573.20, 661.38, 771.72, 925.42]
                arena   = [1765.73, 2224.82, 1695.10, 1977.62, 2366.08]
                grava   = [3531.47, 2966.43, 3390.21, 2966.43, 2366.08]
                agua    = [42.26, 44.99, 44.99, 47.72, 58.11]
                cant_cemento = ((cemento[eleccion_de_resistencia-1] * volumen)/80)
                cant_arena = arena[eleccion_de_resistencia-1] * volumen
                cant_grava = grava[eleccion_de_resistencia-1] * volumen
                cant_agua = agua[eleccion_de_resistencia-1] * volumen
                cant_cemento = round(cant_cemento,2)
                cant_arena = round(cant_arena,2)
                cant_grava = round(cant_grava,2)
                cant_agua = round(cant_agua,2)
                materiales = [
                    f"Cantidad cemento {cant_cemento} Bolsas",
                    f"Cantidad de arena {cant_arena} p3",
                    f"Cantidad de grava {cant_grava} p3",
                    f"Cantidad de agua {cant_agua} Gl"]
                break
            else:
                os.system("cls")
                print("Seleccion no reconocida, por favor intÃ©ntelo nuevamente.")
    return materiales
#region Archivo
def agregar_cliente_a_archivo(datos_cliente):
'''
Crea el archivo a imprimir y le agrega los datos del cliente
'''
    with open('clientes.txt', 'a') as archivo:
        archivo.write(",".join(datos_cliente) + "\n")
def facturacion(datos_cliente, volumen, materiales, tipo_cliente, tipo_factura,unidad):
'''
Crea el archivo a imprimir agregando: Datos del cliente, datos fiscales, Tipo de factura para el cliente y los datos de los materiales necesarios
'''
    cliente = datos_cliente # datos personales
    categoria_cliente = tipo_cliente # datos fiscales
    factura = tipo_factura # tipo de factura para el cliente
    material = materiales # datos de los materiales necesarios para la construccion
    with open('facturacion.txt', 'a') as archivo:
        archivo.write(f"FACTURA TIPO: {factura}, {categoria_cliente}\n")
        archivo.write(f"Cliente: {cliente[1]}\n")
        archivo.write(f"Telefono: {cliente[3]}\n")
        archivo.write(f"Email: {cliente[5]}\n")
        if unidad == 1:
            archivo.write(f"Volumen de hormigon solicitado: {volumen} m3\n")
        else:
            archivo.write(f"Volumen de hormigon solicitado: {volumen} p3\n")
        archivo.write("Materiales:\n")
        for material in materiales:
            archivo.write(material + "\n")
        archivo.write("\n")
#endregion
#region ProgramaPrincipal
while True:
'''
Los llamados principales para la recoleccion de datos y el correcto funcionamiento del programa
'''
    info_cliente = datos_cliente()
    tipo_cliente, tipo_factura = seleccion_tipo_cliente()
    info_cliente.append("Tipo de Cliente: " + tipo_cliente)
    volumen, unidad = calculo_de_volumen()
    seleccion_de_resistencia = Resistencia(volumen, unidad)
    confirmar_pedido = True
    while confirmar_pedido:
    '''
    Confirma o descarta las selecciones del cliente
    '''
        try:
            print('''Confirmar pedido [1]
Descartar pedido [9]''')
            confirmacion = int(input())
            if confirmacion == 1 or confirmacion == 9:
                if confirmacion == 1:
                    #region Llamado_Archivo
                    agregar_cliente_a_archivo(info_cliente)
                    facturacion(info_cliente, volumen, seleccion_de_resistencia, tipo_cliente, tipo_factura, unidad)
                    os.system("cls")
                    print("Su compra fue efectuada con exito")
                    confirmar_pedido = False
                    #endregion
                else:
                    os.system("cls")
                    print("Su pedido a sido cancelado con exito")
                    confirmar_pedido = False
            else:
                os.system("cls")
                print("Opcion seleccionada no reconocida, por favor intente de nuevo.")
        except ValueError:
            os.system("cls")
            print("Opcion seleccionada no reconocida, por favor intente de nuevo.")
            #endregion
