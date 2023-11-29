
def decorador(funcion):
    def funcion_modificada():
        print("antes de llmar a la funcion")
        funcion()
    return funcion_modificada



@decorador
def saludo():
    print("hoola brayan como andas")

saludo()