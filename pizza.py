from ingredientes import *

class Pizza:
    # Atributos estáticos de clase
    precio = 10000
    tamaño = "familiar"
    
    # Atributos de instancia
    def __init__(self):
        self.proteico = ""
        self.vegetales = []
        self.masa = ""
        self.valido = False

    @staticmethod
    def validar_elemento(elemento, lista):
        """Valida si el elemento está en la lista dada"""
        return elemento in lista

    def realizar_pedido(self):
        """Solicita ingredientes al usuario y valida si la pizza es válida"""
        while True:
            proteico = input(f"Ingrese el ingrediente proteico ({proteicos}): ")
            if self.validar_elemento(proteico, proteicos):
                self.proteico = proteico
                break
            else:
                print("Ingrediente proteico inválido. Por favor, elija entre:", proteicos)

        while True:
            vegetal_1 = input(f"Ingrese el primer ingrediente vegetal ({vegetales}): ")
            if self.validar_elemento(vegetal_1, vegetales):
                self.vegetales.append(vegetal_1)
                break
            else:
                print("Ingrediente vegetal inválido. Por favor, elija entre:", vegetales)

        while True:
            vegetal_2 = input(f"Ingrese el segundo ingrediente vegetal ({vegetales}): ")
            if self.validar_elemento(vegetal_2, vegetales) and vegetal_2 != vegetal_1:
                self.vegetales.append(vegetal_2)
                break
            else:
                print("Ingrediente vegetal inválido o repetido. Por favor, elija otro ingrediente.")

        while True:
            masa = input(f"Ingrese el tipo de masa ({masas}): ")
            if self.validar_elemento(masa, masas):
                self.masa = masa
                break
            else:
                print("Tipo de masa inválido. Por favor, elija entre:", masas)

        # Verificar que se ingresaron 2 ingredientes vegetales diferentes
        if len(self.vegetales) == 2:
            self.valido = True
        else:
            print("Debe ingresar 2 ingredientes vegetales distintos.")
            self.valido = False