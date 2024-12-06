"""Diseña una función que tome como parámetro 2 números, y que devuelva una 
lista que contenga TODOS los números enteros entre estos 2 incluyendo AMBOS 
parámetros. 
Ejemplo: los parámetros para mi función son 1 y 9, por lo tanto, mi función 
retornara: [1,2,3,4,5,6,7,8,9] """

# def rango(num1, num2):
#    return list(range(num1, num2 + 1))


# resultado = generar_rango(1, 9)
# print(resultado)




"""Escribir una función que tome como parámetro 2 números, y retorne una lista con 
todos los números pares entre estos, EXCLUYENDO a los parámetros.
Ejemplo: los parámetros son 4 y 9, por lo tanto, la función retornara: [6,8]"""

# def par(num1, num2):
#      return [i for i in range(num1 + 1, num2) if i % 2 == 0]


# resultado = par(4, 9)
# print(resultado)



"""Escribir una función que tome 2 parámetros, el primero que reciba una cadena, y 
el segundo que reciba un carácter. La función tendrá que retornar la cantidad de 
veces que aparece ese carácter en esa cadena.
Ejemplo: si los parámetros son “Hola mi nombre es Sebastián” y “s”, la función 
tendrá que retornar 3 ya que la “s” se encuentra 3 veces repetidas en mi cadena..
"""

# def contar_caracter(cadena, caracter):
#     return cadena.count(caracter)


# resultado = contar_caracter("Hola mi nombre es Sebastián", "s")
# print(resultado)

""""""

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
