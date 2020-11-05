def reto1(N):
   
   if N<100:
     result = "Error en el numero"
   else:
     num = str(N)
     cantidad = len(num)
     indice = cantidad - 1
     if (num[indice] == '4' or num[indice] == '7' or num[indice] == '9'):
       if (N % 3 == 0):
         result = "es divisible"
       else:
         result = "no es divisible"
     elif (num[indice] == '1' or num[indice] == '5'):
       result = N//10
     else:
       result = N % 3

   return result

reto1(142)

def calcularI(v,r):
    if v<=0 and r<=0:
        resultado = "Error en los numeros I"
    else:
       resultado = v/r
    return resultado 

def calcularV(i,r):
    if i<=0 and r<=0:
      resultado = "Error en los numeros V"
    else:
      resultado = i*r
    return resultado 

def calcularR(v,i):
    if v<=0 and i<=0:
      resultado = "Error en los numeros R"
    else:
      resultado = v/i
    return resultado 

def reto2(opcion, valorI, valorV, valorR):

  operaciones = {
        1: calcularI(valorV,valorR),
        2: calcularV(valorI,valorR),
        3: calcularR(valorV,valorI)
  }

  if opcion>3 or opcion<0:
    result = "Opcion incorrecta"
  else:
    result = operaciones.get(opcion)
    
  return result

reto2(3,0.2,3,3) 

def reto3(mes, dia, año):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    if mes>12 or mes<0:
      result = "Error en los numeros M"
    else:
      mesFecha = meses.get(mes)
      if dia>31 or dia<1:
        result = "Error en los numeros D"
      else:
        diaFecha = dia
        if año>2999 or año<1:
          result = "Error en los numeros A"
        else:
          anhoFecha = año
          result = "{0}, {1} de {2}".format(mesFecha,diaFecha,anhoFecha)

    return result
    
reto3(11,7,1985) 