import csv

def control(asignacionfile,registrofile):
  litrosA=0
  tiemposA=0
  litrosR=0
  tiemposR=0
  tiemposAsignados=[]
  tiemposRegistrados=[]
  numEntregaATiempo=0
   
  with open(asignacionfile, mode='r',encoding='utf-8') as asignado, open (registrofile, mode='r', encoding='utf-8' ) as registrado: 
    infoAsignacion = csv.reader(asignado,delimiter=",")
    infoRegistro = csv.reader(registrado,delimiter=",")

    cliente = int(input('Ingrese el cliente a buscar [1]LactoCaribe [2]FrigoAves: '))
    camion = input('Camión a buscar [1-5]: ')

    if cliente == 1:
      cliente = "Lactocaribe"
    else:
      cliente = "Frigoaves"  

    for fila in infoAsignacion:
      if fila[0] == cliente and fila[2] == camion:
        litrosA += int(fila[3])
        tiemposA += int(fila[4])
        tiemposAsignados.append(int(fila[4]))

    for fila in infoRegistro:
      if fila[0] == cliente and fila[2] == camion:
        litrosR += int(fila[3])
        tiemposR += int(fila[4])
        tiemposRegistrados.append(int(fila[4]))   

    for i in range(len(tiemposAsignados)):
      if tiemposAsignados[i]>=tiemposRegistrados[i]:
        numEntregaATiempo+=1


    eficiencia = round((tiemposA-tiemposR)/tiemposA*100,1)
    tasaEntrega = round(litrosR/tiemposR,1)
    nivelCumplimiento = round(litrosR/litrosA*100,1)
    entregasATiempo = round(numEntregaATiempo/len(tiemposAsignados)*100,1)

    print("Eficiencia en tiempo de despacho = {0} %".format(eficiencia))    
    print("Tasa de entrega = {0}".format(tasaEntrega))  
    print("Nivel de cumplimiento = {0}%".format(nivelCumplimiento)) 
    print("Entregas a tiempo = {0}%".format(entregasATiempo)) 
    
#No modifiques esta parte!
#La función control recibe dos parametros de entrada control(matrizasig, matrizregis)
if __name__ == "__main__":
    control('C1-S5 Valores Asignados.csv','C1-S5 Valores Registrados.csv')