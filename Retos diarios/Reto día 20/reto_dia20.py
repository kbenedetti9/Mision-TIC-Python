def control(asignado,registrado):
 
  for k in range(30):
    if asignado[k][2]<=0:
      print("Error en litros asignados Punto # {} Camión {}".format(k+1,asignado[k][1]))
    if registrado[k][2]<=0:
      print("Error en litros registrados Punto # {} Camión {}".format(k+1,registrado[k][1]))
    if asignado[k][3]<=0:
      print("Error en tiempo de despacho asignados Punto # {} Camión {}".format(k+1,asignado[k][1]))
    if registrado[k][3]<=0:
      print("Error en tiempo de despacho registrados Punto # {} Camión {}".format(k+1,registrado[k][1]))    


  for i in range(1,6):
    litrosA=0
    tiemposA=0
    litrosR=0
    tiemposR=0
    eficiencia=0
    tasaEntrega=0
    nivelCumplimiento=0
    
    for j in range(0,30):
        sumarLitros = False
        sumarTiempos = False
        if asignado[j][2]>0 and registrado[j][2]>0:
          sumarLitros = True
        if asignado[j][3]>0 and registrado[j][3]>0:
          sumarTiempos = True  

        if asignado[j][1] == i:
          id = asignado[j][1]
          if sumarLitros == True:
            litrosA += asignado[j][2]
          if sumarTiempos == True:  
            tiemposA += asignado[j][3]
        if registrado[j][1] == i:
          if sumarLitros == True:  
            litrosR += registrado[j][2]
          if sumarTiempos == True:  
            tiemposR += registrado[j][3]

    eficiencia = round((tiemposA-tiemposR)/tiemposA*100,1)
    tasaEntrega = round(litrosR/tiemposR,1)
    nivelCumplimiento = round(litrosR/litrosA*100,1)
    if i == 1:
      eficiencia1 = eficiencia
      tasaEntrega1= tasaEntrega
      nivelCumplimiento1 = nivelCumplimiento
      
    elif i==2:
      eficiencia2 = eficiencia
      tasaEntrega2= tasaEntrega
      nivelCumplimiento2 = nivelCumplimiento
    elif i ==3:
      eficiencia3 = eficiencia
      tasaEntrega3 = tasaEntrega
      nivelCumplimiento3 = nivelCumplimiento
    elif i==4:
      eficiencia4 = eficiencia
      tasaEntrega4= tasaEntrega
      nivelCumplimiento4 = nivelCumplimiento
    else:
      eficiencia5 = eficiencia   
      tasaEntrega5= tasaEntrega
      nivelCumplimiento5 = nivelCumplimiento        
    
  print("Eficiencia en tiempo de despacho")
  print("Para Id camión # 1 = {0} %".format(eficiencia1))
  print("Para Id camión # 2 = {0} %".format(eficiencia2))
  print("Para Id camión # 3 = {0} %".format(eficiencia3))
  print("Para Id camión # 4 = {0} %".format(eficiencia4))
  print("Para Id camión # 5 = {0} %".format(eficiencia5))
  print("Tasa de entrega")
  print("Para Id camión # 1 = {0}".format(tasaEntrega1))
  print("Para Id camión # 2 = {0}".format(tasaEntrega2))
  print("Para Id camión # 3 = {0}".format(tasaEntrega3))
  print("Para Id camión # 4 = {0}".format(tasaEntrega4))
  print("Para Id camión # 5 = {0}".format(tasaEntrega5))
  print("Nivel de cumplimiento")
  print("Para Id camión # 1 = {0} %".format(nivelCumplimiento1))
  print("Para Id camión # 2 = {0} %".format(nivelCumplimiento2))
  print("Para Id camión # 3 = {0} %".format(nivelCumplimiento3))
  print("Para Id camión # 4 = {0} %".format(nivelCumplimiento4))
  print("Para Id camión # 5 = {0} %".format(nivelCumplimiento5))

#No modifiques esta parte! 
if __name__ == "__main__":
    control([[1,5,1329,0], [2,4,0,35], [3,1,1462,54], [4,3,1222,35], [5,2,-111,44],[6,3,1389,52], [7,1,1500,35], [8,1,1419,50], [9,5,1355,44],[10,4,1491,46],[11,1,1427,38],[12,4,1421,31], [13,3,1259,55], [14,5,1489,35], [15,5,1417,37], [16,1,1220,33], [17,1,1291,35], [18,2,1341,48], [19,4,1386,54], [20,3,1467,34], [21,1,1429,42],[22,5,1232,32], [23,3,1343,54], [24,1,1426,33], [25,4,1332,36], [26,4,1494,40], [27,3,1280,39], [28,1,1374,36], [29,2,1376,48], [30,4,1349,50]],[[1,5,1168,52], [2,4,1224,51], [3,1,1379,33], [4,3,1281,52], [5,2,1200,38], [6,3,1320,34], [7,1,1225,52], [8,1,1149,51], [9,5,1424,34], [10,4,0,36], [11,1,1205,0], [12,4,1297,-37],[13,3,1357,49], [14,5,1227,36],[15,5,1263,46], [16,1,1123,33], [17,1,1137,30], [18,2,1374,37], [19,4,1229,33], [20,3,1437,31], [21,1,1290,48], [22,5,1259,48], [23,3,1435,30],[24,1,1104,40], [25,4,1387,43], [26,4,1377,55], [27,3,1294,54], [28,1,1338,51],[29,2,1387,47], [30,4,1208,34]]) #No comentar ni borrar el llamado de la función 