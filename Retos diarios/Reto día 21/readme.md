## RETO SEMANA 4 - DIA 5 MANTENIMIENTO

Durante la revisión del entregable que ya ha sido aprobado, LactoCaribe Ltda. manifiesta que requiere conocer un nuevo indicador de desempeño para cada camión:

    Entregas a tiempo = Nº de entregas a tiempo / Nº total de entregas realizadas x 100 
    
   ***Ojo*** <br>
    
    - Las “entregas a tiempo” excluyen a aquellas que registraron retraso.
    - Una entrega registra retraso cuando el tiempo registrado es mayor al tiempo asignado
    - Para el calculo de Nº de entregas a tiempo Y Nº total de entregas realizadas, los valores de litros y tiempos tanto asignados como registrados en el punto de distribución NO deben ser ni negativos ni cero de lo contrario el punto de distribución es ignorado en el cálculo.

Recuerde que el entregable también incluye los cambios realizados durante la etapa de pruebas y depuración. Es decir,

1. La matriz de asignación y de registro serán pasados como parámetros a la función control. Van ordenadas como [Punto Distribucion, Id Camion, Litros, Tiempo]
2. El mensaje a imprimir ahora contiene la palabra Camión, con tilde.
3. El cálculo para Tasa de entrega ha sido modificado. Debe calcularse como<br>
    Tasa Entrega = Cantidad total de litros despachados / Tiempo total de despacho
4. Debes incluir las siguientes validaciones a tu código:<br>
    a. Que los valores de litros y tiempos asignados no sean 0 o negativos.<br>
    b. Que los valores de litros y tiempos registrados no sean 0 o negativos. <br> 
  **Ojo** Si una de estas condiciones no se cumple, el valor incluido para ese punto de distribución y para ese camión deberá ser ignorado en el cálculo.

    La validación debe realizarse por fila en el siguiente orden
      1. Litros asignados
      2. Litros registrados 
      3. Tiempo de despacho asignado
      4. Tiempo de despacho registrado

Los mensajes a imprimir deben seguir la siguiente nomenclatura. Puedes ver la salida en el ejemplo que se presenta a continuación.

Error en litros asignados Punto # '<'Aqui va el id'>' Camión '<'Aqui va numero camión'>' <br>
Error en litros registrados Punto # '<'Aqui va el id'>' Camión '<'Aqui va numero camión'>' <br>
Error en tiempo de despacho asignados Punto # '<'Aqui va el id'>' Camión '<'Aqui va numero camión'>' <br>
Error en tiempo de despacho registrados Punto # '<'Aqui va el id'>' Camión '<'Aqui va numero camión'>' <br>

Eficiencia en tiempo de Despacho <br>
Para Id camión # '<'Aqui va numero camión'>' = '<'Aqui va numero calculado para ese camión'>' % <br>

Tasa de entrega<br>
Para Id camión # '<'Aqui va numero camión'>' = '<'Aqui va numero calculado para ese camión'>' <br>

Nivel de cumplimiento<br>
Para Id camión # '<'Aqui va numero camión'>' = '<'Aqui va numero calculado para ese camión'>' %

Entregas a tiempo<br>
Para Id camión # '<'Aqui va numero camión'>' = '<'Aqui va numero calculado para ese camión'>' %

## Ejemplo

