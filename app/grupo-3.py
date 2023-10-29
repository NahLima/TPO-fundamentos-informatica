import random

# Definición de tarifas por tipo de cliente
tarifas = [
    ['RESIDENCIAL', 750, 6.5, 15],
    ['COMERCIO', 1500, 7.5, 15],
    ['PYME', 3000, 8, 25],
    ['INDUSTRIA', 7500, 10, 30],
    ['ESTATAL', 3500, 3.5, 10]
]

# Función para identificar un index


def find_index(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1

# Función para pegar el tipo de tarifa


def get_tipo_tarifa(tarifas):
    tipos = []
    for tipo in tarifas:
        tipos.append(tipo[0])
    return tipos

# Función para convertir minusculas en mayusculas upper_text(text, 'upper')


def upper_text(input, case):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    convertido = ""

    for w in input:
        found = False  # Variable para verificar si el caractere fue encontrado
        for j in range(len(lower)):
            if case == "lower" and (lower[j] == w or upper[j] == w):
                convertido += lower[j]
                found = True
            elif case == "upper" and (upper[j] == w or lower[j] == w):
                convertido += upper[j]
                found = True
        if not found:
            convertido += w

    return convertido


# Función para generar datos de clientes aleatorios
def generar_datos_clientes():
    tipos_clientes = get_tipo_tarifa(tarifas)
    datos_clientes = []
    total_facturacion_mes = 0
    total_clientes = random.randint(100, 1000)

    for item in range(total_clientes):
        tipo_cliente = random.choice(tipos_clientes)
        consumo = random.randint(300, 3000)
        tarifa_index = find_index(tipos_clientes, tipo_cliente)
        facturacion = tarifas[tarifa_index][1]  # Costo fijo

        if consumo <= 500:
            # Costo adicional KW/HORA HASTA 2000
            facturacion += consumo * tarifas[tarifa_index][2]
        elif consumo <= 2000:
            facturacion += 500 * tarifas[tarifa_index][2]
            # Costo adicional KW/HORA A PARTIR DE LOS 2000
            facturacion += (consumo - 500) * tarifas[tarifa_index][3]
        else:
            facturacion += 500 * tarifas[tarifa_index][2]
            facturacion += 1500 * tarifas[tarifa_index][3]
            facturacion += (consumo - 2000) * tarifas[tarifa_index][3]

        datos_clientes.append([tipo_cliente, consumo, facturacion])
        total_facturacion_mes += facturacion

    return datos_clientes, total_facturacion_mes


# Función para mostrar la facturación por tipo de cliente
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

        opcion = input("Elija una opción (1/2/3/4/5): ")

        if opcion == '1':
            print("Total de Facturación del Mes:", total_facturacion_mes)
            print("Cantidad de Clientes:", len(datos_clientes))
        elif opcion == '2':
            facturacion_tipo = facturacion_por_tipo(datos_clientes)
            ordenar_por_facturacion(facturacion_tipo)
            print("Facturación por Tipo de Cliente:")
            for tipo in facturacion_tipo:
                print(tipo[0] + ": Total Facturación -",
                      tipo[1], "Cantidad de Clientes -", tipo[2])
        elif opcion == '3':
            lista_clientes = listado_completo(datos_clientes)
            ordenar_por_facturacion(lista_clientes)
            print("Listado Completo de Clientes:")
            for cliente in lista_clientes:
                print("Tipo:", cliente[0], "Consumo:",
                      cliente[1], "KW/HORA, Facturación:", cliente[2])
        elif opcion == '4':
            tipo_elegido = input("Elija un tipo de cliente (RESIDENCIAL/COMERCIO/PYME/INDUSTRIA/ESTATAL): ")
            tipo_elegido_convertido = upper_text(tipo_elegido, 'upper')
            total_facturacion_tipo = 0
            cantidad_clientes_tipo = 0
            for tipo in tarifas:
                # tipo_cliente = tipo[0]
                for cliente in datos_clientes:
                    if cliente[0] == tipo_elegido_convertido:
                        total_facturacion_tipo += cliente[2]
                        cantidad_clientes_tipo += 1
            if total_facturacion_tipo > 0:
                print("Tipo de Cliente:", tipo_elegido_convertido)
                print("Total de Facturación:", total_facturacion_tipo)
                print("Cantidad de Clientes:", cantidad_clientes_tipo)
            else:
                print("Tipo de cliente no válido. Intente de nuevo.")

    print("Saliendo del programa...")


# Llamada a la función principal para iniciar el programa
programa_principal()