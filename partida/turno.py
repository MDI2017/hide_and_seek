from jugadores.cazador import Cazador
from constantes import CASILLAS, DIVISIONES, TABLERO
from .info_turno import InfoTurno


class Turno:
    def __init__(self, tablero):
        self.tablero = tablero
        self.jugador = None
        self.primer_turno = True
        self.info = InfoTurno()

    def cambio_turno(self, jugador):
        self.jugador = jugador
        self._set_info()

    def _set_info(self):
        self.info.jugador_actual(self.jugador)

    def set_movimientos(self, movimientos):
        self.jugador.ficha.movimientos = movimientos
        self.info.movim_restantes(movimientos)

    def mover_ficha(self, nuevo_casillero):
        movimientos = self.jugador.ficha.mover_ficha(nuevo_casillero)
        self.info.movim_restantes(movimientos)

    def fin_turno(self):
        if isinstance(self.jugador, Cazador):
            self._verificar_avistaje()

    def _verificar_avistaje(self):
        casillero_cazador = self.jugador.ficha.casillero.indice

        # verificación vertical inferior
        print(self._vertical_verification(casillero_cazador[CASILLAS.FILA] + 1, TABLERO.FILAS, True))

        # verificación vertical superior
        print(self._vertical_verification(TABLERO.INICIO, casillero_cazador[CASILLAS.FILA]))

        # verificación horizontal derecha
        print(self._horizontal_verification(casillero_cazador[CASILLAS.COLUMNA] + 1, TABLERO.COLUMNAS, True))

        # verificación horizontal izquierda
        print(self._horizontal_verification(TABLERO.INICIO, casillero_cazador[CASILLAS.COLUMNA]))

        # verificación diagona superior derecha
        print(self._diagonal_verification(TABLERO.INICIO, casillero_cazador[CASILLAS.FILA], True))

        # verificación diagona superior izquierda
        print(self._diagonal_verification(TABLERO.INICIO, casillero_cazador[CASILLAS.FILA]))

        # verificación diagona superior derecha
        print(self._diagonal_verification(casillero_cazador[CASILLAS.FILA] + 1, TABLERO.FILAS, True, True))

        # verificación diagona superios izquierda
        print(self._diagonal_verification(casillero_cazador[CASILLAS.FILA] + 1, TABLERO.FILAS, False, True))

    def _vertical_verification(self, inicio, final, abajo=False):
        columna = self.jugador.ficha.casillero.indice[CASILLAS.COLUMNA]

        if abajo:
            division = DIVISIONES.SUPERIOR
        else:
            division = DIVISIONES.INFERIOR

        for i in range(inicio, final):

            if abajo:  # itera hacia abajo
                fila = i
            else:  # itera hacia arriba
                fila = final - i - 1

            casillero = self.tablero.casilleros[columna][fila]

            if casillero.paredes[division]:
                return False
            if casillero.esta_ocupado:
                return columna, fila

        return False

    def _horizontal_verification(self, inicio, final, derecha=False):
        fila = self.jugador.ficha.casillero.indice[CASILLAS.FILA]

        if derecha:
            division = DIVISIONES.IZQUIERDA
        else:
            division = DIVISIONES.DERECHA

        for i in range(inicio, final):

            if derecha:  # itera hacia Derecha
                columna = i
            else:  # itera hacia izquierda
                columna = final - i - 1

            casillero = self.tablero.casilleros[columna][fila]

            if casillero.paredes[division]:
                return False
            if casillero.esta_ocupado:
                return columna, fila

        return False

    def _diagonal_verification(self, inicio, final, derecha=False, abajo=False):

        columna = self.jugador.ficha.casillero.indice[CASILLAS.COLUMNA]

        if (derecha and abajo) or (not derecha and not abajo):
            division_lateral_superior = DIVISIONES.IZQUIERDA
            division_lateral_inferior = DIVISIONES.DERECHA
        else:
            division_lateral_superior = DIVISIONES.DERECHA
            division_lateral_inferior = DIVISIONES.IZQUIERDA

        for i in range(inicio, final):

            if derecha:
                columna += 1
            else:
                columna -= 1

            if abajo:  # itera hacia abajo
                fila = i
            else:  # itera hacia arriba
                fila = final - i - 1

            # corroboro no estar iterando fuera de los límites del tablero
            if (derecha and columna > 9) or (not derecha and columna < 0):
                return False

            casillero = self.tablero.casilleros[columna][fila]

            if (casillero.paredes[DIVISIONES.SUPERIOR] and casillero.paredes[division_lateral_superior]) \
                    or (casillero.paredes[DIVISIONES.INFERIOR] and casillero.paredes[division_lateral_inferior]):
                return False

            if casillero.esta_ocupado:
                return columna, fila

        return False
