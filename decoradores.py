
def decorador(funcion):
    def funcion_modificada():
        print("antes de llmar a la funcion")
        funcion()
        print("despues d ellamr a una funcion")
    return funcion_modificada


def saludo():
    print("hola brayan")

saludo_modificado = decorador(saludo)
saludo_modificado()