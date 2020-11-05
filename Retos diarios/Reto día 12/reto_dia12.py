def promedio(x):
  resultado = 0
  cantidad = len(x)
  for i in x:
    resultado+=i
  resultado = resultado/cantidad
  return resultado  

def reto1(l):
  pares=0
  impares=0
  
  for i in l:
    if i%2==0:
      pares+=i
    else:
      impares+=i  
  print("Promedio {0} Suma pares {1} Suma impares {2}".format(promedio(l),pares,impares))

reto1([1,2,3,4,5,6,7])  

def reto2(x,y):
  num = y.count(x)
  if num !=0:
    i = y.index(x) 
    return i
  else:
    return False  
reto2(1, [0,2,3,4,5,6,7])

def reto3(a,b):
 
  for i in a:
    encuentra = b.count(i)
    if encuentra == 0:
      b.append(i)
  b = sorted(b)
  return b

reto3([4,6,7,6,3],[6,1,2])