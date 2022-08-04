import math



#Write a Python program to calculate body mass index

#Ingrese la estatura en metros
altura = float(input('Ingrese su altura en metros: \n'))
#Ingrese el peso en KG
peso = float(input('Ingrese su peso en kilogramos: \n'))
#Hallar IMC
imc = peso / (altura**2)
#Mostramos el valor
print(f'El indice de masa corporal es de {round(imc, 2)}')

