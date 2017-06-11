from gui.dibujable import Dibujable
from constantes import CASILLAS


class Ficha(Dibujable):
    def __init__(self, casillero, nombre_archivo, ancho=60, alto=60, dibujado=False):
        super().__init__(0, 0, nombre_archivo=nombre_archivo, ancho=ancho, alto=alto, dibujado=dibujado)
        self.posicionX = CASILLAS.LADO * casillero[0]
        self.posicionY = CASILLAS.LADO * casillero[1]

    def _al_mover(self):
        pass

    def _al_dibujar(self):
        pass
