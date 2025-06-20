#!/usr/bin/python
# -*- coding: utf-8 -*-

from monitoreo.modelo.Equipo import Equipo


class Excavadora(Equipo):
    def __init__(self):
        self.tipoExcavacion = None
        self.horasOperacion = None

    def extraer(self, ):
        pass

    def cargarVolquete(self, ):
        pass
