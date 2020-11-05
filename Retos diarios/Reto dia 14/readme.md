## Retos del día

***OJO*** 
1. Recuerda que es tu responsabilidad definir la función indicada y retornar el valor solicitado. <br/>
    def reto1():<br/>
        print(resultado) o return resultado
2. Las funciones podrán recibir parámetros o solicitar los datos al usuario usando la función input() de Python. Revisa el enunciado del reto para determinar como se deben recibir los valores y recuerda que para input() los valores serán entregados en el orden que sea indicado en el enunciado.
3. Hemos ampliado el plazo para enviar el reto hasta las 7:00 am del día siguiente, así que toma el tiempo necesario para analizar y desarrollar tu solución. Recuerda que lo más importante antes de empezar a programar es pensar en el algoritmo que vas a utilizar. Cuales son los pasos para solucionar el problema? La implementación y las funciones a usar se pueden encontrar una vez esto este claro.


<b>INFORMACIÓN IMPORTANTE:</b> Recuerda que los retos del día son una oportunidad de reforzar los conocimientos adquiridos en esta sesión teórica y adicionalmente sirven para modificar, practicar y aprender a considerar soluciones alternas. Por este motivo, es importante no sólo usar el contenido de la sesión síncrona y preguntar a los monitores, sino también buscar en Internet soluciones viables a los problemas planteados. 

### Reto del día 1
Crea una funcion reto1(T) que reciba una matriz T[n][m] e imprima primero la suma de los elementos pares y luego la suma de los elementos impares. 

Ejemplo: <br/>
reto1([[1,2,3],[4,5,6],[7,8,9]]) <br/>
imprime <br/>
20<br/>
25

### Reto del día 2

Las respuestas a una encuesta sobre la opinión de las personas con relación a la gestión del gobierno actual se almacenaron en una lista x. Proponga un programa en Python que calcule la frecuencia de cada una y las imprima en una matriz.

Cree una función reto2(x) que reciba la lista x. ***Ojo*** Debes validar los posibles valores de las respuestas: E, B, R, M, P, N, si el elemento no tiene uno de estos valores debe devolver 'Error en los datos'

Ejemplo:<br/> 
reto2([‘E’,’R’,’B’,’B’,’B’,’M’,’E’,’E’,’R’]) <br/>
Imprime  [['E', 3], ['R', 2], ['B', 3], ['M', 1]] 

reto2(['E','E','E','B','B','M','E','E','R','N','N','N','M','M','M','B','E','R','N','N','N','M','M','M','B']) <br/>
Imprime [['E', 6], ['B', 4], ['M', 7], ['R', 2], ['N', 6]] 

reto2([‘E’,’R’,’B’,’B’,'H']) <br/>
Imprime "Error en los datos" 

