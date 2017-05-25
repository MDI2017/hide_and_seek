from pygame_functions import drawRect, drawLine
from constantes import COLORES
from .posicionable import Posicionable


class Dibujable(Posicionable):
    def __init__(self, posicion_x, posicion_y, ancho, alto, color=COLORES.AZUl, dibujado=False):
        super().__init__(posicion_x, posicion_y, ancho, alto)
        self.color = color
        self.dibujado = dibujado

    def dibujar(self):
        drawRect(self.posicionX, self.posicionY, self.ancho, self.alto, self.color)
        self.dibujado = True
