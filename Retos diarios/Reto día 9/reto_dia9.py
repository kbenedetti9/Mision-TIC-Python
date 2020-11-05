def reto1(numero):
  
  suma = 0
  for i in range (0,numero+1,2):
    suma+=i 
  if numero%2 != 0:
    suma+=numero  
      
  print(suma)

reto1(9)    

def reto2(frase):
    frase = frase.upper()
    cantidad = len(frase)
    nuevaFrase = ''
    alfabeto = {
        'A':'D',
        'B':'E',
        'C':'F',
        'D':'G',
        'E':'H',
        'F':'I',
        'G':'J',
        'H':'K',
        'I':'L',
        'J':'M',
        'K':'N',
        'L':'Ñ',
        'M':'O',
        'N':'P',
        'Ñ':'Q',
        'O':'R',
        'P':'S',
        'Q':'T',
        'R':'U',
        'S':'V',
        'T':'W',
        'U':'X',
        'V':'Y',
        'W':'Z',
        'X':'A',
        'Y':'B',
        'Z':'C',
        ' ':' '
    }

    for i in range(cantidad):
      nuevaFrase+=alfabeto.get(frase[i])
             
    print(nuevaFrase)

reto2("EL ATAQUE A LOS GALOS INICIA EL LUNES EN LA MAÑANA")  

def reto3(frase, letra):
    frase = frase.lower()
    letra = letra.lower()
    cantidad = len(frase)
    suma = 0
    for i in range (cantidad):
      if frase[i] == letra:
        suma+= 1
       
    print(suma) # Modifica el codigo para imprimir cada valor

reto3("MONDONGO","o")