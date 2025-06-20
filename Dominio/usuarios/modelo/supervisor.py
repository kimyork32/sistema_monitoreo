#!/usr/bin/python
# -*- coding: utf-8 -*-

from usuarios.modelo.Persona import Persona


class Supervisor(Persona):
    def __init__(self):
        self.EquipoAsignado = None

    def asignarOperacion(self, ):
        pass

    def monitorearEquipos(self, ):
        pass
