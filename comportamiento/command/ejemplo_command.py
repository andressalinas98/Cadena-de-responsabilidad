from .command import *
from cadena_principal import Control

class EjemploCommand(Control):
    def obtener_nombre(self):
        return "Command"

    def handler_request(self, opt):
        if opt == 11:
            comandos = [Politician(), DomesticEngineer(), Programmer()]
            r = Recivier()
            for i in comandos:
                i.execute(r)
        else:
            self.__succesor__.handler_request(opt)        

