#region importaciones#
import platform
import os
#endregion

#region Funciones
def limpiar_pantalla():
    '''
    Esta funcion limpia la consola dependiendo de si se usa windows o linux
    NOTA: Esta hecho asi por diferencias entre ordenadores del equipo
    '''
    if (platform.system() == "windows"):
        os.system("cls")
    else:
        os.system("clear")
def selector_unidad():
    '''
    Esta funcion pide el tipo de unidad que se desea utilizar, calcula el volumen y lo manda a la funcion resistencia para hacer los calculos
    se guarda en una variable para poder retornarla y que los datos se puedan reutilizar sin tener que llamar nuevamente a la funcion
    NOTA: revisar las unidades de medidas estan hechas siempre en metros
    '''
    print('''
Unidades:
	1) Metros        5) Decametro
	2) Kilometros    6) Centimetro
	3) Yardas        7) Milimetro
	4) Hectometro
	''')
    unidad=int(input("Que tipo de unidad deseas utilizar? "))
    #unidad = int(input("cual unidad va a utilizar\n kilómetro(1)\n hectómetro(2)\n decámetro(3)\n metro(4)\n decímetro(5)\n centímetro(6)\n milímetro(7)"))
    match unidad:
    	case 1:
		    largo_superficie=float(input("Cual es el largo de la superficie? "))
		    ancho_superficie=float(input("Cual es el ancho de la superficie? "))
		    alto_superficie=float(input("Cual es la altura de la superficie? "))
		    volumen=largo_superficie*ancho_superficie*alto_superficie
		    print("el volumen es de: ", volumen, "m3")
		    resis=resistencia(volumen)
    	case 2:
		    print("Cambiar a yardas en proceso")
		    '''
		    para pasar de yardas a metro es la siguiente operacion:
		    medida en yarda * 0.9144 / 1
		    '''
		    pass
    selector=[largo_superficie,ancho_superficie,alto_superficie,volumen,resis]
    return(selector)
def datos_cliente():
    '''
    En esta funcion se le pide los datos al cliente guardando Nombre, Apellido, telefono y email en variables que luego se devolveran para poder usarlos cuando sea necesario sin necesidad de llamar a la funcion
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
    datos=[nombre_cliente,apellido_cliente,telefono_cliente,mail_cliente]
    return(datos)
    
def calcular_concreto(volumen, cemento_kg, arena_m3, grava_m3, agua_litro, saco_cemento, resistencia_concreto_psi):
    '''
    Esta funcion calcula:
    * El cemento total necesario para la superficie.
    * La cantidad de arena necesaria
    * La cantidad de grava necesaria
    * La cantidad de agua necesaria
    y los muestra en pantalla redondeando solo con dos decimales
    Tambien guarda todo en una variable para reutilizarlas cuando sea necesario sin necesidad de llamar nuevamente a la funcion
    '''
    cemento_total=(volumen*saco_cemento)*1.05 #desperdicio de 1.05
    arena_total=(volumen*arena_m3)
    grava_total=(volumen*grava_m3)
    agua_total=(volumen*agua_litro)
    print(f'''
    Para una Resistencia de {resistencia_concreto_psi} necesitaras:
    El cemento total es de: {round(cemento_total,2)}Kg
    La arena total es de: {round(arena_total,2)}m3
    La grava total es de: {round(grava_total,2)}m3
    El agua total es de: {round(agua_total,2)}L
          ''')
    calcular=[cemento_total,arena_total,grava_total,agua_total]
    return(calcular)
def resistencia(volumen):
    '''
    En esta funcion se pide el tipo de resistencia para guardarlo en una variable y calcular el concreto con los valores adecuados para cada resistencia.
    Si no se selecciona algun valor de la lista se vuelve a llamar a si misma hasta que ponga un valor correcto
    NOTA: buscar para que sirve cada tipo de resistencia
    NOTA: los sacos de cemento se calculan con sacos de 50kg
    '''
    print('''
