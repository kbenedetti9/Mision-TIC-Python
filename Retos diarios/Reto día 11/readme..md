## Retos del día

***OJO*** A partir de esta sesión es tu responsabilidad definir la función indicada y retornar el valor solicitado. 
def reto1():
    print(resultado) o return resultado

<b>INFORMACIÓN IMPORTANTE:</b> Recuerda que los retos del día son una oportunidad de reforzar los conocimientos adquiridos en esta sesión teórica y adicionalmente sirven para modificar, practicar y aprender a considerar soluciones alternas. Por este motivo, es importante no sólo usar el contenido de la sesión síncrona y preguntar a los monitores, sino también buscar en Internet soluciones viables a los problemas planteados. 

Recuerda que tienes hasta la media noche para enviar el reto, así que toma el tiempo necesario para analizar y desarrollar tu solución. Lo más importante antes de empezar a programar es pensar en el algoritmo que vas a utilizar. Cuales son los pasos para solucionar el problema? La implementación y las funciones a usar se pueden encontrar una vez esto este claro.


### Reto del día 1
Crea una funcion reto1 que reciba tres numeros a, b y c. Calcule la suma (S) entre a y b y si S es menor o igual que c calcule la suma sucesiva de los numeros entre S y c (incluyéndolos). Si S es mayor que c debe calcular las multiplicaciones sucesivas de los numeros entre c y S (incluyéndolos). 

Ejemplos:<br/>
reto1(2,3,7)
Si los parámetros de entrada son a=2, b=3, y c=7 <br/>
a+b = 5 <br/>
5 < 7 <br/>
5 + 6 + 7 = 18. <br/> 

Ahora si  a=7, b=3, y c=7 <br/>
7 * 8 * 9 * 10 = 5040.

### Reto del día 2
Crea una función primo que reciba como parámetro un número entero X y determine si es Primo o No. Si es Primo, debe retornar True sino False.

Adicionalmente crea una función reto2 que recibe un número entero X como parámetro, y que valide todos los números de 1 hasta X llamando la función primo e imprima todos los que sean Primos (es decir que la función primo retorne True). ***Ojo*** Ambas funciones deben existir y serán probadas por el autotest.

Ejemplo:<br/>
reto2(11) Si el parametro de entrada es 11 <br/> 
imprime<br/>
2<br/>
3<br/>
5<br/>
7<br/>
11<br/><br/>
<br/>
primo(2) devuelve True <br/>
primo(4) devuelve False<br/>

