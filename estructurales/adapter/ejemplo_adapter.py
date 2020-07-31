from .adapter import *
from cadena_principal import Control

class EjemploAdapter(Control):
    def obtener_nombre(self):
        return "Adapter"

    def handler_request(self, opt):
        if opt == 3:
            print("Ejemplo adapter")

            print("Objeto original")
            original = Original()
            print(original.escribir())

            print("Objeto a adaptar")
            adaptado = Adaptado()
            print(adaptado.escribir_reves())

            print("Objeto adaptado")
            adaptador = Adaptador()
            print(adaptador.escribir())
        else:
            self.__succesor__.handler_request(opt)

 