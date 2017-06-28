from jugadores.cazador import Cazador
from constantes import CASILLAS, DIVISIONES, TABLERO


class Turno:
    def __init__(self, tablero):
        self.tablero = tablero
        self.jugador = None
        self.primer_turno = True

    def fin_turno(self):
        if isinstance(self.jugador, Cazador):
            self._verificar_avistaje()

    def _vertical_verification(self, inicio, final, abajo=False):
        columna = self.jugador.ficha.casillero[CASILLAS.COLUMNA]

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
        fila = self.jugador.ficha.casillero[CASILLAS.FILA]

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

    def _verificar_avistaje(self):
        casillero_cazador = self.jugador.ficha.casillero

        print('avistaje vertical inferior')
        self._vertical_verification(casillero_cazador[CASILLAS.FILA] + 1, TABLERO.FILAS, True)

        print('avistaje vertical superior')
        self._vertical_verification(TABLERO.INICIO, casillero_cazador[CASILLAS.FILA])

        self._horizontal_verification(casillero_cazador[CASILLAS.COLUMNA] + 1, TABLERO.COLUMNAS, True)

        self._horizontal_verification(TABLERO.INICIO, casillero_cazador[CASILLAS.COLUMNA])

        # Iterecion diagonal inferior derecha desde la pocición del cazador
        columna = casillero_cazador[CASILLAS.COLUMNA] + 1
        for fila in range(casillero_cazador[CASILLAS.FILA] + 1, 12):
            if columna > 9:
                break

            casillero = self.tablero.casilleros[columna][fila]
            if casillero.esta_ocupado:
                print('avistaje')
                print(str(columna), str(fila))
                break

            if (casillero.paredes[DIVISIONES.SUPERIOR] and casillero.paredes[DIVISIONES.IZQUIERDA]) \
                    or (casillero.paredes[DIVISIONES.INFERIOR] and casillero.paredes[DIVISIONES.DERECHA]):
                print('pared')
                print(str(columna), str(casillero_cazador[fila]))
                break
            columna += 1

        # Iterecion diagonal inferior izquierda desde la pocición del cazador
        columna = casillero_cazador[CASILLAS.COLUMNA] - 1
        for fila in range(casillero_cazador[CASILLAS.FILA] + 1, 12):
            if columna < 0:
                break

            casillero = self.tablero.casilleros[columna][fila]
            if casillero.esta_ocupado:
                print('avistaje')
                print(str(columna), str(fila))
                break

            if (casillero.paredes[DIVISIONES.SUPERIOR] and casillero.paredes[DIVISIONES.DERECHA]) \
                    or (casillero.paredes[DIVISIONES.INFERIOR] and casillero.paredes[DIVISIONES.IZQUIERDA]):
                print('pared')
                print(str(columna), str(fila))
                break
            columna -= 1

        # Iterecion diagonal superior derecha desde la pocición del cazador
        columna = casillero_cazador[CASILLAS.COLUMNA] + 1
        for i in range(0, casillero_cazador[CASILLAS.FILA]):
            if columna > 9:
                break
            indice_filas = casillero_cazador[CASILLAS.FILA] - 1 - i

            casillero = self.tablero.casilleros[columna][indice_filas]
            if casillero.esta_ocupado:
                print('avistaje')
                print(str(columna), str(indice_filas))
                break

            if (casillero.paredes[DIVISIONES.INFERIOR] and casillero.paredes[DIVISIONES.IZQUIERDA]) or \
                    (casillero.paredes[DIVISIONES.SUPERIOR] and casillero.paredes[DIVISIONES.DERECHA]):
                print('pared')
                print(str(columna), str(indice_filas))
                break
            columna += 1

        # Iterecion diagonal superior izquierda desde la pocición del cazador
        columna = casillero_cazador[CASILLAS.COLUMNA] - 1
        for i in range(0, casillero_cazador[CASILLAS.FILA]):
            if columna < 0:
                break
            indice_filas = casillero_cazador[CASILLAS.FILA] - 1 - i

            casillero = self.tablero.casilleros[columna][indice_filas]
            if casillero.esta_ocupado:
                print('avistaje')
                print(str(columna), str(indice_filas))
                break

            if (casillero.paredes[DIVISIONES.INFERIOR] and casillero.paredes[DIVISIONES.DERECHA]) \
                    or (casillero.paredes[DIVISIONES.SUPERIOR] and casillero.paredes[DIVISIONES.IZQUIERDA]):
                print('pared')
                print(str(columna), str(indice_filas))
                break
            columna -= 1
