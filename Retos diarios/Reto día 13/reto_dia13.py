def mayor(x):
  x = sorted(x,reverse= True)
  cantidad = len(x)
  num = x[0]
  veces = 0
  
  for i in range(0,cantidad):
    
    if x[i] == num:
      veces+=1
  print("{0}".format(num))   
  print("{0}".format(veces)) 

def reto1():
  lista = []
  n = int(input("Ingrese el numero de elementos "))   
  for i in range(0,n):
    l = int(input("Ingrese el elemento: "))  
    lista.append(l)
  mayor(lista)

#No modifiques esta parte! 
if __name__ == "__main__":
    reto1()  
    mayor([23,43,43,9,43])

def reto2(x,y,z):
  lista = []
  for i in range(x):
    lista.append(y)
    y = y + z
  print(lista) 
#No modifiques esta parte! 
if __name__ == "__main__":
    reto2(3,11,7)  