from pygame_functions import *
from tablero.tablero import Tablero
from constantes import *

screenSize(600, 720)
setBackgroundColour(COLORES.BLANCO)

tablero = Tablero()
tablero.dibujarCasilleros()
tablero.dibujarDivisiones()

endWait()