def reto1(x):
    cadena = str(x)
    invertido = cadena[3]+cadena[2]+cadena[1]+cadena[0]
    num = int(invertido)
    return num

reto1(1234) 

def reto2(x50,x100,x200,x500):
    moneda50 = x50 * 50
    moneda100 = x100 * 100
    moneda200 = x200 * 200
    moneda500 = x500 * 500
    result = moneda50+moneda100+moneda200+moneda500
    
    return result

reto2(1,2,1,2)

def reto3(x):
    b = x**(1/2)
    b = round(b)
    return b

reto3(25)

def reto4(x,y):
    
    resultado = int(x)+int(y)
    
    return resultado

reto4("4","4")