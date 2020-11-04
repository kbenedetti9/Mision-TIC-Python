def control():
  matrizResultado = []
  sobreEntregas=[]
  demoras=[]
  masEntregas=[]
  masDemoras=[]
  deficientes=[]
  num = 0 
  orden =[[1,98,11],[2,86,14],[3,99,11],[4,89,12],[5,89,12],[6,96,10],[7,93,13],
          [8,87,15],[9,89,10],[10,92,10],[11,99,15],[12,90,12],[13,87,15],[14,96,12],
          [15,92,15],[16,85,10],[17,86,10],[18,97,14],[19,90,14],[20,98,12]]
  registro = [[1,100,10],[2,86,10],[3,97,15],[4,93,15],[5,94,12],[6,93,13],[7,95,12],
              [8,85,11],[9,90,11],[10,90,12],[11,85,12],[12,89,12],[13,85,12],[14,93,11],
              [15,89,10],[16,89,14],[17,93,13],[18,99,11],[19,93,13],[20,99,11]]
  for i in range(20):
    m=[]
    punto = "Punto # {0}".format(i+1)
    puntoN = "Punto {0}".format(i+1)
    m.append(punto)
    cajasEntregadas = orden[i][1]-registro[i][1]
    m.append(cajasEntregadas)
    if cajasEntregadas<0:
      sobreEntrega=[]
      sobreEntrega.append(puntoN)
      sobreEntrega.append(cajasEntregadas)
      sobreEntregas.append(sobreEntrega) 
    tiempo = orden[i][2]-registro[i][2]
    m.append(tiempo)
    if tiempo<0:
      demora=[]
      demora.append(puntoN)
      demora.append(tiempo)
      demoras.append(demora) 
    tiempo = orden[i][2]-registro[i][2]
    print("{0}".format(punto))
    print("Diferencia de cajas = {0}".format(cajasEntregadas))
    print("Diferencia de tiempos = {0}".format(tiempo))
    porcentaje = round((100*registro[i][2])/orden[i][2],1)
    eficiencia = round(100-porcentaje,1)
    print("Eficiencia = {0}%".format(eficiencia))
    matrizResultado.append(m)
  
  for l in range(len(demoras)):
    for m in range(len(sobreEntregas)):
      if demoras[l][0] == sobreEntregas[m][0]:
        deficientes.append(demoras[l][0])

  for k in range(3):
    mayorDemora=100
    for i in range(len(demoras)):  
      if demoras[i][1] < mayorDemora:
        mayorDemora = demoras[i][1]
        puntoMasDemora = demoras[i][0]
        nume =i
    demoras.pop(nume)
    masDemoras.append("{0}:{1}".format(puntoMasDemora,mayorDemora))
  print("Los puntos con mayores demoras de tiempo = [{0},{1},{2}]".format(masDemoras[0],masDemoras[1],masDemoras[2]))

  for k in range(3):
    mayorEntrega=100
    for i in range(len(sobreEntregas)):  
      if sobreEntregas[i][1] < mayorEntrega:
        mayorEntrega = sobreEntregas[i][1]
        puntoMasEntrega = sobreEntregas[i][0]
        num =i
    sobreEntregas.pop(num)
    masEntregas.append("{0}:{1}".format(puntoMasEntrega,mayorEntrega))    
  print("Los puntos con mayores sobre-entregas = [{0},{1},{2}]".format(masEntregas[0],masEntregas[1],masEntregas[2]))
    
  print("Los puntos donde pasan ambas = {0},{1},{2},{3}".format(deficientes[0],deficientes[1],deficientes[2],deficientes[3]))

control()