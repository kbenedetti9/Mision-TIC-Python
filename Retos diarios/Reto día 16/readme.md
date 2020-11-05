## Retos del día

***OJO*** 
1. Recuerda que es tu responsabilidad definir la función indicada y retornar el valor solicitado. <br/>
    def reto1():<br/>
        print(resultado) o return resultado
2. Las funciones podrán recibir parámetros o solicitar los datos al usuario usando la función input() de Python. Revisa el enunciado del reto para determinar como se deben recibir los valores y recuerda que para input() los valores serán entregados en el orden que sea indicado en el enunciado.
3. Hemos ampliado el plazo para enviar el reto hasta las 7:00 am del día siguiente, así que toma el tiempo necesario para analizar y desarrollar tu solución. Recuerda que lo más importante antes de empezar a programar es pensar en el algoritmo que vas a utilizar. Cuales son los pasos para solucionar el problema? La implementación y las funciones a usar se pueden encontrar una vez esto este claro.


<b>INFORMACIÓN IMPORTANTE:</b> Recuerda que los retos del día son una oportunidad de reforzar los conocimientos adquiridos en esta sesión teórica y adicionalmente sirven para modificar, practicar y aprender a considerar soluciones alternas. Por este motivo, es importante no sólo usar el contenido de la sesión síncrona y preguntar a los monitores, sino también buscar en Internet soluciones viables a los problemas planteados. 

### Reto #1
Crea una funcion reto1(x, y) que reciba dos listas de igual tamaño N, y retorne una tercera lista (z) que tenga el menor (o el mismo) de los números en cada una de las posiciones de ambas listas. Si no son del mismo tamaño debe retornar "Error en los datos"

*A continuacion encontraras las funciones que debe contener tu algoritmo, y datos de ejemplo para que realices tus pruebas:*

<table>
<thead><tr>
<th>Funcion</th>
<th>Parametros de entrada<br> (argumentos)</th>
<th>Valores entrados por el<br> usuario dentro de la función</th>
<th>Valores a imprimir</th>
<th>Valores a retornar <br>por la función</th>
</tr>
</thead>
<tbody>
<tr>
<td><code> reto1(x,y)</code></td>
<td>x, y        #Listas</td>
<td></td>
<td> z                     #Lista<br/>
    "Error en los datos"  #Si x y y no tienen el mismo número de elementos</td>
    <td></td>
</tr>
<tr>
<td><code> reto1([1, 4, 6], [3, 8, 2])</code></td>
<td>[1, 4, 6], [3, 8, 2]</td>
<td></td>
<td>[1, 4, 2]             <br/></td>
    <td></td>
</tr>
<tr>
<td><code> reto1([1, 4, 2], [1, 4, 5])</code></td>
<td>[1, 4, 2], [1, 4, 5]</td>
<td></td>
<td>[1, 4, 2] <br/></td>
    <td></td>
</tr>
<tr>
<td><code> reto1([1, 4, 2], [1, 4])</code></td>
<td>[1, 4, 2], [1, 4]</td>
<td></td>
<td>"Error en los datos"           <br/></td>
    <td></td>
</tr>
</tbody></table>

### Reto #2

Proponga una función reto2(x, y) que tome como entrada dos vectores x y y. Calcule la diferencia simétrica entre ellos, es decir los elementos de A que no se encuentran en B y los elementos de B que no se encuentran en A y retorne la lista final.

*A continuacion encontraras las funciones que debe contener tu algoritmo, y datos de ejemplo para que realices tus pruebas:*

<table>
<thead><tr>
<th>Funcion</th>
<th>Parametros de entrada<br> (argumentos)</th>
<th>Valores entrados por el<br> usuario dentro de la función</th>
<th>Valores a imprimir</th>
<th>Valores a retornar <br>por la función</th>
</tr>
</thead>
<tbody>
<tr>
<td><code> reto2(x,y)</code></td>
<td>x, y        #Listas</td>
<td></td>
<td> </td>
    <td>z                     #Lista</td>
</tr>
<tr>
<td><code> reto2([1,2,3],[3,4,5])</code></td>
<td>[1,2,3],[3,4,5]</td>
<td></td>
<td></td>
    <td>[1,2,4,5]</td>
</tr>
<tr>
<td><code> reto2([1],[2,3,4,5,6,7])</code></td>
<td>[1],[2,3,4,5,6,7]</td>
<td></td>
<td></td>
    <td>[1,2,3,4,5,6,7]</td>
</tr>
<tr>
<td><code> reto2([1, 4, 2], [1, 4, 2])</code></td>
<td>[1, 4, 2], [1, 4, 2]</td>
<td></td>
<td></td>
    <td>[]</td>
</tr>
</tbody></table>
