from pygame_functions import *


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

