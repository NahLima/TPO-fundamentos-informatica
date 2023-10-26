#  TPO-fundamentos-informatica grupo 3
Criterio de evaluación: Se evaluarán los siguientes aspectos:

--> Funcionamiento del programa.

-->Técnicas de programación y estrategias de resolución del problema.

--> Prolijidad y claridad del código y de la interfaz de usuario. 

--> La calificación final recibida por cada integrante dependerá no solo del trabajo presentado sino también de la defensa ejercida en forma individual.  Por esta razón, pueden tener notas diferentes miembros del mismo grupo.


*ENUNCIADO*

**Título: Empresa de Electricidad**

Una empresa que se dedica a la distribución de electricidad, tiene distintos tipos de clientes que consumen energía y el precio varía según el rubro. Todos los meses, tienen que generar la facturación de los tipos de clientes, el cual se calcula según la cantidad de KW/Hora consumido y el rubro al cual pertenece y para ello cuentan con la siguiente información:

| Tipo de cliente | Costo fijo hasta 500 KW/HORA | Costo adicional KW/HORA HASTA 2000 | Costo adicional KW/HORA A PARTIR DE LOS 2000 |
|-----------------|------------------------------|-----------------------------------|---------------------------------------------|
| RESIDENCIAL     | $750                         | $6,5                              | $15                                         |
| COMERCIO        | $1500                        | $7,5                              | $15                                         |
| PYME            | $3000                        | $8                                | $25                                         |
| INDUSTRIA       | $7500                        | $10                               | $30                                         |
| ESTATAL         | $3500                        | $3,5                              | $10                                         |


Además, se sabe que, por la zona en donde la empresa opera, la cantidad máxima de clientes que puede tener es de 1000 pero tiene un mínimo de 100. También, la cantidad de KW/HORA mínimas que se consumen por cliente son desde 300 KW/HORA pero nunca superan los 3000 KW/HORA.

La empresa cuenta con todos los datos de los consumos de los clientes en el mes y por tipo de rubro.  Necesita que se calcule la facturación de cada uno y poder, de esta forma responder las siguientes necesidades:

- Total de la facturación del mes y cuantos clientes fueron.

- Total de facturación por tipo de cliente y la cantidad de clientes ordenado por facturación.

-	Listado completo detallado del total facturado de cada cliente con su tipo, ordenado por total facturado.

- Poder seleccionar un tipo de cliente y que se detallen la facturación y cantidad de clientes del mismo.

**Objetivo**: 
Se solicita el desarrollo de un programa, con un menú principal para poder acceder a las opciones detalladas.  El programa solo debe terminar cuando el usuario elija la opción del menú correspondiente a SALIR.

Los datos serán generados por números al azar ya que la carga manual se complejiza para la ejecución. Tener en cuenta las restricciones del enunciado para determinar las cantidades correctas al realizar esta generación de datos.

