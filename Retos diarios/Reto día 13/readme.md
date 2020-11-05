## Retos del día

***OJO*** 
1. Recuerda que es tu responsabilidad definir la función indicada y retornar el valor solicitado. <br/>
    def reto1():<br/>
        print(resultado) o return resultado
2. A partir de esta sesión, las funciones podrán recibir parámetros o solicitar los datos al usuario usando la función input() de Python. Revisa el enunciado del reto para determinar como se deben recibir los valores y recuerda que para input() los valores serán entregados en el orden que sea indicado en el enunciado.
3. Hemos ampliado el plazo para enviar el reto hasta las 7:00 am del día siguiente, así que toma el tiempo necesario para analizar y desarrollar tu solución. Recuerda que lo más importante antes de empezar a programar es pensar en el algoritmo que vas a utilizar. Cuales son los pasos para solucionar el problema? La implementación y las funciones a usar se pueden encontrar una vez esto este claro.


<b>INFORMACIÓN IMPORTANTE:</b> Recuerda que los retos del día son una oportunidad de reforzar los conocimientos adquiridos en esta sesión teórica y adicionalmente sirven para modificar, practicar y aprender a considerar soluciones alternas. Por este motivo, es importante no sólo usar el contenido de la sesión síncrona y preguntar a los monitores, sino también buscar en Internet soluciones viables a los problemas planteados. 

### Reto del día 1
Crea una función mayor(x) que reciba una lista x e imprima el mayor número de la lista y el número de veces que aparece el mayor.

Crea una funcion reto1() que no reciba parámetros pero lea el numero de elementos a ingresar y los elementos de la lista y llame a la función mayor(x).

***Ojo*** El primer valor a ingresar cuando se llama la función reto1() es el numero de elementos N que tiene la lista y los siguientes N valores son los elementos de la lista. 

Ejemplo: <br/>
reto1() <br/>
input() recibe 5 ---- Este es el numero de elementos <br/>
input() recibe 20 <br/>
input() recibe 32 <br/>
input() recibe 8 <br/>
input() recibe 32 <br/>
input() recibe 3 <br/>
imprime <br/>
Mayor 32 <br/>
Veces 2

mayor([2,3,5,8,1]) imprime <br/>
8
1

### Reto del día 2

Escribe una función reto2(x,y,z) donde x es el número de elementos, y es el valor inicial y z la diferencia entre cada elemento. Con estos parámetros crea una lista de x elementos que inicia en y y va de z en z.

Ejemplo:<br/>
reto2(6,2,5) devuelve<br/>
[2,7,12,17,22,27]

reto2(3,11,7) devuelve<br/>
[11,18,25]
