#!/usr/bin/python
# -*- coding: utf-8 -*-

from usuarios.modelo.Persona import Persona


class Operador(Persona):
    def __init__(self):
        self.licencia = None
        self.equipoAsignado = None

    def operar(self, ):
        pass

    def reportarIncidencia(self, ):
        pass
