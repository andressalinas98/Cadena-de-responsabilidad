#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .fabricas import *
from cadena_principal import Control

class EjemploAbstractFactory(Control):
    def obtener_nombre(self):
        return "AbstractFactory"

    def handler_request(self, opt):
        if opt == 1:
            print("Ejemplo Abstract Factory")
            print("seleccione una fabrica: \n\t 0 - AMD \n\t 1 - Intel \n\t 2 - Alien ")
            fabricas = [FabricaAMD(), FabricaIntel(), FabricaAlien()]

            fabrica = fabricas[int(input())]

            partes = [fabrica.crearMemoria(), fabrica.crearProcesador(), fabrica.crearBoard()]

            for p in partes:
                p.implementacion()
                p.operacion()
        else:
            self.__succesor__.handler_request(opt)

    