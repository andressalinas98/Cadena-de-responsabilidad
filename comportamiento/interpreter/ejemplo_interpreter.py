from .interpreter import *
from cadena_principal import Control

class EjemploInterpreter(Control):
    def obtener_nombre(self):
        return "Interpreter"

    def handler_request(self, opt):
        if opt == 12:
            operacion = ExpresionPluss(left=ExpresionNumber(value='15'),right=ExpresionMinus(left=ExpresionNumber(value='25'), right=ExpresionNumber(value='5')))

            print(operacion.evaluate())
        else:
            self.__succesor__.handler_request(opt)

   