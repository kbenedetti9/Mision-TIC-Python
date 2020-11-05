## Retos del día

***OJO*** 
1. Recuerda que es tu responsabilidad definir la función indicada y retornar el valor solicitado. <br/>
    def reto1():<br/>
        print(resultado) o return resultado
2. Las funciones podrán recibir parámetros o solicitar los datos al usuario usando la función input() de Python. Revisa el enunciado del reto para determinar como se deben recibir los valores y recuerda que para input() los valores serán entregados en el orden que sea indicado en el enunciado.
3. Hemos ampliado el plazo para enviar el reto hasta las 7:00 am del día siguiente, así que toma el tiempo necesario para analizar y desarrollar tu solución. Recuerda que lo más importante antes de empezar a programar es pensar en el algoritmo que vas a utilizar. Cuales son los pasos para solucionar el problema? La implementación y las funciones a usar se pueden encontrar una vez esto este claro.


<b>INFORMACIÓN IMPORTANTE:</b> Recuerda que los retos del día son una oportunidad de reforzar los conocimientos adquiridos en esta sesión teórica y adicionalmente sirven para modificar, practicar y aprender a considerar soluciones alternas. Por este motivo, es importante no sólo usar el contenido de la sesión síncrona y preguntar a los monitores, sino también buscar en Internet soluciones viables a los problemas planteados. 

### Reto #1
Crea una funcion reto1(T, Y) que reciba una matriz T[n][m] y una matriz Y[n][m] e imprima una matriz Z[n][m] que represente la suma de T y Y.

La función debe validar que T y Y tengan el mismo número de elementos, y si no es así, imprima un mensaje de error "Error en los datos".

*A continuacion encontraras las funciones que debe contener tu algoritmo, y datos de ejemplo para que realices tus pruebas:*

<table>
<thead><tr>
<th>Funcion</th>
<th>Parametros de entrada (argumentos)</th>
<th>Valores entrados por el <br>usuario dentro de la función</th>
<th>Valores a imprimir</th>
<th>Valores a retornar<br> por la función</th>
</tr>
</thead>
<tbody>
<tr>
<td><code> reto1(T,Y)</code></td>
<td>T , Y        #Matrices</td>
<td></td>
<td> Z                     #Matriz en orden ascendente <br/>
    "Error en los datos"  #Si la matriz T y Y no tienen los mismos elementos</td>
    <td></td>
</tr>
<tr>
<td><code> reto1([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[3,3,3],[2,2,2]])</code></td>
<td>[[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[3,3,3],[2,2,2]]</td>
<td></td>
<td>[[2,3,4],[7,8,9],[9,10,11]]             <br/></td>
    <td></td>
</tr>
<tr>
<td><code> reto1([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[3,3,3]])</code></td>
<td>[[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[3,3,3]]</td>
<td></td>
<td>"Error en los datos"           <br/></td>
    <td></td>
</tr>
<tr>
<td><code> reto1([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[3,3],[2,2,2]])</code></td>
<td>[[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[3,3],[2,2,2]]</td>
<td></td>
<td>"Error en los datos"           <br/></td>
    <td></td>
</tr>
</tbody></table>

### Reto #2

Crea una función crearMatriz(n) que dado un valor n, reciba los valores para generar una matriz cuadrada nxn y retorne dicha matriz. 

Crea una función validarMatriz(T) que reciba una matriz T y con esa matriz compruebe si es un cuadrado mágico o no. Si es, debe imprimir el resultado de la suma. Si no, imprime False.

Un cuadrado mágico es una tabla en la cual la suma de sus filas, columnas y diagonales (arriba y abajo) dan como resultado el mismo número.

Crea una función reto2(n) que llame a crearMatriz(n) y luego a validarMatriz(T).

*A continuacion encontraras las funciones que debe contener tu algoritmo, y datos de ejemplo para que realices tus pruebas:*

<table>
<thead><tr>
<th>Funcion</th>
<th>Parametros de entrada <br>(argumentos)</th>
<th>Valores entrados por el <br>usuario dentro de la función</th>
<th>Valores a imprimir</th>
<th>Valores a retornar<br> por la función</th>
</tr>
</thead>
<tbody>
<tr>
<td><code> crearMatriz(n)</code></td>
<td>n        #Numero de elementos nxn</td>
<td> nxn Enteros para llenar la matriz</td>
<td></td>
    <td>T   #Matriz creada</td>
</tr>
    <tr>
<td><code> crearMatriz(3)</code></td>
<td>3 </td>
<td> 2 <br/>
        7 <br/>
        6 <br/>
        9<br/>
        5<br/>
        1<br/>
        6<br/>
    1<br/>
    8
        </td>
<td></td>
    <td>[[2,7,6],[9,5,1],[6,1,8]]</td>
</tr>
    <tr><td/><td/><td/><td/><td/></tr>
    <tr><td/><td/><td/><td/><td/></tr>
    <tr>
<td><code> validarMatriz(T)</code></td>
<td>T        #Matriz</td>
<td></td>
<td>n        #Promedio<br/>
    False    #Si no es cuadrado magico</td>
    <td></td>
</tr>
    <tr>
<td><code> validarMatriz([[8,1,6],[3,5,7],[4,9,2]])</code></td>
<td>[[8,1,6],[3,5,7],[4,9,2]] </td>
<td> </td>
<td>15</td>
    <td></td>
</tr>
<tr>
<td><code> validarMatriz([[2,7],[9,5]])</code></td>
<td>[[2,7],[9,5]] </td>
<td> </td>
<td>False</td>
    <td></td>
</tr>
<tr><td/><td/><td/><td/><td/></tr>
    <tr><td/><td/><td/><td/><td/></tr>
<tr>
<td><code> reto2(n)</code></td>
<td>n #Numero de elementos nxn</td>
<td> nxn #Ccada elemento 
        </td>
<td>False<br/></td>
    <td></td>
</tr>
    <tr>
<td><code> reto2(3)</code></td>
<td>3</td>
<td> 2 <br/>
        7 <br/>
        6 <br/>
        9<br/>
        5<br/>
        1<br/>
        6<br/>
    1<br/>
    8
        </td>
<td>n        #Promedio<br/>
    False    #Si no es cuadrado magico</td>
    <td></td>
</tr>
</tbody></table>