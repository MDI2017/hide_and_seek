from pygame_functions import *
from gui.input_clickleable import Input
from gui.button import Button
from gui.radio_button import RadioButton
from constantes import PATHS, FONT_SIZE, SEPARACIONES

POS_X = 0
POS_Y = 1
ANCHO = 2
ALTO = 3

LARGO_INPUT = 250
FUENTE_GRILLA = FONT_SIZE.MEDIANO
ALTO_GRILLA = FUENTE_GRILLA * 1.7


class GrillaJugador:
    def __init__(self, posX, posY, alto_grilla=40, dibujada=False):
        self.altoGrilla = alto_grilla
        self._mediaGrilla = self.altoGrilla / 2
        self.posX = posX
        self.posY = posY
        self.dibujada = dibujada
        self.botonBorrar = None
        self.textBox = None
        self.botonSeleccionAvatar = None
        self.radioButtonCazador = None
        self.avatar = None

    def dibujar_grilla(self):
        self.__dibujar_boton_borrar()
        self._dibujar_textbox()
        self._dibujar_boton_selecion_avatar()
        self._dibujar_radio_button()
        self.dibujada = True

    def _dibujar_textbox(self):
        posicion_x_text_box = self.botonBorrar.rect[POS_X] + self.botonBorrar.rect[ANCHO] + SEPARACIONES.SEPARACION
        posicion_y_text_box = self.posY + (self._mediaGrilla - ALTO_GRILLA / 2)
        self.textBox = Input(posicion_x_text_box, posicion_y_text_box, LARGO_INPUT, 0, "Nombre jugador", 0,
                             FUENTE_GRILLA)

    def __dibujar_boton_borrar(self):
        self.botonBorrar = Button(self.posX, self.posY, "boton_borrar_habilitado.png")
        self.botonBorrar.agregar_imagen("boton_borrar_presionado.png")
        self.botonBorrar.agregar_imagen("boton_borrar_desactivado.png")
        self.botonBorrar.dibujar()
        posicion_y_boton = self.posY + (self._mediaGrilla - self.botonBorrar.rect[ALTO] / 2)
        self.botonBorrar.mover(pos_y=posicion_y_boton)

    def _dibujar_boton_selecion_avatar(self):
        posicion_x_boton = self.textBox.rect[POS_X] + self.textBox.rect[ANCHO] + SEPARACIONES.SEPARACION
        posicion_y_boton = self.posY
        self.botonSeleccionAvatar = Button(posicion_x_boton, posicion_y_boton, "no_avatar.png")
        self.botonSeleccionAvatar.dibujar()
        posicion_y_boton = self.posY + (self._mediaGrilla - self.botonSeleccionAvatar.rect[ALTO] / 2)
        self.botonSeleccionAvatar.mover(pos_y=posicion_y_boton)

    def _dibujar_radio_button(self):
        posicion_x_boton = self.botonSeleccionAvatar.rect[POS_X] + self.botonSeleccionAvatar.rect[
            ANCHO] + SEPARACIONES.SEPARACION
        posicion_y_boton = self.posY
        self.radioButtonCazador = RadioButton(posicion_x_boton, posicion_y_boton, "radio_cazador_no_seleccionado.png")
        self.radioButtonCazador.agregar_imagen("radio_cazador_seleccionado.png")
        self.radioButtonCazador.dibujar()
        posicion_y_boton = self.posY + (self._mediaGrilla - self.radioButtonCazador.rect[ALTO] / 2)
        self.radioButtonCazador.mover(pos_y=posicion_y_boton)

    def obtener_datos(self):
        if not self.textBox.texto:
            return None

        return {
            'nombre': self.textBox.texto,
            'es_cazador': self.radioButtonCazador.seleccionado,
            'avatar': self.avatar,
        }
