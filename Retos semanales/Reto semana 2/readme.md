## Reto de la semana 

Uno de los clientes de Transportes del Norte es Frigoaves S.A.S., una empresa de alimentos que requiere mantener un control estricto sobre los tiempos de despacho de sus mercancías en sus 20 puntos de distribución. Actualmente, cada camión cuenta con un portal de antenas RFID, que realizan la lectura de cada caja de mercancía que sale por las puertas de su contenedor.

Además del control de inventario, Transportes del Norte desea brindarle a Frigoaves la posibilidad de llevar el control de tiempos de despacho que realiza en cada punto de distribución asignado, para garantizar las exigencias del Departamento de Logística de Frigoaves.  

Por su parte, Frigoaves ha definido los siguientes parámetros:
Un tiempo máximo de 15 minutos para la permanencia de cada camión en cada punto de distribución.
Una cantidad fija de 100 cajas de mercancía, a despachar en cada punto de distribución.

Teniendo en cuenta que cada camión sale cargado con 2000 cajas del centro de despacho de Frigoaves, desarrolla un programa que:
Lea la señal del portal de antenas RFID en el camión, y registre el conteo de cajas de mercancía, una a una, a medida que son extraídas del camión en cada punto de despacho.
Lleve un conteo del inventario existente en el contenedor del camión.
Emita una alarma si se excede el tiempo de despacho estipulado o si se entregan más productos de los especificados, por punto de despacho.
Genere un reporte al final de cada despacho, indicando el número de cajas entregadas y el tiempo de despacho, por cada uno de los 20 puntos de distribución.
En caso de que se entreguen más cajas de las estipuladas para cada punto de distribución, se debe notificar que “Se ha agotado el inventario” indicando el número del último punto de distribución que recibió la última caja.


### Ejemplo

1. La entrada des de la función controldecamion son Tiempo de entrega y cantidad de cajas, de esta forma controldecamion(TiempoDeEntrega, CantidadDeCajas). Para el caso que se utilice controldecamion(10,100), la salida esperada es la siguiente: 

  Punto de distribución # 1
<p> Caja # 1  </p>
<p> Caja # 2  </p>
<p> Caja # 3  </p>
<p> Caja # 4  </p>
<p> Caja # 5  </p>
<p> Caja # 6  </p>
<p> Caja # 7  </p>
<p> Caja # 8  </p>
<p> Caja # 9  </p>
<p> Caja # 10 (Con esta misma estructura hasta la caja 100) </p>
<p> . </p>
<p> . </p>
<p> . </p>
<p> Caja # 100 </p>
<p>  El total de cajas en inventario en el camión =  1900 </p>
<p>  Cantidad de cajas despachadas =  100 </p>
<p>  Tiempo de despacho =  10 </p>
<p>  Punto de distribución # 2 (Asi mismo, para cada punto de distirbución hasta el 20) </p>
<p> . </p>
<p> . </p>
<p> . </p>
<p>  Punto de distribución # 20 </p>
<p>  Caja # 1 </p>
<p> Caja # 2  </p>
<p> Caja # 3  </p>
<p> Caja # 4  </p> Caja # 2
<p> . </p>
<p> . </p>
<p> . </p>
<p> Caja # 99 </p>
<p> Caja # 100 </p>
<p>  El total de cajas en inventario en el camión =  0 </p>
<p>  Cantidad de cajas despachadas =  100 </p>
<p>  Tiempo de despacho =  10 </p>


2. En caso de que el tiempo ingresado sea 20, controldecamion(20,100), como el tiempo de entrega (20) es mayor al tiempo maximo de entrega que son 15 minutos, que se imprima este mensaje: "Se excede el limite de tiempo"




3. En caso de que la cantidad de cajas a entregar supere el valor de 100, por ejemplo: controldecamion(10,102), la salida esperada es la siguiente:

  Punto de distribución # 1
<p> Caja # 1  </p>
<p> Caja # 2  </p>
<p> Caja # 3  </p>
<p> Caja # 4  </p>
<p> Caja # 5  </p>
<p> Caja # 6  </p>
<p> Caja # 7  </p>
<p> Caja # 8  </p>
<p> Caja # 9  </p>
<p> Caja # 10 </p>
<p> . </p>
<p> . </p>
<p> . </p>
<p> Caja # 100 </p>
<p> Encender alarma <p>
<p> Caja # 101 </p>
<p> Encender alarma <p>
<p> Caja # 102 </p>    
<p>  El total de cajas en inventario en el camión =  1898 </p>
<p>  Cantidad de cajas despachadas =  102 </p>
<p>  Tiempo de despacho =  10 </p>
<p>  Punto de distribución # 2 (Asi mismo, para cada punto de distirbución hasta el que alcance el inventario en el camión) </p>
<p> . </p>
<p> . </p>
<p> . </p>
<p>  Punto de distribución # 20 </p>
<p> Caja # 1 </p>
<p> Caja # 2  </p>
<p> Caja # 3  </p>
<p> Caja # 4  </p> Caja # 2
<p> . </p>
<p> . </p>
<p> . </p>
<p> Caja # 61</p>
<p> Caja # 62 </p>
<p> Se ha agotado el inventario en el camión<p>
<p>  El total de cajas en inventario en el camión =  0 </p>
<p>  Cantidad de cajas despachadas =  62 </p>
<p>  Tiempo de despacho =  10 </p>



