from .proxy import *
from cadena_principal import Control

class EjemploProxy(Control):
    def obtener_nombre(self):
        return "Proxy"

    def handler_request(self, opt):
        if opt == 7:
            print("Ejemplo proxy")

            proxy = Proxy(RealSubject())

            print(proxy.peticion())
        else:
            self.__succesor__.handler_request(opt)

       