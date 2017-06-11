from pygame import *
from gui.ficha import Ficha


class Jugador():
    def __init__(self, nombre, avatar, es_cazador=None):
        self.nombre = nombre
        self.avatar = avatar
        self.es_cazador = es_cazador
        self.ficha = None

    def __crear_ficha(self, pos_x, pos_y):
        self.ficha = Ficha()