

#Escribe un algoritmo que le pida un numero al usuario, si el numero que ingreso el usuario es el correcto escribe "usted a ganado", si el numero es no es correcto escribe " usted a perdido"

import random

number = input ("Escriba un numero: ")
number = float (number)
ran_number = random.randint(1, 9)

if number==ran_number:

  print ("You are a winner")
  
else:

    print ("You are a lose")
    print ("The random number is: ", ran_number)












