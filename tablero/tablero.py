from .casillero import *


class Tablero:
    def __init__(self):
        self.casilleros = [[Casillero(60, 60 * x, 60 * i) for i in range(12)] for x in range(10)]

    def dibujarCasilleros(self):

        for indexFila, fila in enumerate(self.casilleros):
            for indexColumna, casillero in enumerate(fila):
                casillero.dibujarCasillero()
