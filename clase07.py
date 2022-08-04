import math

# Mostrar la tangente de un numero.

def find_tan(my_number):
    result = math.tan(my_number)
    print(f"La Tangente de {my_number} es: {result}")
    

my_number = float(input("Ingrese un numero:  "))
find_tan(my_number)
