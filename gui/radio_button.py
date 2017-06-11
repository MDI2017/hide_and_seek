from constantes import RECT
from gui.dibujable import Dibujable
from gui.clickeable import Clickeable

INACTIVO = 0
SELECCIONADO = 1
DESHABILITADO = 2


class RadioButton(Clickeable, Dibujable):
    def __init__(self, posicion_x, posicion_y, nombre_archivo, ancho=None, alto=None, dibujado=False):
        super().__init__(posicion_x, posicion_y, nombre_archivo)

        self.seleccionado = None


    def _al_dibujar(self):
        self.rect = self.sprite.rect
        self.xFinal = self.rect[RECT.POS_X] + self.rect[RECT.ANCHO]
        self.yFinal = self.rect[RECT.POS_Y] + self.rect[RECT.ALTO]

        if self.inactivo:
            self.cambiar_imagen(DESHABILITADO)

    def _al_liberar_click(self):

        if self.seleccionado:
            self.cambiar_imagen(INACTIVO)
        else:
            self.cambiar_imagen(SELECCIONADO)

        self.seleccionado = not self.seleccionado

    def quitar_seleccion(self):
        self.seleccionado = False
        self.cambiar_imagen(INACTIVO)
