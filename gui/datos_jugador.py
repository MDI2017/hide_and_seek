from pygame_functions import *
from gui.input_clickleable import Input
from gui.button import Button
from constantes import PATHS, FONT_SIZE, SEPARACIONES

POS_X = 0
POS_Y = 1
ALTO = 2
ANCHO = 3

LARGO_INPUT = 250

FUENTE_GRILLA = FONT_SIZE.MEDIANO

class GrillaJugador:

    ALTO_GRILLA = FUENTE_GRILLA * 1.7

    def __init__(self, posX, posY, dibujada=False):
        self.posX = posX
        self.posY = posY
        self.dibujada = dibujada
        self.botonBorrar = None
        self.textBox = None
        self.botonBorrarRect = None

    def dibujar_grilla(self):
        self.__dibujar_boton_borrar()
        self._dibujar_textbox()
        self.dibujada = True

    def _dibujar_textbox(self):

        posicion_x_text_box = self.botonBorrarRect[POS_X] + self.botonBorrarRect[ANCHO] + SEPARACIONES.SEPARACION
        posicion_y_text_box = self.posY
        self.textBox = Input(posicion_x_text_box, posicion_y_text_box, LARGO_INPUT, 0, "Nombre jugador", 0, FUENTE_GRILLA)

    def __dibujar_boton_borrar(self):
        self.botonBorrar = makeSprite(PATHS.PATH_IMAGENES + "boton_borrar.png")
        moveSprite(self.botonBorrar, self.posX, self.posY)
        self.botonBorrarRect = self.botonBorrar.rect
        showSprite(self.botonBorrar)
