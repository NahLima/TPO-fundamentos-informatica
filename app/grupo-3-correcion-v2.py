'''Una empresa que se dedica a la distribución de electricidad, tiene distintos tipos de clientes que consumen energía y el precio varía según el rubro.
Todos los meses, tienen que generar la facturación de los tipos de clientes,
el cual se calcula según la cantidad de KW/Hora consumido y el rubro al cual pertenece y para ello cuentan con la siguiente información:
    
Tipo de cliente|Costo fijo hasta 500 |Costo adicional    |Costo adicional
               |KW/HORA              |KW/HORA HASTA 2000 |KW/HORA A PARTIR DE LOS 2000
               |                     |                   |
RESIDENCIAL    |$750                 |$6,5               |$15
COMERCIO       |$1500                |$7,5               |$15
PYME           |$3000                |$8                 |$25
INDUSTRIA      |$7500                |$10                |$30
ESTATAL        |$3500                |$3,5               |$10

Además, se sabe que, por la zona en donde la empresa opera, la cantidad máxima de clientes que puede tener es de 1000 pero tiene un mínimo de 100.
También, la cantidad de KW/HORA mínimas que se consumen por cliente son desde 300 KW/HORA pero nunca superan los 3000 KW/HORA.
La empresa cuenta con todos los datos de los consumos de los clientes en el mes y por tipo de rubro.
Necesita que se calcule la facturación de cada uno y poder, de esta forma responder las siguientes necesidades:

-Total de la facturación del mes y cuantos clientes fueron.
-Total de facturación por tipo de cliente y la cantidad de clientes ordenado por facturación.
-Listado completo detallado del total facturado de cada cliente con su tipo, ordenado por total facturado.
-Poder seleccionar un tipo de cliente y que se detallen la facturación y cantidad de clientes del mismo.

Objetivo:
Se solicita el desarrollo de un programa, con un menú principal para poder acceder a las opciones detalladas.
El programa solo debe terminar cuando el usuario elija la opción del menú correspondiente a SALIR.
Los datos serán generados por números al azar ya que la carga manual se complejiza para la ejecución.
Tener en cuenta las restricciones del enunciado para determinar las cantidades correctas al realizar esta generación de datos.'''

import random

# Definición de tarifas por tipo de cliente
# Aca agregamos una variable llamada tarifas y le poneos las listas de los diferentes tipos de clientes

tarifas = [['RESIDENCIAL', 750, 6.5, 15], ['COMERCIO', 1500, 7.5, 15], ['PYME', 3000, 8, 25], ['INDUSTRIA', 7500, 10, 30], ['ESTATAL', 3500, 3.5, 10]]


# Función para identificar un index

