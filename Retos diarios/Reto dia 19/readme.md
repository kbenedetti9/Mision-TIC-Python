## RETO SEMANA 4

LactoCaribe Ltda. es otro cliente de Transportes del Norte, cuya operación demanda 5 de sus camiones. A diferencia de Frigoaves, LactoCaribe distribuye carga a granel (leche) a sus 30 puntos de distribución.

Ellos se encuentran interesados en medir la eficiencia de cada uno de los 5 camiones, por lo que les ha atraído implementar el sistema que desarrollaste durante Semana 3, acondicionando la “eficiencia en los tiempos de despacho” para cada camión:

1. Eficiencia en tiempos de despacho = (Tiempo total de despacho asignado - Tiempo total de despacho registrado) / Tiempo de total despacho asignado x 100
2. Tasa de entrega (Lt/min) = Cantidad total de litros despachados / Tiempo total de despacho x 100
3. Nivel de Cumplimiento de los despachos = Total de Litros despachados / Total de litros asignados x 100

Desarrolla un programa que calcule y muestre los 3 indicadores de desempeño anteriores.

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
    <td class="tg-pwu9">Tiempo de   despacho<br>     (minutos)</td>
  </tr>
  <tr>
    <td class="tg-rgq0">1</td>
    <td class="tg-6fom">5</td>
    <td class="tg-udtg">1329</td>
    <td class="tg-udtg">48</td>
  </tr>
  <tr>
    <td class="tg-rgq0">2</td>
    <td class="tg-6fom">4</td>
    <td class="tg-udtg">1386</td>
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
    <td class="tg-udtg">1445</td>
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
    <td class="tg-19ba">1437</td>
    <td class="tg-19ba">36</td>
  </tr>
  <tr>
    <td class="tg-rgq0">11</td>
    <td class="tg-6fom">1</td>
    <td class="tg-19ba">1205</td>
    <td class="tg-19ba">42</td>
  </tr>
  <tr>
    <td class="tg-rgq0">12</td>
    <td class="tg-6fom">4</td>
    <td class="tg-19ba">1297</td>
    <td class="tg-19ba">37</td>
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

<p>Eficiencia en tiempos de despacho</p>
<p>Para Id # 1 = -6.7 %</p> 
<p>Para Id # 2 = 12.9 %</p>
<p>Para Id # 3 = 7.1 %</p>
<p>Para Id # 4 = 1.0 %</p>
<p>Para Id # 5 = -10.2 %</p>

<p>Tasa de entrega</p>
<p>Para Id # 1 = 2881.6 %</p>
<p>Para Id # 2 = 3246.7 %</p>
<p>Para Id # 3 = 3249.6 %</p>
<p>Para Id # 4 = 3169.2 %</p>
<p>Para Id # 5 = 2935.6 %</p>

<p>Nivel de cumplimiento</p>
<p>Para Id # 1 = 87.3 %</p>
<p>Para Id # 2 = 95.2 %</p>
<p>Para Id # 3 = 102.1 %</p>
<p>Para Id # 4 = 92.9 %</p>
<p>Para Id # 5 = 92.9 %</p>

### Recomendaciones:

1. Mantener el formato de la "salida esperada" (orden, palabras y signos). Para ello se recomienda copiar y pegar del ejemplo. 
2. La plataforma discrimina por espacios y mayúsculas.
3. La salida esperada debe truncarse a una cifra significativa. Para redondear numeros reales puedes usar la función round(), de la siguiente manera :
   round(1.539, 1) --->   1.5