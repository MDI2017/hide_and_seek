from .casillero import *
from constantes import *

ALTO_CASILLERO = 60


class Tablero:
    def __init__(self):
        self.casilleros = [[Casillero(60, 60 * x, 60 * i) for i in range(12)] for x in range(10)]

    def dibujarCasilleros(self):

        for indexColumna, columna in enumerate(self.casilleros):
            for indexFila, casillero in enumerate(columna):

                if indexFila == 0:
                    casillero.color = COLORES.PIEDRA_LIBRE
                    casillero.zona = ZONAS.PIEDRA_LIBRE
                    if indexColumna == 4:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 5:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO

                elif indexFila == 1:
                    casillero.zona = ZONAS.PIEDRA_LIBRE
                    casillero.color = COLORES.DARK_PRIMARY

                    if indexColumna == 1 or indexColumna == 7:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 2 or indexColumna == 8:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO
                    if (1 <= indexColumna <= 3) or(6 <= indexColumna <= 8):
                        casillero.paredes[DIVISIONES.INFERIOR] = ESTADOS.TIENE_MURO

                elif indexFila == 2:
                    if indexColumna == 1 or indexColumna == 7:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 2 or indexColumna == 8:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO
                    if (1 <= indexColumna <= 3) or(6 <= indexColumna <= 8):
                        casillero.paredes[DIVISIONES.SUPERIOR] = ESTADOS.TIENE_MURO

                elif indexFila == 3:
                    if indexColumna == 0 or indexColumna == 9:
                        casillero.paredes[DIVISIONES.INFERIOR] = ESTADOS.TIENE_MURO
                    if indexColumna == 4:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 5:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO

                elif indexFila == 4:
                    casillero.zona = ZONAS.PERRITO_GUARDIAN
                    if indexColumna == 0 or indexColumna == 9:
                        casillero.paredes[DIVISIONES.SUPERIOR] = ESTADOS.TIENE_MURO
                    if indexColumna == 2 or indexColumna == 4 or indexColumna == 6:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 3 or indexColumna == 5 or indexColumna == 7:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO
                    if indexColumna == 2 or indexColumna == 4 or indexColumna == 5 or indexColumna == 7:
                        casillero.paredes[DIVISIONES.INFERIOR] = ESTADOS.TIENE_MURO

                elif indexFila == 5:
                    if indexColumna == 2 or indexColumna == 4 or indexColumna == 5 or indexColumna == 7:
                        casillero.paredes[DIVISIONES.SUPERIOR] = ESTADOS.TIENE_MURO

                elif indexFila == 6:
                    if indexColumna == 1 or indexColumna == 3 or indexColumna == 6 or indexColumna == 8:
                        casillero.paredes[DIVISIONES.INFERIOR] = ESTADOS.TIENE_MURO
                    if indexColumna == 4:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 5:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO

                elif indexFila == 7:
                    casillero.zona = ZONAS.DOBLE_LANZAMIENTO
                    if indexColumna == 1 or indexColumna == 3 or indexColumna == 6 or indexColumna == 8:
                        casillero.paredes[DIVISIONES.SUPERIOR] = ESTADOS.TIENE_MURO
                    if indexColumna == 2 or indexColumna == 6:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 3 or indexColumna == 7:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO

                elif indexFila == 8:
                    if indexColumna == 0 or indexColumna == 9:
                        casillero.paredes[DIVISIONES.INFERIOR] = ESTADOS.TIENE_MURO
                    if indexColumna == 4:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 5:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO

                elif indexFila == 9:
                    if indexColumna == 0 or indexColumna == 9:
                        casillero.paredes[DIVISIONES.SUPERIOR] = ESTADOS.TIENE_MURO
                    if indexColumna == 4:
                        casillero.paredes[DIVISIONES.DERECHA] = ESTADOS.TIENE_MURO
                    if indexColumna == 5:
                        casillero.paredes[DIVISIONES.IZQUIERDA] = ESTADOS.TIENE_MURO
                    if 3 <= indexColumna <= 6:
                        casillero.paredes[DIVISIONES.INFERIOR] = ESTADOS.TIENE_MURO

                elif indexFila == 10:
                    if 3 <= indexColumna <= 6:
                        casillero.zona = ZONAS.PROHIBIDA
                        casillero.color = COLORES.ZONA_PROHIBIDA
                    elif indexColumna == 2 or indexColumna == 7:
                        casillero.zona = ZONAS.LARGADA
                        casillero.color = COLORES.ZONA_LARGADA
                    else:
                        casillero.zona = ZONAS.ESCAPE
                        casillero.color = COLORES.ZONA_ESPCAPE

                else:
                    if indexColumna <= 3 or indexColumna >= 6:
                        casillero.zona = ZONAS.FUERA_TABLERO
                    else:
                        casillero.zona = ZONAS.LIBERTAD
                        casillero.color = COLORES.ZONA_LIBERTAD

                casillero.dibujarCasillero()

    def dibujarDivisiones(self):

        for indexColumna, columna in enumerate(self.casilleros):
            for indexFila, casillero in enumerate(columna):
                casillero.dibujarDivisiones()