from pygame_functions import makeTextBox, showTextBox, textBoxInput, makeLabel, showLabel, hideLabel, hideTextBox,textboxGroup
from .clickeable import Clickeable
from constantes import RECT


class Input(Clickeable):
    def __init__(self, posicion_x, posicion_y, ancho, case=0,
                 place_holder="Ingrese un Texto", max_length=0, fuente=22, alto=None):
        super().__init__(posicion_x, posicion_y, ancho, alto)

        self.fuente = fuente
        self.maxLength = max_length
        self.placeHolder = place_holder
        self.case = case
        self.textBox = makeTextBox(self.posicionX, self.posicionY, self.ancho, self.case, self.placeHolder,
                                   self.maxLength, self.fuente)

        self.rect = (self.posicionX, self.posicionY, self.ancho, self.textBox.boxSize)
        self.xFinal = self.rect[RECT.POS_X] + self.rect[RECT.ANCHO]
        self.yFinal = self.rect[RECT.POS_Y] + self.rect[RECT.ALTO]

        self.label = None

        self.texto = None
        showTextBox(self.textBox)
        self._textBoxVisible = True

    def _al_liberar_click(self):

        self._mostrar_textBox()
        self.texto = None
        self.label = None

        self.texto = textBoxInput(self.textBox)
        self.label = makeLabel(self.texto, self.fuente, self.posicionX, self.posicionY)
        self._mostrar_label()


    def _mostrar_label(self):
        hideTextBox(self.textBox)
        showLabel(self.label)

    def _mostrar_textBox(self):
        hideLabel(self.label)
        showTextBox(self.textBox)
        print(self.textBox.rect)
        print(self.rect)

    def ocultarTextBox(self):
        textboxGroup.remove(self.textBox)

        
    def ocultarLabel(self):
        hideLabel(self.label)




