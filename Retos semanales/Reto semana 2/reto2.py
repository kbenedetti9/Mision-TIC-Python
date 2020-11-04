def controldecamion(time, cajas):
  i=1
  totalCajas=2000
  if time <=15:
    while i<=20 and totalCajas !=0:
      j=1
      print("Punto de distribución # {0}".format(i))
      while j <= cajas and totalCajas !=0:
        totalCajas-=1
        if j > 100:
          print("Encender alarma")
        print("Caja # {0}".format(j))
        j+=1 
      i+=1
      if totalCajas==0 and cajas>100:
        print("Se ha agotado el inventario en el camión") 
      print("El total de cajas en inventario en el camión=  {0}".format(totalCajas))
      print("Cantidad de cajas despachadas =  {0}".format(j-1))
      print("Tiempo de despacho =  {0}".format(time))    
  else:
    print("Se excede el limite de tiempo")    

controldecamion(10,100)