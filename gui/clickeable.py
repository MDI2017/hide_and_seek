import pygame
from constantes import RECT
from gui.posicionable import Posicionable


class Clickeable(Posicionable):
    """
    Clase que le da la propiedad a los elementos para ser clickeables y asi ser seleccionado. Recibe una la posicion donde se hizo
    click en el mouse, si el elemento esta ubicado donde se hizo el click se realiza la operacion
    """
    def __init__(self, posicion_x, posicion_y, ancho=None, alto=None):
        super().__init__(posicion_x, posicion_y, ancho, alto)

        self.rect = None
        self.xFinal = None
        self.yFinal = None
        self.inactivo = None

    def click_elemento(self, posicion_mouse):
        if self.inactivo or not posicion_mouse or not self._verificar_posicion(posicion_mouse,
                                                                               self.rect[RECT.POS_X], self.xFinal,
                                                                               self.rect[RECT.POS_Y], self.yFinal):
            return False
        else:
            return self._clickeado()

    def _clickeado(self):
        self._al_clickear()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    posicion_mouse = pygame.mouse.get_pos()
                    self._al_liberar_click()
                    return self._verificar_posicion(posicion_mouse,
                                                    self.rect[RECT.POS_X], self.xFinal,
                                                    self.rect[RECT.POS_Y], self.yFinal)

    def _verificar_posicion(self, posicion_mouse, x_inicial, x_final, y_inicial, y_final):
        return x_inicial < posicion_mouse[0] < x_final and y_inicial < posicion_mouse[1] < y_final

    def activar(self):
        self.inactivo = False
        self._al_activar()

    def desactivar(self):
        self.inactivo = True
        self._al_desactivar()

    def _al_clickear(self):
        pass

    def _al_liberar_click(self):
        pass

    def _al_desactivar(self):
        pass

    def _al_activar(self):
        pass
