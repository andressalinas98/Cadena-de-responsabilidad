from .decorator import *
from cadena_principal import Control

class EjemploDecorator(Control):
    def obtener_nombre(self):
        return "Decorator"

    def handler_request(self, opt):
        if opt == 6:
            print("Ejemplo decorator")

            objeto = ComponenteConcreto()
            objeto.operacion()
            print("-"*10)
            decorador1 = DecoradorConcretoA(objeto)
            decorador1.operacion()
            print("-"*10)
            decorador2 = DecoradorConcretoB(decorador1)
            decorador2.operacion()
        else:
            self.__succesor__.handler_request(opt)

