from constantes import RECT, ESTADOS_BOTONES
from gui.dibujable import Dibujable
from gui.clickeable import Clickeable


class Button(Clickeable, Dibujable):
    """
    Clase para generar los botones necesarios dentro de la interfaz gráfica
    """

    def __init__(self, posicion_x, posicion_y, nombre_archivo, ancho=None, alto=None, dibujado=False):
        super().__init__(posicion_x, posicion_y, nombre_archivo)

    def _al_clickear(self):
        if len(self.sprite.images) > 1:
            self.cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)

    def _al_dibujar(self):
        self._set_parametros()
        if self.inactivo:
            self.cambiar_imagen(ESTADOS_BOTONES.INACTIVO)

    def _al_liberar_click(self):
        self.cambiar_imagen(ESTADOS_BOTONES.ACTIVO)

    def _set_parametros(self):
        self.rect = self.sprite.rect
        self.xFinal = self.rect[RECT.POS_X] + self.rect[RECT.ANCHO]
        self.yFinal = self.rect[RECT.POS_Y] + self.rect[RECT.ALTO]

    def _al_mover(self):
        self._set_parametros()

    def _al_desactivar(self):
        self.cambiar_imagen(ESTADOS_BOTONES.INACTIVO)

    def _al_activar(self):
        self.cambiar_imagen(ESTADOS_BOTONES.ACTIVO)