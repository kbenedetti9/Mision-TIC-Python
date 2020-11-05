def reto1(nota):
   if nota >= 0 and nota <= 59:
     result = 'F'
   elif nota >= 60 and nota <= 69:
     result = 'D'
   elif nota >= 70 and nota <= 79:
     result = 'C'
   elif nota >= 80 and nota <= 89:
     result = 'B'
   elif nota >= 90 and nota <= 100:
     result = 'A'    
    
   return result

reto1(64)

def reto2(indice):
    if indice >= 0 and indice <= 50:
      result = 'buena'
    elif indice >= 51 and indice <=  100:
      result = 'regular'
    elif indice >= 101 and indice <= 150:
      result = 'mala'
    elif indice >= 151 and indice <= 200:
      result = 'muy mala'
    else:
      result = 'extremadamente mala'
    
    return result

reto2(65) 

def reto3(nombre1, nombre2):
   
    if nombre1 < nombre2:
      result = nombre1
    else:
      result = nombre2
    
    return result
    
reto3("Pedro", "Ana") 