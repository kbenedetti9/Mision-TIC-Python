def reto1(palabra):

  cantidad = len(palabra)
  i = 0
  correcto = 0
  num = cantidad
  while i<cantidad:
    num-=1
    if palabra[num] == palabra[i]:
      correcto+=1
    i+=1

  if correcto == cantidad:
    result = True
  else: 
    result = False  
 
  print(result) # Modifica el codigo para imprimir cada valor

reto1("ojo")    

def reto2(numero):
    
  num = str(numero)
  cantidad = len(num)
    
  while cantidad != 1:
    i = 0
    suma = 0
    while i<cantidad:
      suma += int(num[i])
      i+=1
    cantidad = len(str(suma))    
    num = str(suma)

  return suma

reto2(347)  

def reto3(numero):

  i = 1
  contador = 0 
  if numero <= 1:
    result = "Error en el numero"
  else:
    while i<=numero:
      if numero % i == 0:
        contador+=1
      i+=1  
  if contador == 2:
    result = True
  else:
    result = False         
  
  return result

reto3(89)  