Resistencias:
          1) 3.500
          2) 3.000
          3) 2.500
          4) 2.000
          5) 1.500''')
    resistencia_concreto_psi=int(input("Que tipo de resistencia psi deseas usar? "))
    
    match resistencia_concreto_psi: #Dependiendo de la opcion que elija el usuario va a hacer los calculos segun la resistencia
        case 1:
            resistencia_concreto_kg=246
            cemento_kg=420
            arena_m3=0.67
            grava_m3=0.67
            agua_litro=220
            saco_cemento=8 #lo redondie hacia arriba porque no se puede comprar media bolsa de cemento y 3 medialunas xD
            resistencia_concreto_psi=3500
            calcular=calcular_concreto(volumen, cemento_kg, arena_m3, grava_m3, agua_litro, saco_cemento, resistencia_concreto_psi) #va a la funcion para calcular los materiales y el concreto y los guarda en una variable para usarlos cuando sea necesario
            return(resistencia_concreto_psi, calcular) #devuelve los valores para que puedan ser usados fuera de la funcion
        case 2:
            resistencia_concreto_kg=210
            cemento_kg=350
            saco_cemento=7
            arena_m3=0.56
            grava_m3=0.84
            agua_litro=180
            resistencia_concreto_psi=3000
            calcular=calcular_concreto(volumen, cemento_kg, arena_m3, grava_m3, agua_litro, saco_cemento, resistencia_concreto_psi)
            return(resistencia_concreto_psi, calcular)
        case 3:
            resistencia_concreto_kg=175
            cemento_kg=300
            arena_m3=0.48
            grava_m3=0.96
            agua_litro=170
            saco_cemento=6
            resistencia_concreto_psi=2500
            calcular=calcular_concreto(volumen, cemento_kg, arena_m3, grava_m3, agua_litro, saco_cemento, resistencia_concreto_psi)
            return(resistencia_concreto_psi, calcular)
        case 4:
            resistencia_concreto_kg=140
            cemento_kg=260
            arena_m3=0.63
            grava_m3=0.84
            agua_litro=170
            saco_cemento=5
            resistencia_concreto_psi=2000
            calcular=calcular_concreto(volumen, cemento_kg, arena_m3, grava_m3, agua_litro, saco_cemento, resistencia_concreto_psi)
            return(resistencia_concreto_psi, calcular)
        case 5:
            resistencia_concreto_kg=105
            cemento_kg=210
            arena_m3=0.5
            grava_m3=1.0
            agua_litro=160
            saco_cemento=4
            resistencia_concreto_psi=1500
            calcular=calcular_concreto(volumen, cemento_kg, arena_m3, grava_m3, agua_litro, saco_cemento, resistencia_concreto_psi)
            return(resistencia_concreto_psi, calcular)
        case resistencia_concreto: #si no de selecciona ninguna de las opciones permitidas vuelve a llamarse para que el usuario ponga un valor correcto
            limpiar_pantalla()
            print("Selecciona un valor de la tabla")
            R = resistencia()
            return R
    return(resistencia_concreto_psi, calcular)
#endregion
#region Principal_Inicio
limpiar_pantalla()
    
datos=datos_cliente()
selector=selector_unidad()

#region DatosClientes
nombre_cliente=datos[0]
apellido_cliente=datos[1]
telefono_cliente=datos[2]
email_cliente=datos[3]
#endregion
#region DatosSuperficie
LargoSuperficie=selector[0]
AnchoSuperficie=selector[1]
AltoSuperficie=selector[2]
VolumenSuperficie=selector[3]
ResistenciaRequerida=selector[4][0]
#endregion
#region MaterialesRequeridos
Cemento=round(selector[4][1][0],2)
Arena=round(selector[4][1][1],2)
Grava=round(selector[4][1][2],2)
Agua=round(selector[4][1][3],2)
#endregion

limpiar_pantalla()

print("Datos del cliente: ")
print(f"Nombre: {nombre_cliente}")
print(f"Apellido: {apellido_cliente}")
print(f"Telefono: {telefono_cliente}")
print(f"Email: {email_cliente}")
print(" ")
print("Datos Sobre la superficie: ")
print(f"Largo de la superficie: {LargoSuperficie}")
print(f"Ancho de la superficie: {AnchoSuperficie}")
print(f"Altura de la superficie: {AltoSuperficie}")
print(f"Volumen de la superficie: {VolumenSuperficie}")
print(f"Resistencia Requerida: {ResistenciaRequerida}")
print(" ")
print("Materiales Requeridos: ")
print(f"Cemento: {Cemento}")
print(f"Arena: {Arena}")
print(f"Grava: {Grava}")
print(f"Agua: {Agua}")
#endregion
