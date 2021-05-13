print("este es un programa que genera un numero aleatorio haber si aciertas suerte !!")
import random
while True:
    nun=float(input("elige tu numero"))
    al= random.randint (1,10)
    if nun==al:
        print ("acertaste")
        break
    else:
        print ("nunca acertaras jajajaja perdiste")
