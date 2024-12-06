"""Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo 
para un rango de números indicado por un usuario. """

# def es_primo(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def numeros_primos_en_rango(num1, num2):
#     return [i for i in range(num1 + 1, num2) if es_primo(i)]

# resultado = numeros_primos_en_rango(10, 30)
# print(resultado)

"""Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por 
ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50 """

# numero = int(input("Ingresa un número para obtener su tabla de multiplicar: "))

# tabla_multiplicar = [numero * i for i in range(1, 11)]

# print(f"La tabla de multiplicar del {numero} es:", tabla_multiplicar)

"""Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir 
caracteres. """

# cadena = input("Ingresa una cadena: ")

# caracteres_unicos = []

# for caracter in cadena:
#     if caracter not in caracteres_unicos:
#         caracteres_unicos.append(caracter)

# print("Lista de caracteres únicos:", caracteres_unicos)

"""Crea una tupla con números, pide un numero por teclado e indica cuantas veces se 
repite."""

# tupla = (1, 2, 3, 4, 5, 3, 7, 3, 8, 9)


# numero = int(input("Ingresa un número para saber cuántas veces se repite en la tupla: "))

# repeticiones = tupla.count(numero)

# print(f"El número {numero} se repite {repeticiones} veces en la tupla.")

""" Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios"""

# cadena = input("Ingresa una cadena: ")

# cadena_sin_espacios = [caracter for caracter in cadena if caracter != ' ']

# print("Lista de caracteres sin espacios:", cadena_sin_espacios)




