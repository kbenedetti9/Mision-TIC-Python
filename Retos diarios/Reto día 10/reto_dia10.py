def reto1(frase1, frase2):
  frase1 = frase1.lower().replace(" ","")
  frase2 = frase2.lower().replace(" ","")
  conteo = 0
  for i in frase1:
    for j in frase2:
      if i == j:
        frase2 = frase2.replace(i,"") 
        conteo+=1
        break
  return (conteo)

reto1("Mi prueba","Tres valores")    

def reto2(numero):
  for i in range(1,numero+1):
    for j in range(1,i+1):
      print(i,end="")
    print()    
         
reto2(7)   