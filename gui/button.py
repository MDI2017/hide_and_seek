from constantes import *
from gui.dibujable import Dibujable


class Button(Dibujable):
    """
    Clase para generar los botones necesarios dentro de la interfaz gráfica
    """

    # def __init__(self, posicion_x, posicion_y, alto, ancho, color=COLORES.AZUl):
    #     super().__init__(posicion_x, posicion_y, alto, ancho, color)

    def boton_precionado(self, posicion):

        if posicion and self.posicionX < posicion[1] < self.posicionX + self.alto \
                and self.posicionY < posicion[0] < self.posicionY + self.ancho:
            print(posicion)
            return True

        return False




