def reto1(x,y):
  menor=[]
  if len(x) == len(y):
    for i in range(len(x)):
      if x[i]<= y[i]:
        menor.append(x[i])
      else:
        menor.append(y[i])
    print(menor)        
  else:
    print("Error en los datos")

#No modifiques esta parte! 
if __name__ == "__main__":
    reto1([1,2,3], [3,3,3])

def reto2(x,y):
  diferentes=[]
  for i in x:
    if i not in y:
      diferentes.append(i)
  for j in y:
    if j not in x:
      diferentes.append(j)
  print(diferentes)        


#No modifiques esta parte! 
if __name__ == "__main__":
    reto2([1,5],[2,3,4,5,6,7])