1. Esta es la Orden de Despacho (que contiene las cajas asignadas, tiempos asignados e identificador del camión que hace el despacho en cada punto de distribución) emitida por LactoCaribe :

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-pb0m{border-color:inherit;text-align:center;vertical-align:bottom}
.tg .tg-6fom{background-color:#dae8fc;border-color:inherit;text-align:center;vertical-align:bottom}
.tg .tg-cey4{border-color:inherit;font-size:16px;text-align:left;vertical-align:top}
.tg .tg-g25u{background-color:#cbcefb;border-color:inherit;font-size:16px;text-align:center;vertical-align:top}
.tg .tg-udtg{border-color:inherit;color:#000000;font-size:16px;text-align:center;vertical-align:bottom}
.tg .tg-pwu9{background-color:#9698ed;border-color:inherit;font-size:16px;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-gmla{border-color:inherit;font-size:16px;text-align:center;vertical-align:top}
.tg .tg-v837{background-color:#9698ed;border-color:inherit;font-size:16px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-rgq0{border-color:inherit;font-size:16px;text-align:center;vertical-align:bottom}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-yxgd{border-color:inherit;color:#000000;font-size:16px;font-weight:bold;text-align:center;vertical-align:bottom}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-g25u" colspan="4">Asignado por LactoCaribe</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-v837">Punto de Distribución</td>
    <td class="tg-v837">ID del camión</td>
    <td class="tg-pwu9">Litros a Entregar</td>
    <td class="tg-pwu9">Tiempo de despacho<br>     (minutos)</td>
  </tr>
  <tr>
    <td class="tg-rgq0">1</td>
    <td class="tg-6fom">5</td>
    <td class="tg-udtg">1329</td>
    <td class="tg-udtg">0</td>
  </tr>
  <tr>
    <td class="tg-rgq0">2</td>
    <td class="tg-6fom">4</td>
    <td class="tg-udtg">0</td>
    <td class="tg-udtg">35</td>
  </tr>
  <tr>
    <td class="tg-rgq0">3</td>
    <td class="tg-6fom">1</td>
    <td class="tg-udtg">1462</td>
    <td class="tg-udtg">54</td>
  </tr>
  <tr>
    <td class="tg-rgq0">4</td>
    <td class="tg-6fom">3</td>
    <td class="tg-udtg">1222</td>
    <td class="tg-udtg">35</td>
  </tr>
  <tr>
    <td class="tg-rgq0">5</td>
    <td class="tg-6fom">2</td>
    <td class="tg-udtg">-111</td>
    <td class="tg-udtg">44</td>
  </tr>
  <tr>
    <td class="tg-rgq0">6</td>
    <td class="tg-6fom">3</td>
    <td class="tg-udtg">1389</td>
    <td class="tg-udtg">52</td>
  </tr>
  <tr>
    <td class="tg-rgq0">7</td>
    <td class="tg-6fom">1</td>
    <td class="tg-udtg">1500</td>
    <td class="tg-udtg">35</td>
  </tr>
  <tr>
    <td class="tg-rgq0">8</td>
    <td class="tg-6fom">1</td>
    <td class="tg-udtg">1419</td>
    <td class="tg-udtg">50</td>
  </tr>
  <tr>
    <td class="tg-rgq0">9</td>
    <td class="tg-6fom">5</td>
    <td class="tg-udtg">1355</td>
    <td class="tg-udtg">44</td>
  </tr>
  <tr>
    <td class="tg-rgq0">10</td>
    <td class="tg-6fom">4</td>
    <td class="tg-udtg">1491</td>
    <td class="tg-udtg">46</td>
  </tr>
  <tr>
    <td class="tg-rgq0">11</td>
    <td class="tg-6fom">1</td>
    <td class="tg-udtg">1427</td>
    <td class="tg-udtg">38</td>
  </tr>
  <tr>
    <td class="tg-rgq0">12</td>
    <td class="tg-6fom">4</td>
    <td class="tg-udtg">1421</td>
    <td class="tg-udtg">31</td>
  </tr>
  <tr>
    <td class="tg-rgq0">13</td>
    <td class="tg-6fom">3</td>
    <td class="tg-udtg">1259</td>
    <td class="tg-udtg">55</td>
  </tr>
  <tr>
    <td class="tg-rgq0">14</td>
    <td class="tg-6fom">5</td>
    <td class="tg-udtg">1489</td>
    <td class="tg-udtg">35</td>
  </tr>
  <tr>
    <td class="tg-rgq0">15</td>
    <td class="tg-6fom">5</td>
    <td class="tg-udtg">1417</td>
    <td class="tg-udtg">37</td>
  </tr>
  <tr>
    <td class="tg-rgq0">16</td>
    <td class="tg-6fom">1</td>
    <td class="tg-udtg">1220</td>
    <td class="tg-udtg">33</td>
  </tr>
  <tr>
    <td class="tg-rgq0">17</td>
    <td class="tg-6fom">1</td>
    <td class="tg-udtg">1291</td>
    <td class="tg-udtg">35</td>
  </tr>
  <tr>
    <td class="tg-rgq0">18</td>
    <td class="tg-6fom">2</td>
    <td class="tg-udtg">1341</td>
    <td class="tg-udtg">48</td>
  </tr>
  <tr>
    <td class="tg-rgq0">19</td>
    <td class="tg-6fom">4</td>
    <td class="tg-udtg">1386</td>
    <td class="tg-udtg">54</td>
  </tr>
  <tr>
    <td class="tg-rgq0">20</td>
    <td class="tg-6fom">3</td>
    <td class="tg-udtg">1467</td>
    <td class="tg-udtg">34</td>
  </tr>
  <tr>
    <td class="tg-gmla">21</td>
    <td class="tg-6fom">1</td>
    <td class="tg-pb0m">1429</td>
    <td class="tg-pb0m">42</td>
  </tr>
  <tr>
    <td class="tg-gmla">22</td>
    <td class="tg-6fom">5</td>
    <td class="tg-pb0m">1232</td>
    <td class="tg-pb0m">32</td>
  </tr>
  <tr>
    <td class="tg-gmla">23</td>
    <td class="tg-6fom">3</td>
    <td class="tg-pb0m">1343</td>
    <td class="tg-pb0m">54</td>
  </tr>
  <tr>
    <td class="tg-gmla">24</td>
    <td class="tg-6fom">1</td>
    <td class="tg-pb0m">1426</td>
    <td class="tg-pb0m">33</td>
  </tr>
  <tr>
    <td class="tg-gmla">25</td>
    <td class="tg-6fom">4</td>
    <td class="tg-pb0m">1332</td>
    <td class="tg-pb0m">36</td>
  </tr>
  <tr>
    <td class="tg-gmla">26</td>
    <td class="tg-6fom">4</td>
    <td class="tg-pb0m">1494</td>
    <td class="tg-pb0m">40</td>
  </tr>
  <tr>
    <td class="tg-gmla">27</td>
    <td class="tg-6fom">3</td>
    <td class="tg-pb0m">1280</td>
    <td class="tg-pb0m">39</td>
  </tr>
  <tr>
    <td class="tg-gmla">28</td>
    <td class="tg-6fom">1</td>
    <td class="tg-pb0m">1374</td>
    <td class="tg-pb0m">36</td>
  </tr>
  <tr>
    <td class="tg-gmla">29</td>
    <td class="tg-6fom">2</td>
    <td class="tg-pb0m">1376</td>
    <td class="tg-pb0m">48</td>
  </tr>
  <tr>
    <td class="tg-gmla">30</td>
    <td class="tg-6fom">4</td>
    <td class="tg-pb0m">1349</td>
    <td class="tg-pb0m">50</td>
  </tr>
  <tr>
    <td class="tg-cey4">Total</td>
    <td class="tg-0pky"></td>
    <td class="tg-yxgd">41351</td>
    <td class="tg-yxgd">1253</td>
  </tr>
</tbody>
</table>

2. Si al consignar los valores en la plantilla de los registros del conductor obtenemos este resultado:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-6fom{background-color:#dae8fc;border-color:inherit;text-align:center;vertical-align:bottom}
.tg .tg-cey4{border-color:inherit;font-size:16px;text-align:left;vertical-align:top}
.tg .tg-19ba{border-color:inherit;color:#000000;font-size:16px;text-align:left;vertical-align:bottom}
.tg .tg-g25u{background-color:#cbcefb;border-color:inherit;font-size:16px;text-align:center;vertical-align:top}
.tg .tg-yrit{border-color:inherit;color:#000000;font-size:16px;font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-pwu9{background-color:#9698ed;border-color:inherit;font-size:16px;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-gmla{border-color:inherit;font-size:16px;text-align:center;vertical-align:top}
.tg .tg-v837{background-color:#9698ed;border-color:inherit;font-size:16px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-rgq0{border-color:inherit;font-size:16px;text-align:center;vertical-align:bottom}
.tg .tg-za14{border-color:inherit;text-align:left;vertical-align:bottom}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-g25u" colspan="4">Registrado por cada Camión</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-v837">Punto de Distribución</td>
    <td class="tg-v837">ID del camión</td>
    <td class="tg-pwu9">Litros a Entregar</td>
    <td class="tg-pwu9">Tiempo de   despacho<br>     (minutos)</td>
  </tr>
  <tr>
    <td class="tg-rgq0">1</td>
    <td class="tg-6fom">5</td>
    <td class="tg-19ba">1168</td>
    <td class="tg-19ba">52</td>
  </tr>
  <tr>
    <td class="tg-rgq0">2</td>
    <td class="tg-6fom">4</td>
    <td class="tg-19ba">1224</td>
    <td class="tg-19ba">51</td>
  </tr>
  <tr>
    <td class="tg-rgq0">3</td>
    <td class="tg-6fom">1</td>
    <td class="tg-19ba">1379</td>
    <td class="tg-19ba">33</td>
  </tr>
  <tr>
    <td class="tg-rgq0">4</td>
    <td class="tg-6fom">3</td>
    <td class="tg-19ba">1281</td>
    <td class="tg-19ba">52</td>
  </tr>
  <tr>
    <td class="tg-rgq0">5</td>
    <td class="tg-6fom">2</td>
    <td class="tg-19ba">1200</td>
    <td class="tg-19ba">38</td>
  </tr>
  <tr>
    <td class="tg-rgq0">6</td>
    <td class="tg-6fom">3</td>
    <td class="tg-19ba">1320</td>
    <td class="tg-19ba">34</td>
  </tr>
  <tr>
    <td class="tg-rgq0">7</td>
    <td class="tg-6fom">1</td>
    <td class="tg-19ba">1225</td>
    <td class="tg-19ba">52</td>
  </tr>
  <tr>
    <td class="tg-rgq0">8</td>
    <td class="tg-6fom">1</td>
    <td class="tg-19ba">1149</td>
    <td class="tg-19ba">51</td>
  </tr>
  <tr>
    <td class="tg-rgq0">9</td>
    <td class="tg-6fom">5</td>
    <td class="tg-19ba">1424</td>
    <td class="tg-19ba">34</td>
  </tr>
  <tr>
    <td class="tg-rgq0">10</td>
    <td class="tg-6fom">4</td>
    <td class="tg-19ba">0</td>
    <td class="tg-19ba">36</td>
  </tr>
  <tr>
    <td class="tg-rgq0">11</td>
    <td class="tg-6fom">1</td>
    <td class="tg-19ba">1205</td>
    <td class="tg-19ba">0</td>
  </tr>
  <tr>
    <td class="tg-rgq0">12</td>
    <td class="tg-6fom">4</td>
    <td class="tg-19ba">1297</td>
    <td class="tg-19ba">-37</td>
  </tr>
  <tr>
    <td class="tg-rgq0">13</td>
    <td class="tg-6fom">3</td>
    <td class="tg-19ba">1357</td>
    <td class="tg-19ba">49</td>
  </tr>
  <tr>
    <td class="tg-rgq0">14</td>
    <td class="tg-6fom">5</td>
    <td class="tg-19ba">1227</td>
    <td class="tg-19ba">36</td>
  </tr>
  <tr>
    <td class="tg-rgq0">15</td>
    <td class="tg-6fom">5</td>
    <td class="tg-19ba">1263</td>
    <td class="tg-19ba">46</td>
  </tr>
  <tr>
    <td class="tg-rgq0">16</td>
    <td class="tg-6fom">1</td>
    <td class="tg-19ba">1123</td>
    <td class="tg-19ba">33</td>
  </tr>
  <tr>
    <td class="tg-rgq0">17</td>
    <td class="tg-6fom">1</td>
    <td class="tg-19ba">1137</td>
    <td class="tg-19ba">30</td>
  </tr>
  <tr>
    <td class="tg-rgq0">18</td>
    <td class="tg-6fom">2</td>
    <td class="tg-19ba">1374</td>
    <td class="tg-19ba">37</td>
  </tr>
  <tr>
    <td class="tg-rgq0">19</td>
    <td class="tg-6fom">4</td>
    <td class="tg-19ba">1229</td>
    <td class="tg-19ba">33</td>
  </tr>
  <tr>
    <td class="tg-rgq0">20</td>
    <td class="tg-6fom">3</td>
    <td class="tg-19ba">1437</td>
    <td class="tg-19ba">31</td>
  </tr>
  <tr>
    <td class="tg-gmla">21</td>
    <td class="tg-6fom">1</td>
    <td class="tg-za14">1290</td>
    <td class="tg-za14">48</td>
  </tr>
  <tr>
    <td class="tg-gmla">22</td>
    <td class="tg-6fom">5</td>
    <td class="tg-za14">1259</td>
    <td class="tg-za14">48</td>
  </tr>
  <tr>
    <td class="tg-gmla">23</td>
    <td class="tg-6fom">3</td>
    <td class="tg-za14">1435</td>
    <td class="tg-za14">30</td>
  </tr>
  <tr>
    <td class="tg-gmla">24</td>
    <td class="tg-6fom">1</td>
    <td class="tg-za14">1104</td>
    <td class="tg-za14">40</td>
  </tr>
  <tr>
    <td class="tg-gmla">25</td>
    <td class="tg-6fom">4</td>
    <td class="tg-za14">1387</td>
    <td class="tg-za14">43</td>
  </tr>
  <tr>
    <td class="tg-gmla">26</td>
    <td class="tg-6fom">4</td>
    <td class="tg-za14">1377</td>
    <td class="tg-za14">55</td>
  </tr>
  <tr>
    <td class="tg-gmla">27</td>
    <td class="tg-6fom">3</td>
    <td class="tg-za14">1294</td>
    <td class="tg-za14">54</td>
  </tr>
  <tr>
    <td class="tg-gmla">28</td>
    <td class="tg-6fom">1</td>
    <td class="tg-za14">1338</td>
    <td class="tg-za14">51</td>
  </tr>
  <tr>
    <td class="tg-gmla">29</td>
    <td class="tg-6fom">2</td>
    <td class="tg-za14">1387</td>
    <td class="tg-za14">47</td>
  </tr>
  <tr>
    <td class="tg-gmla">30</td>
    <td class="tg-6fom">4</td>
    <td class="tg-za14">1208</td>
    <td class="tg-za14">34</td>
  </tr>
  <tr>
    <td class="tg-cey4">Total</td>
    <td class="tg-0pky"></td>
    <td class="tg-yrit">38535</td>
    <td class="tg-yrit">1257</td>
  </tr>
</tbody>
</table>

3. La salida esperada es la siguiente:

Error en tiempo de despacho asignados Punto # 1 Camión 5<br>
Error en litros asignados Punto # 2 Camión 4 <br>
Error en litros asignados Punto # 5 Camión 2 <br>
Error en litros registrados Punto # 10 Camión 4 <br>
Error en tiempo de despacho registrados Punto # 11 Camión 1 <br>
Error en tiempo de despacho registrados Punto # 12 Camión 4<br>
<br>
Eficiencia en tiempo de Despacho <br>
Para Id camión # 1 = -6.3 %<br>
Para Id camión # 2 = 12.9 % <br>
Para Id camión # 3 = 7.1 % <br>
Para Id camión # 4 = 3.4 % <br>
Para Id camión # 5 = -10.8 % <br>
<br>
Tasa de entrega <br>
Para Id camión # 1 = 32.4<br>
Para Id camión # 2 = 22.6 <br>
Para Id camión # 3 = 32.5<br>
Para Id camión # 4 = 25.8<br>
Para Id camión # 5 = 38.7<br>

Nivel de cumplimiento<br>
Para Id camión # 1 = 87.3 %<br>
Para Id camión # 2 = 101.6 %<br>
Para Id camión # 3 = 102.1 %<br>
Para Id camión # 4 = 93.1 %<br>
Para Id camión # 5 = 92.9 %<br>

Entregas a tiempo<br>
Para Id camión # 1 = 37.5 %<br>
Para Id camión # 2 = 100.0 %<br>
Para Id camión # 3 = 66.7 %<br>
Para Id camión # 4 = 50.0 %<br>
Para Id camión # 5 = 25.0 %<br>

### Recomendaciones:

1. Mantener el formato de la "salida esperada" (orden, palabras y signos). Para ello se recomienda copiar y pegar del ejemplo. 
2. La plataforma discrimina por espacios y mayúsculas.
3. La salida esperada debe truncarse a una cifra significativa. Para redondear numeros reales puedes usar la función round(), de la siguiente manera :
   round(1.539, 1) --->   1.5