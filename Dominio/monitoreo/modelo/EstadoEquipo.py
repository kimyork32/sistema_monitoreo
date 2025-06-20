#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

class EstadoEquipo(Enum):
    OPERATIVO = 1
    EN_MANTENIMIENTO = 2
    CARGANDO = 3
    DESCARGANDO = 4
    TRANSPORTANDO = 5
