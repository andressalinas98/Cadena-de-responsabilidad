from .chain_of_responsability import *
from cadena_principal import Control

class EjemploCadena(Control):
    def obtener_nombre(self):
        return "Chain of responsability"

    def handler_request(self, opt):
        if opt == 10:
            cadena = [HandlerOptionSix(), HandlerOptionTwo(), HandlerOptionThree(), HandlerOptionFour(),
                  HandlerOptionFive(), HandlerOptionOne(), HandlerOptionSeven(), HandlerOptionDefault()]

            for i in range(len(cadena)-1):
                cadena[i].set_succesor(cadena[i+1])

            opcion = int(input("ingrese un número: "))
            cadena[0].handler_request(opcion)

        else:
            self.__succesor__.handler_request(opt)
