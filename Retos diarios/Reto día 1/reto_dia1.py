def reto1(x,y,z,w):
    
  result = (x+y+z+w)/4
    
  return result

reto1(3,3,3,3)

def reto2(x):
    
    miNum = str(x)
    num = len(miNum)
    
    return num

reto2(1234)

def reto3(x):
    
    ultimoNum = x%10
    
    return ultimoNum

reto3(789)

def reto4(x,y):
    
    num1 = x%10
    num2 = x//10
    num3 = y%10
    num4 = y//10
    result = num1 + num2 + num3 + num4
    return result

reto4(35,52)