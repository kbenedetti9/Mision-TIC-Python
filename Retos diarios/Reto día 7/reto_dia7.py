def reto1(numero):
   
   multiplica = 1

   while multiplica <= 12:
     print(numero * multiplica)
     multiplica+=1

reto1(3)    

def reto2(numero):
   
  factorial = 1
  resultado = 1
  while factorial < numero:
     resultado = resultado *(factorial+1)
     factorial += 1

  print(resultado) 

reto2(4) 

def reto3(valor, vidas):
    result = 0
    div = vidas
    while vidas>0:
      result = result + valor
      valor-=1
      vidas-=1
    result = result/div
    if result % 2 == 0:
      juego = "Gana"
    else:
      juego = "Pierde"
      
    print(juego)

reto3(27,4) 