import math
# my_str = "A,9,1"
# my_str.split(",")
# print(my_str)

#ejercicio 1



#ejercicio 2

# Forgotten languages (also known as extinct languages) are languages that are no longer in use. Such languages were, probably, widely used before and no one could have ever imagined that they will become extinct at some point. Unfortunately, that is what happened to them. On the happy side of things, a language may be dead, but some of its words may continue to be used in other languages.

# Using something called as the Internet, you have acquired a dictionary of N words of a forgotten language. Meanwhile, you also know K phrases used in modern languages. For each of the words of the forgotten language, your task is to determine whether the word is still in use in any of these K modern phrases or not.

palabras = input("Ingrese las palabras a buscar: ")
oracion = input("Ingrese la oracion: ")

palabras = palabras.split(" ")

if palabras[0] in oracion:
    print(f"La palabra extinta {palabras[0]} SI está en el lenguaje")
else:
    print(f"La palabra extinta {palabras[0]} NO está en el lenguaje")

if palabras[1] in oracion:
    print(f"La palabra extinta {palabras[1]} SI está en el lenguaje")
else:
    print(f"La palabra extinta {palabras[1]} NO está en el lenguaje")
