from pizza import Pizza
from ingredientes import *

# a. Imprimir los atributos de clase
print("Precio de la pizza:", Pizza.precio)
print("Tamaño de la pizza:", Pizza.tamaño)

# b. Validar "salsa de tomate"
print("Salsa de tomate está en la lista:", Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Crear instancia y realizar pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Imprimir los detalles del pedido
print("Ingredientes proteicos:", mi_pizza.proteico)
print("Ingredientes vegetales:", mi_pizza.vegetales)
print("Tipo de masa:", mi_pizza.masa)
print("Es una pizza válida:", mi_pizza.valido)

# e. Mostrar si la clase Pizza es válida (debe generar un error)
# print("Es la clase Pizza válida?", Pizza.valido)  # Genera un error, ya que `valido` es un atributo de instancia, no de clase.