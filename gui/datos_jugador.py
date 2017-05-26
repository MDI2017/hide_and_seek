from pygame_functions import *
from gui.clickeable import Clickeable


class GrillaJugador:

    def __init__(self, posX, posY, dibujada=False):
        self.posX = posX
        self.posY = posY
        self.dibujada = dibujada
        self.textBox = makeTextBox(self.posX, self.posY, 300, 0, "Nombre jugador", 0, 32)

    def dibujar_grilla(self):
        self._dibujar_textbox()
        self.dibujada = True
        print(self.textBox.boxSize)

    def _dibujar_textbox(self):
         showTextBox(self.textBox)
         # textBoxInput(self.textBox)

    def imput_click(self, posicion_mouse):

        if Clickeable.elemento_precionado(posicion_mouse, self.posX, self.posY, 300, self.textBox.boxSize):
            nombre_jugador = textBoxInput(self.textBox)
            hideTextBox(self.textBox)
            label_nombre = makeLabel(nombre_jugador, 24, self.posX, self.posY + 5)
            showLabel(label_nombre)
