from constantes import RECT
from gui.dibujable import Dibujable
from gui.clickeable import Clickeable
from constantes import PATHS

ACTIVO = 0
PRESIONADO = 1
INACTIVO = 2


class Button(Clickeable, Dibujable):
    """
    Clase para generar los botones necesarios dentro de la interfaz gráfica
    """

    def __init__(self, posicion_x, posicion_y, nombre_archivo, ancho=None, alto=None, dibujado=False):
        super().__init__(posicion_x, posicion_y, nombre_archivo)
        self.nombeArchivoPresionado = None
        self.nombeArchivoDesactivado = None

    def _al_clickear(self):
        self.cambiar_imagen(PRESIONADO)

    def _al_dibujar(self):
        self.rect = self.sprite.rect
        self.xFinal = self.rect[RECT.POS_X] + self.rect[RECT.ANCHO]
        self.yFinal = self.rect[RECT.POS_Y] + self.rect[RECT.ALTO]

        if self.inactivo:
            self.cambiar_imagen(INACTIVO)

    def _al_liberar_click(self):
        self.cambiar_imagen(ACTIVO)
