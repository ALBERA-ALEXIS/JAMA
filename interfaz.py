def datos_cliente():
    '''
    En esta funcion se le pide los datos al cliente guardando Nombre, Apellido, telefono y email en variables
    '''
    nombre_cliente = input("Nombre: ")
    apellido_cliente = input("Apellido: ")
    telefono_cliente = input("Telefono de Contacto: ")
    mail_cliente = input("Email de Contacto: ")
    print(f'''
          Nombre:  {nombre_cliente}
          Apellido: {apellido_cliente}
          Telefono: {telefono_cliente}
          Mail: {mail_cliente}''')
    pass

def resistencia():
    '''
    En esta funcion se pide el tipo de resistencia para guardarlo en una variable para usarla mas adelante
    
    NOTA: buscar para que sirve cada tipo de resistencia
    '''
    print('''
Resistencias:
          1) 3.500
          2) 3.000
          3) 2.500
          4) 2.000
          5) 1.500''')
    resistencia_concreto=int(input("Que tipo de resistencia deseas usar? "))
    match resistencia_concreto:
        case 1:
            return 3500
        case 2:
            return 3000
        case 3:
            return 2500
        case 4:
            return 2000
        case 5:
            return 1500
        case resistencia_concreto:
            print("Selecciona un valor de la tabla")
            R = resistencia()
            return R

unidad = int(input("cual unidad va a utilizar\n kilómetro(1)\n hectómetro(2)\n decámetro(3)\n metro(4)\n decímetro(5)\n centímetro(6)\n milímetro(7)"))

#region Pruebas
'''
datos_cliente()
R = resistencia()
print(R)
'''
#endregion