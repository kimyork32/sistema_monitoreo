#!/usr/bin/python
# -*- coding: utf-8 -*-

from monitoreo.modelo.Equipo import Equipo


class Volquete(Equipo):
    def __init__(self):
        self.capacidadCarga = None
        self.cargaActual = None

    def cargar(self, ):
        pass

    def descargar(self, ):
        pass
