import random
from pygame_functions import *
from gui.dibujable import Dibujable
from gui.clickeable import Clickeable
from constantes import RECT


class Dado(Clickeable, Dibujable):
    """
       Clase que crea y dibuja el dado, nos da la posibilidad de poder tirarlo y que nos de un resultado aleatorio dentro de las 6
       posibilidades
       """
    def __init__(self, posicion_x, posicion_y, nombre_archivo="dice1.png",
                 ancho=None, alto=None, dibujado=False):
        super().__init__(posicion_x, posicion_y, nombre_archivo)

        self.agregar_imagen("dice2.png")
        self.agregar_imagen("dice3.png")
        self.agregar_imagen("dice4.png")
        self.agregar_imagen("dice5.png")
        self.agregar_imagen("dice6.png")
        self.dibujar()

    def _al_liberar_click(self):
        self.tirar_dado()

    # def _clickeado(self):
    #     return super()._clickeado()

    # def _al_clickear(self):
    #     super()._al_clickear()

    def _al_dibujar(self):
        self._set_parametros()

    def tirar_dado(self):
        giros_dado = 10
        movimientos = 0

        while giros_dado > 0:
            pause(100)
            movimientos = random.randint(0, 5)
            self.cambiar_imagen(movimientos)
            giros_dado -= 1

        return movimientos + 1

    def _set_parametros(self):
        self.rect = self.sprite.rect
        self.xFinal = self.rect[RECT.POS_X] + self.rect[RECT.ANCHO]
        self.yFinal = self.rect[RECT.POS_Y] + self.rect[RECT.ALTO]
