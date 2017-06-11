from pygame import *
from gui.ficha import Ficha


class Jugador():
    def __init__(self, nombre, avatar):
        self.nombre = nombre
        self.avatar = avatar
        self.ficha = None
