from .composite import *
from cadena_principal import Control

class EjemploComposite(Control):
    def obtener_nombre(self):
        return "Composite"

    def handler_request(self, opt):
        if opt == 5:
            print("Ejemplo composite")

            elemento = Compuesto()

            for i in range(5):
                elemento.agregar_elemento(Simple())

            elemento2 = Compuesto()
            elemento2.agregar_elemento(Simple())

            elemento.agregar_elemento(elemento2)
            elemento.operacion()
        else:
            self.__succesor__.handler_request(opt)