def find_index(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1


# Función para pegar el tipo de tarifa
# Aca abrimos una nueva variable llamada tipo de cliente, a la cual le pediremos que nos traiga solo los nombres de los clientes

tipo_de_cliente = ['RESIDENCIAL', 'COMERCIO', 'PYME', 'INDUSTRIA', 'ESTATAL']


# esta es otra forma para llamar a los clientes
'''def tipo_de_cliente(tarifas):
    tipos = []
    for tipo in tarifas:
        tipos.append(tipo[0])
    return tipos'''

# Función para convertir minusculas en mayusculas mayus_minus(text, 'mayus')
def mayus_minus(input, case):
    minus = "abcdefghijklmnopqrstuvwxyz"
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    convertido = ""
    for w in input:
        buscar = False  # Variable para verificar si el caractere fue encontrado
        for j in range(len(minus)):
            if case == "minus" and (minus[j] == w or mayus[j] == w):
                convertido += minus[j]
                buscar = True
            elif case == "mayus" and (mayus[j] == w or minus[j] == w):
                convertido += mayus[j]
                buscar = True
        if not buscar:
            convertido += w
    return convertido


# Función para generar datos de clientes aleatorios
'''En esta parte creamos una nueva función llamada datos_clientes para almacenar en esta sus diferentes datos;
   a los tipo_de_cliente les agregamos una variable, creamos datos_clientes donde se guardara todo, total de facturacion
   empezando en 0 y total de cliente que es de 100-1000 y que los eliga aleatoreamente'''


def generar_datos_clientes():
    tipos_clientes = tipo_de_cliente
    datos_clientes = []
    total_facturacion_mes = 0
    total_clientes = random.randint(100, 1000)

    for item in range(total_clientes):
        '''creamos un random.randint para que nos eliga aleatoriamente el tipo de cliente:
           y añadimos len() para que tenga el rango de clientes'''
        tipo_cliente = tipo_de_cliente[random.randint(0, len(tipo_de_cliente) - 1)]
        '''los consumos minimos por cliente son de 300 pero nunca superan los 3000'''
        consumo = random.randint(300, 3000)
        '''luego aplicamos la variable tarifa_index para almacenar la posicion del cliente'''
        tarifa_index = find_index(tipos_clientes, tipo_cliente)
        '''y por ultimo facturación que seria para guardar el tipo de cliente con su facturación, [1](es la tarifa)'''
        facturacion = tarifas[tarifa_index][1]  # costo fijo

        '''hacemos los consumos de clientes, si son menos de 500 sera el primero, si son mas de 500 y menos de 2000 se hace
           el consumo menos 500 por el segundo cuadrante, mas el consumo de 500. y si el consumo supera los 2000, sera el consumo
           menos los 2000 por el 3 cuadrante mas el consumo de 500'''
        if consumo <= 500:
            facturacion = tarifas[tarifa_index][1]
        elif consumo > 500 or consumo <= 2000:
            facturacion = (consumo - 500) * \
                tarifas[tarifa_index][2] + tarifas[tarifa_index][1]
        else:
            facturacion = (consumo - 2000) * \
                tarifas[tarifa_index][3] + tarifas[tarifa_index][1]

        datos_clientes.append([tipo_cliente, consumo, facturacion])
        total_facturacion_mes += facturacion

    return datos_clientes, total_facturacion_mes


# Función para mostrar la facturación por tipo de cliente


# HASTA ACAAAAAAAAAAAAAAA
def facturacion_por_tipo(datos_clientes):
    facturacion_tipo = []

    for tipo in tarifas:
        tipo_cliente = tipo[0]
        total_facturacion = 0
        cantidad_clientes = 0

        for cliente in datos_clientes:
            if cliente[0] == tipo_cliente:
                total_facturacion += cliente[2]
                cantidad_clientes += 1

        facturacion_tipo.append(
            [tipo_cliente, total_facturacion, cantidad_clientes])

    return facturacion_tipo

# Función para mostrar el listado completo de clientes

def listado_completo(datos_clientes):
    return datos_clientes

# Función de ordenamiento

#bubble sort
def ordenar_por_facturacion(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j][2] < datos[j + 1][2]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                
                

# # Función principal del programa


def programa_principal():
    datos_clientes_total_facturacion_mes = generar_datos_clientes()
    datos_clientes = datos_clientes_total_facturacion_mes[0]
    total_facturacion_mes = datos_clientes_total_facturacion_mes[1]

    opcion = None

    while opcion != '5':
        print("\nMenú Principal:")
        print("1. Mostrar Total de Facturación del Mes y Cantidad de Clientes")
        print("2. Mostrar Facturación por Tipo de Cliente")
        print("3. Mostrar Listado Completo de Clientes")
        print("4. Seleccionar Tipo de Cliente")
        print("5. Salir")

        opcion = int(input("Elija una opción (1/2/3/4/5): "))
        
        while opcion < 1 or opcion > 5:
            print("Opción no válida. Por favor, ingrese 1, 2, 3, 4 o 5.")
            opcion = input("Elija una opción (1/2/3/4/5): ")

        if opcion == 1:
            print("Total de Facturación del Mes:", total_facturacion_mes)
            print("Cantidad de Clientes:", len(datos_clientes))
            
        elif opcion == 2:
            facturacion_tipo = facturacion_por_tipo(datos_clientes)
            ordenar_por_facturacion(facturacion_tipo)
            
            print("Facturación por Tipo de Cliente:")
            
            for tipo in facturacion_tipo:
                print(tipo[0] + ": Total Facturación -",
                      tipo[1], "Cantidad de Clientes -", tipo[2])
                
        elif opcion == 3:
            lista_clientes = listado_completo(datos_clientes)
            ordenar_por_facturacion(lista_clientes)
            print("Listado Completo de Clientes:")
            for cliente in lista_clientes:
                print("Tipo:", cliente[0], "Consumo:",
                      cliente[1], "KW/HORA, Facturación:", cliente[2])
        elif opcion == 4:
            tipo_elegido = input("Elija un tipo de cliente (RESIDENCIAL/COMERCIO/PYME/INDUSTRIA/ESTATAL): ")
            tipo_elegido_convertido = mayus_minus(tipo_elegido, 'mayus')
            total_facturacion_tipo = 0
            cantidad_clientes_tipo = 0
            
            for cliente in datos_clientes:
                if cliente[0] == tipo_elegido_convertido:
                    total_facturacion_tipo += cliente[2]
                    cantidad_clientes_tipo += 1
                    
            if cantidad_clientes_tipo > 0:
                print("Tipo de Cliente:", tipo_elegido_convertido)
                print("Total de Facturación:", total_facturacion_tipo)
                print("Cantidad de Clientes:", cantidad_clientes_tipo)
            else:
                print("Tipo de cliente no válido. Intente de nuevo.")


    print("Saliendo del programa...")


# Llamada a la función principal para iniciar el programa
programa_principal()
