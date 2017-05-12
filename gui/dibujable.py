from pygame_functions import drawRect, drawLine
from constantes import COLORES


class Dibujable:
    def __init__(self, posicion_x, posicion_y, ancho, alto, color=COLORES.AZUl):
        self.posicionX = posicion_x
        self.posicionY = posicion_y
        self.alto = alto
        self.ancho = ancho
        self.color = color

    def dibujar(self):
        drawRect(self.posicionX, self.posicionY, self.ancho, self.alto, self.color)
