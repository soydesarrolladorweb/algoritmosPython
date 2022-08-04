'''
Ejercicio 1.
Genere un programa que reciba un entero n, entre 1 y 20, y que imprima el cubo de
los números desde 1 hasta n espaciados por un final de línea, avanzando de 1 en 1.
Ejemplo:    
                n = 4
                1
                4
                9
                16
'''
n = input("Insert a upper limit number: ")
n = int(n)

# Solution 1

while n >= 1:
    print(n ** 3)
    n -= 1


# Solution 2

n = input("Insert a upper limit number: ")
n = int(n)
for i in range(1, n + 1):
    print(i ** 3)


# Solution 3

n = input("Insert a upper limit number: ")
n = int(n)
result = []

while n >= 1:
    result.append(n ** 3)
    n -= 1

result.reverse()
for i in result:
    print(i)


# Solution 4

n = input("Insert a upper limit number: ")
n = int(n)

j = 20

while n >= 1:
    if n == j:
        for i in range(1, n + 1):
            print(i ** 3)
        break
    else:
        j -= 1



'''
ercicio 2.
Los palíndromos son frases que se leen igual de derecha de izquierda que de
izquierda a derecha. Por ejemplo, anita lava la tina es un palíndromo, ya que
obviando los espacios en blanco, la frase se lee igual. Elabora un programa que diga
si una frase es un palíndromo o no.
Ejemplo:
frase = “anita la la tina”
resultado = la frase “anita lava la tina” es un palíndromo
Pista 1: Puedes usar el método replace(“ “, “”) para reemplazar los espacios en
blanco de la frase
Pista 2: Las cadenas de texto pueden recorrerse de manera similar que una lista, es
decir, for letra in cadena: print(letra)
'''

# Solution 2

phrase = input("Insert a phrase to analyse: ")
phrase = phrase.replace(" ", "")
new_phrase = phrase[::-1]
print(phrase == new_phrase)

# Solution 3

phrase = input("insert a phrase: ")
phrase = phrase.replace(" ", "")
phrase = phrase.lower()
new_phrase = phrase[::-1]
print("es un palindromo" if new_phrase == phrase else "no es un palindromo")
