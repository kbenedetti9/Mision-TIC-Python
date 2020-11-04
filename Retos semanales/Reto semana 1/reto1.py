def menu(option,num1,num2):
   opciones = {
       1: op1(num1),
       2: op2(num1,num2),
       3: op3(num1),
       4: op4()
   }

   resultado = opciones.get(option)
   return resultado

def op1(num1):
  numero = str(num1)
  cantidad= len(numero)    
  if cantidad == 4:
    if numero[0] >= numero[1] and numero[0] >= numero[2] and numero[0] >= numero[3]:
        mayor = numero[0]
    elif numero[1] >= numero[0] and numero[1] >= numero[2] and numero[1] >= numero[3]:
        mayor = numero[1]
    elif numero[2] >= numero[0] and numero[2] >= numero[1] and numero[2] >= numero[3]:
        mayor = numero[2]
    else:
        mayor = numero[3]
  else:
    return("numero incorrecto")
  numResult = int(mayor)     
  if numResult % 2 == 0:
    return (numResult,"par")
  else:
    return (numResult,"impar")    

def op2(num1, num2): 
  numero1 = str(num1)
  cantidad1= len(numero1)
  numero2 = str(num2)
  cantidad2 = len(numero2)
  if cantidad1 == 3 and cantidad2 == 3:
    if numero1[0] >= numero1[1] and numero1[0] >= numero1[2]:
      mayor = numero1[0]
    elif numero1[1] >= numero1[0] and numero1[1] >= numero1[2]:
      mayor = numero1[1]  
    else:
      mayor = numero1[2]   

    if numero2[0] <= numero2[1] and numero2[0] <= numero2[2]:
      menor = numero2[0] 
    elif numero2[1] <= numero2[0] and numero2[1] <= numero2[2]:
      menor = numero2[1]
    else:
      menor = numero2[2]  
    nuevoNum = mayor + menor
    result = int(nuevoNum)
    return result
  else:
    return ("numeros incorrectos")

def op3(num1):
  numero = str(num1)
  cantidad= len(numero)
  if cantidad == 3:
    numeros = [int(numero[0]), int(numero[1]), int(numero[2])]
    numOrdenado = sorted(numeros, reverse= True)
    numNuevo = "{0}{1}{2}".format(numOrdenado[0],numOrdenado[1],numOrdenado[2])
    result = int(numNuevo)
    return result
  else:  
    return ("numeros incorrectos")

def op4():
    
  return ("salir")
    

menu(4,58,35)