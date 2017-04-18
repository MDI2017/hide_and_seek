from pygame_functions import *
from tablero.tablero import Tablero
from constantes import *
from dado.dado import dado


screenSize(730, 720)
setBackgroundColour(COLORES.BLANCO)

tablero = Tablero()
tablero.dibujarCasilleros()
tablero.dibujarDivisiones()

movRestantes = dado()

endWait()