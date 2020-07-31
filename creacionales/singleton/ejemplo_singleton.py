from .singleton import Singleton
from cadena_principal import Control

class EjemploSingleton(Control):
    def obtener_nombre(self):
        return "Singleton"

    def handler_request(self, opt):
        if opt == 0:
            print("Ejemplo Singleton")
            x = Singleton.get_instance()
            y = Singleton.get_instance()


            print( x is y)

            y.set_value(10)

            print(x.get_value())
        else:
            self.__succesor__.handler_request(opt)

    