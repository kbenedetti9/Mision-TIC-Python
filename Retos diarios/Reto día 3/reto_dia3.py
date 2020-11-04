def reto1(edadJuan, edadPedro,nietos):
   sum = edadJuan + edadPedro
   if (edadJuan>35 or edadPedro<50) and sum%2==0 and nietos>=1:
     result = 'SI'
   else:
     result = 'NO'# Escribe tu código aquí. Manten la indentación!!
    
   return result # Reemplaza 0 por la variable que tiene el resultado

reto1(36, 45, 2)

def reto2(factorProyecto, factorEquipo):
    sum = factorEquipo + factorProyecto
    porcentaje = sum/100
    porcentaje60 = 50*0.6
    if porcentaje > porcentaje60 and factorProyecto>=12 and factorEquipo>=12:
      result = 0.05
    else:
      result = 0.025
   
    return result

reto2(12,12) 

def reto3(x):
    if (x>=1) and (x<=100):
      if x%2 == 0:
        result = "par"
      else:    
        result = "impar"
    
    return result
reto3(5) 