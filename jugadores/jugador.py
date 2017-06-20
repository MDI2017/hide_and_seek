from pygame import *
from gui.ficha import Ficha


class Jugador:
    """
    Clase que crea un jugador con nombre y avatar que le designemos
    """
    def __init__(self, nombre, avatar):
        self.nombre = nombre
        self.avatar = avatar
        self.ficha = None
