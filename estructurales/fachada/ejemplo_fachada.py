from .fachada import *
from cadena_principal import Control

class EjemploFachada(Control):
    def obtener_nombre(self):
        return "Fachada"

    def handler_request(self, opt):
        if opt == 8:
            print("Ejemplo fachada")

            fachada = Fachada()

            print(fachada.buscar_libros())
            print(fachada.buscar_musica())
            print(fachada.buscar_videos())
            
        else:
            self.__succesor__.handler_request(opt)

