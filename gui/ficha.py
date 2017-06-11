from gui.dibujable import Dibujable


class Ficha(Dibujable):
    def __init__(self, posicion_x, posicion_y, nombre_archivo, ancho=60, alto=60, dibujado=False):
        super().__init__(posicion_x, posicion_y, nombre_archivo, ancho, alto, dibujado)

    def _al_mover(self):
        pass

    def _al_dibujar(self):
        pass
