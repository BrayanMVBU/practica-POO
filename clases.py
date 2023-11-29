
class Animal:
    def __init__(self, nombre, peso, color):
        self.nombre = nombre
        self.peso = peso
        self.color = color
    
    def mostrar(self):
        return f"{self.nombre}, {self.peso},{self.color}"
        

murcielago = Animal("murcielago","3","negro")
print(murcielago.mostrar())


           
    
        