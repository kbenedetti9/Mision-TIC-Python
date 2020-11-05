## Retos del día

<b>INFORMACIÓN IMPORTANTE:</b> Recuerda que los retos del día son una oportunidad de reforzar los conocimientos adquiridos en esta sesión teórica y adicionalmente sirven para modificar, practicar y aprender a considerar soluciones alternas. Por este motivo, es importante no sólo usar el contenido de la sesión síncrona y preguntar a los monitores, sino también buscar en Internet soluciones viables a los problemas planteados. 

Recuerda que tienes hasta la media noche para enviar el reto, así que toma el tiempo necesario para analizar y desarrollar tu solución. Lo más importante antes de empezar a programar es pensar en el algoritmo que vas a utilizar. Cuales son los pasos para solucionar el problema? La implementación y las funciones a usar se pueden encontrar una vez esto este claro.


### Reto del día 1
Genera un código que dado un número, calcule la suma de los números pares menores al valor hasta el 0. El número se incluye en la suma sea o no par.

Ejemplo:
Si el usuario ingresa 21
21+20+18+16+14+12+10+8+6+4+2 = 131

Si el usuario ingresa 6
6+4+2 = 12

### Reto del día 2

Cuenta la historia que Cayo Julio César, uno de los más grandes militares de la antigua Roma, comunicaba las órdenes a sus generales en los campos de batalla mediante mensajes cifrados. La forma utilizada por Julio Cesar para cifrar sus mensajes (conocida con posterioridad como cifrado Cesar), consistía en escribir el mensaje y posteriormente desplazar cada letra tres posiciones a la derecha. 

Por ejemplo, utilizando nuestro alfabeto, el sistema quedaría así:

Alfabeto original:       A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z
Alfabeto cifrado:        D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z A B C

Así las cosas, si se deseaba enviar el mensaje, EL ATAQUE A LOS GALOS INICIA EL LUNES EN LA MAÑANA. lo que se enviará a los generales es: HÑ DWDTXH D ÑRV JDÑRV LPLFLD HÑ ÑXPHV HP ÑD ODQDPD

Proponga una rutina que tome como entrada el mensaje a cifrar y devuelva el mensaje cifrado.

Recomendaciones:
1. Convierta el mensaje de entrada a mayúsculas, indiferentemente de cómo fueron escritos. Pista: Busca en Google u otro motor de busqueda
2. Sólo se desplazan las letras, espacios, signos de puntuación, números y demás permanecen sin cambios
3. Con los elementos aprendidos hasta el momento, considere la utlización de un Diccionario (como en el caso de Dependiendo De de la semana pasada) para obtener una letra cifrada dado una letra de entrada.  

Ejemplos:
"EL ATAQUE A LOS GALOS INICIA EL LUNES EN LA MAÑANA" devuelve 
HÑ DWDTXH D ÑRV JDÑRV LPLFLD HÑ ÑXPHV HP ÑD ODQDPD

"AYER ESTABA LLOVIENDO?" devuelve 
DBHU HVWDED ÑÑRYLHPGR?

### Reto del día 3
Escribe un programa que reciba una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase (incluye minúsculas y mayúsculas).

Ejemplo:
"Hoy es Jueves", "e" devuelve
3

"Aqui estamos todos", "a" devuelve
2