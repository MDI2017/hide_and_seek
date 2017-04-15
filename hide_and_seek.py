from pygame_functions import *
from tablero.tablero import Tablero

screenSize(600, 720)
setBackgroundColour("red")

tablero = Tablero()

tablero.dibujarCasilleros()


endWait()