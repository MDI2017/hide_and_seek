from constantes import RECT
from gui.dibujable import Dibujable
from gui.clickeable import Clickeable
from constantes import PATHS

ACTIVO = 0
PRESIONADO = 1
INACTIVO = 2


class Button(Dibujable):
    """
    Clase para generar los botones necesarios dentro de la interfaz gráfica
    """

    def __init__(self, posicion_x, posicion_y, nombre_archivo, ancho=None, alto=None, dibujado=False, inactivo=False):
        super().__init__(posicion_x, posicion_y, nombre_archivo, ancho, alto, dibujado)
        self.nombeArchivoPresionado = None
        self.nombeArchivoDesactivado = None
        self.inactivo = inactivo

    def click_boton(self, posicion_mouse):

        if self.inactivo:
            return False
        elif Clickeable.click_sprite(posicion_mouse, self.spriteRect):
            if self.sprite.currentImage == PRESIONADO:
                return True
            else:
                self.cambiar_imagen(1)
                return True
        elif self.sprite.currentImage == ACTIVO:
            return False
        else:
            self.cambiar_imagen(ACTIVO)
            return False
