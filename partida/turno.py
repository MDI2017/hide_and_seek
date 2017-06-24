from jugadores.cazador import Cazador
from constantes import CASILLAS, DIVISIONES


class Turno:
    def __init__(self, jugador, tablero):
        self.jugador = jugador
        self.tablero = tablero

    def fin_turno(self):
        if isinstance(self.jugador, Cazador):
            self._verificar_avistaje()

    def _verificar_avistaje(self):
        casillero_cazador = self.jugador.ficha.casillero

        # Iterecion desde la pocición del cazador hacia abajo
        for fila in range(casillero_cazador[CASILLAS.FILA] + 1, 12):
            casillero = self.tablero.casilleros[casillero_cazador[CASILLAS.COLUMNA]][fila]
            if casillero.esta_ocupado:
                print('avistaje')
                print(str(casillero_cazador[CASILLAS.COLUMNA]), str(fila))
                break

            if casillero.paredes[DIVISIONES.INFERIOR]:
                print('pared')
                print(str(casillero_cazador[CASILLAS.COLUMNA]), str(fila))
                break

        # Iterecion desde la pocición del cazador hacia arriba
        for i in range(0, casillero_cazador[CASILLAS.FILA]):
            indice_filas = casillero_cazador[CASILLAS.FILA] - 1 - i

            casillero = self.tablero.casilleros[casillero_cazador[CASILLAS.COLUMNA]][indice_filas]

            if casillero.esta_ocupado:
                print('avistaje')
                print(str(casillero_cazador[CASILLAS.COLUMNA]), str(indice_filas))
                break

            if casillero.paredes[DIVISIONES.SUPERIOR]:
                print('pared')
                print(str(casillero_cazador[CASILLAS.COLUMNA]), str(indice_filas))
                break

        # Iterecion desde la pocición del cazador hacia derecha
        for columna in range(casillero_cazador[CASILLAS.COLUMNA] + 1, 10):
            casillero = self.tablero.casilleros[columna][casillero_cazador[CASILLAS.FILA]]

            if casillero.esta_ocupado:
                print('avistaje')
                print(str(casillero_cazador[columna]), str(casillero_cazador[CASILLAS.FILA]))
                break

            if casillero.paredes[DIVISIONES.DERECHA]:
                print('pared')
                print('columna', str(columna))
                print('fila', str(CASILLAS.FILA))
                print(str(columna), str(casillero_cazador[CASILLAS.FILA]))
                break

        # Iterecion desde la pocición del cazador hacia izquierda
        for i in range(0, casillero_cazador[CASILLAS.COLUMNA]):
            indice_columnas = casillero_cazador[CASILLAS.COLUMNA] - 1 - i
            casillero = self.tablero.casilleros[indice_columnas][casillero_cazador[CASILLAS.FILA]]

            if casillero.esta_ocupado:
                print('avistaje')
                print(str(casillero_cazador[indice_columnas]), str(casillero_cazador[CASILLAS.FILA]))
                break

            if casillero.paredes[DIVISIONES.IZQUIERDA]:
                print('pared')
                print(str(indice_columnas), str(casillero_cazador[CASILLAS.FILA]))
                break

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
