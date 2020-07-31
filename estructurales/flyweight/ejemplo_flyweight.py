from .flyweight import *
from cadena_principal import Control

class EjemploFlyweight(Control):
    def obtener_nombre(self):
        return "Flyweight"

    def handler_request(self, opt):
        if opt == 9:
            print("Ejemplo flyweight")

            factoria = FlyweightFactory()

            flyweights = []

            for i in range(10):
                flyweights.append(factoria.entregar_flyweight())

            print(flyweights[0].concreto == flyweights[2].concreto)
            
            for f in flyweights:
                print(f.operacion())
        else:
            self.__succesor__.handler_request(opt)


      