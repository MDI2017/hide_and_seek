from pygame_functions import *
from gui.clickeable import Clickeable
from constantes import PATHS, FONT_SIZE, SEPARACIONES
from gui.button import Button

POS_X = 0
POS_Y = 1
ALTO = 2
ANCHO = 3

LARGO_INPUT = 250




class GrillaJugador:

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
        print(self.botonBorrarRect)
        print(self.posX)
        print(SEPARACIONES.SEPARACION)

        posicion_x_text_box = self.botonBorrarRect[POS_X] + self.botonBorrarRect[ANCHO] + SEPARACIONES.SEPARACION
        posicion_y_text_box = self.posY
        self.textBox = makeTextBox(posicion_x_text_box, posicion_y_text_box, LARGO_INPUT, 0, "Nombre jugador", 0, FONT_SIZE.MEDIANO)
        showTextBox(self.textBox)
        # textBoxInput(self.textBox)

    def imput_click(self, posicion_mouse):

        if Clickeable.click_elemento(posicion_mouse, self.posX, self.posY, LARGO_INPUT, self.textBox.boxSize):
            nombre_jugador = textBoxInput(self.textBox)
            hideTextBox(self.textBox)
            label_nombre = makeLabel(nombre_jugador, FONT_SIZE.MEDIANO, self.posX + 60, self.posY)
            showLabel(label_nombre)

    def __dibujar_boton_borrar(self):
        self.botonBorrar = makeSprite(PATHS.PATH_IMAGENES + "boton_borrar.png")
        moveSprite(self.botonBorrar, self.posX, self.posY)
        self.botonBorrarRect = self.botonBorrar.rect
        showSprite(self.botonBorrar)
