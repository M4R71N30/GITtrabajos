"""Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área 
del rectángulo"""

#class Rectangulo:
 # def __init__(self, base, altura):
    # self.base = base
     #self.altura = altura

    #def area(self):
    # return self.base * self.altura


#rectangulo = Rectangulo(5, 10)
#print("El área del rectángulo es:", rectangulo.area())

"""Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente 
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del 
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.""" 

# class Usuario:
#     def __init__(self, nombre, apellido, edad, email, telefono=None):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.telefono = telefono  
    
#     def describir_usuario(self):
#         print(f"Usuario: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Correo electrónico: {self.email}")
#         if self.telefono:
#             print(f"Teléfono: {self.telefono}")
#         else:
#             print("Teléfono no proporcionado.")
    
#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre} {self.apellido} Bienvenido.")

# usuario1 = Usuario("Juan", "Pérez", 30, "juan.perez@example.com", "123-456-7890")
# usuario2 = Usuario("Ana", "Gómez", 25, "ana.gomez@example.com")
# usuario3 = Usuario("Carlos", "Martínez", 40, "carlos.martinez@example.com", "987-654-3210")

# usuarios = [usuario1, usuario2, usuario3]

# for usuario in usuarios:
#     usuario.describir_usuario()
#     print()  
#     usuario.saludar_usuario()
    # print(" " * 40)  

"""Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: 
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un 
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase 
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los 
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame 
al método.""" 

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida
    
#     def describir_restaurante(self):
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")
    
#     def abrir_restaurante(self):
#         print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")


# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores = sabores
    
#     def mostrar_sabores(self):
#         print(f"Sabores disponibles en {self.restaurante_nombre}:")
#         for sabor in self.sabores:
#             print(f"- {sabor}")


# heladeria = Heladeria("la buena comida", "Helados", ["Chocolate", "Vainilla", "frutilla", "flan", "limon"])


# heladeria.describir_restaurante() 
# heladeria.abrir_restaurante()  
# heladeria.mostrar_sabores()  


