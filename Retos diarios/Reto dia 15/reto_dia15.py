def reto1(t,y):
  matriz=[]
  if len(t) == len(y) and len(t[0]) == len(y[0]):
    for i in range(len(t)):
      m=[]
      for j in range(len(t[0])):
        suma=0
        suma = t[i][j]+y[i][j]
        m.append(suma)
      matriz.append(m)
    print(matriz)    
  else:
    print("Error en los datos")  
#No modifiques esta parte! 
if __name__ == "__main__":
    reto1([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1],[3,3,3],[2,2,2]])

def crearMatriz(n):
  matriz=[]
  for i in range(n):
    m=[]
    for j in range(n):
      num= int(input("Ingrese un nunmero"))
      m.append(num)
    matriz.append(m)  
  return matriz 

def validarMatriz(t):
  contFila=0
  contCol=0
  sumaD1=0
  sumaD2=0
  for i in range(len(t)):
    sumaF=0
    sumaC=0
    sumaD1+=t[i][i]
    sumaD2+=t[i][2-i]
    for j in range(len(t[0])):
      sumaF+=t[i][j]
      sumaC+=t[j][i]

    if i == 0:
      numIgual = sumaF
      contFila+=1
      contCol+=1
    else:
      if sumaF == numIgual:
        contFila+=1
      if sumaC == numIgual:
        contCol+=1
  if sumaD2 == numIgual:
      contDia=True

     
  if contFila == len(t) and contCol == len(t) and contDia==True:
    print(numIgual)
  else:
    print(False)  

def reto2(n):
  numero = int(input("Ingrese un numero: "))
  print(crearMatriz(numero))
  validarMatriz([[8,1,6],[3,5,7],[4,9,2]])

#No modifiques esta parte! 
if __name__ == "__main__":
    reto2(3)
