from .bridge import *
from cadena_principal import Control

class EjemploBridge(Control):
    def obtener_nombre(self):
        return "Bridge"

    def handler_request(self, opt):
        if opt == 4:
            print("Ejemplo bridge")

            objeto = Abstraccion(ImplementadorConcretoB())
            print(objeto.operacion())

            objeto_refinado = AbstraccionRefinada(ImpelmentadorConcretoC())
            print(objeto_refinado.operacion())
            print(objeto_refinado.operacion_refinada())
        else:
            self.__succesor__.handler_request(opt)

    