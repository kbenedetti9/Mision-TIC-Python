def reto1(t):
  pares = 0
  impares = 0
  for i in range(len(t)):
    for j in range(len(t[i])):
      if t[i][j] % 2 == 0:
        pares+=t[i][j]
      else:
        impares+=t[i][j]  
  print(pares)
  print(impares)

#No modifiques esta parte! 
if __name__ == "__main__":
    reto1([[1,2,3],[4,5,6],[7,8,9]])
 
def reto2(x):
  matriz=[]
  letras=' '
      
  for i in x:
    if i != 'E' and i != 'B' and i != 'R' and i != 'M' and i != 'P' and i != 'N':
      print("Error en los datos")
    else:
      for j in x:
        if j==i:
          diferente=0
          for k in range(len(letras)):
            if j != letras[k]:
              diferente+=1
          if diferente == len(letras): 
            m=[]  
            letras+=i
            veces = x.count(j)
            m.append(j)
            m.append(veces)
            matriz.append(m)
  print(matriz)

#No modifiques esta parte! 
if __name__ == "__main__":
    reto2(["E","R","B","B","B","M","E","E","R"])