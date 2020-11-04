## RETO SEMANA 5 

Llegó la hora de implementar! Transportes del Norte te ha contactado para desarrollar una interfaz para su Departamento de Logística. Es esta unidad de negocio la encargada de toda la interacción con los clientes de Transporte del Norte. Es aquí donde se registran y se dan de baja clientes, se asignan camiones a cada cliente, se programan sus despachos periódicamente, y se llevan indicadores de desempeño, tanto para Transportes del Norte, como para cada uno de sus clientes.

Como sabes, el nuevo desarrollo está orientado a operadores del Departamento de Logística de Transportes del Norte. Tu desarrollo trabajará a partir de dos archivos que son el insumo para poder calcular los parámetros de desempeño. Por tanto, debe:

1. Leer desde el archivo “C1-S5 Valores Asignados.csv” los siguientes campos, correspondientes a la programación asignada por Transportes del Norte:
 * Nombre del cliente de Transporte del Norte 
 * Punto de Distribución 
 * ID del Camión 
 * Carga a entregar 
 * Tiempo de despacho (minutos)


2. Leer desde el archivo “C1-S5 Valores Registrados.csv” los siguientes campos, correspondientes a la operación registrada por los conductores de Transportes del Norte:
 * Nombre del cliente de Transporte del Norte 
 * Punto de Distribución 
 * ID del Camión 
 * Carga a entregada 
 * Tiempo de despacho (minutos) 

Debes desarrollar una interfaz de consola que permita mostrar los indicadores de desempeño de cada vehículo, para cada cliente, permitiendo:

1. Escoger entre cada uno de sus dos principales clientes (Lactocaribe y Frigoaves)
2. Seleccionar el vehículo al que se le calcularán los indicadores de desempeño
3. Desplegar los siguientes indicadores de desempeño para cada vehículo:
 * Eficiencia en tiempos de despacho = (Tiempo total de despacho asignado - Tiempo total de despacho registrado) / Tiempo de total despacho asignado x 100 
 * Tasa de entrega (Lt/min) = Cantidad total de litros despachados / Tiempo total de despacho 
 * Nivel de Cumplimiento de los dchos = Total de Litros despachados / Total de litros asignados x 100 
 * Porcentaje de entregas a tiempo = No. de entregas a tiempo / No. Total de entregas realizadas 
4. Registrar (escribir) en un archivo CSV un informe con los 4 indicadores de desempeño anteriores, para cada camión y para cada cliente.

### EJEMPLO

1. Leer en tu codigo el archivo 'C1-S5 Valores Asignados.csv' y el archivo 'C1-S5 Valores Registrados.csv'
       La ubicación de estos se pasaran como parametro de entrada a la función control como puedes observar en el celda de    desarrollo. En ese orden.

2. La función de control tiene dos inputs en el siguiente orden:

    def control(asignacionfile, registrosfile) :
                cliente = input()  # Donde 1 corresponde a Lactocaribe y 2 a Frigogaves
                Camion = input()   # ID del camión de los cuales se van a obetner los indicadores de desempeño


3. La estructura de salida esperada para el caso donde se escoge el cliente 1 (Lactocaribe) y el Id del camión # 2, es la siguiente :

    Eficiencia en tiempo de Despacho = -11.8 %

    Tasa de entrega = 25.6

    Nivel de cumplimiento = 90.0 %

    Entregas a tiempo = 33.3 %

