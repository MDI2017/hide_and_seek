from constantes import *
from gui.dibujable import Dibujable
from gui.clickeable import Clickeable


class Button(Dibujable):
    """
    Clase para generar los botones necesarios dentro de la interfaz gráfica
    """
    def boton_precionado(self,posicion_mouse):

        return Clickeable.elemento_precionado( posicion_mouse, self.posicionX, self.posicionY, self.alto, self.ancho)
