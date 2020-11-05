def reto1(a,b,c):
  resultado = 0
  s = a+b
  if s<=c:
    for i in range(s,c+1):
      resultado += i
  else:
    resultado = 1
    for i in range(c,s+1):
      resultado *=i
  return resultado

reto1(7,3,7)  

def primo(x):
  contador = 0
  for i in range(1,x+1):
    if x%i == 0:
      contador+=1
  if contador == 2:
    resultado = True
  else:
    resultado = False
  return resultado   

def reto2(x):
  for i in range(1,x+1):
    if primo(i):
      print(i)

reto2(11)   