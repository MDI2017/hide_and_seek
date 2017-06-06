from .button import Button
from .datos_jugador import GrillaJugador
import pygame
from constantes import SEPARACIONES, RECT


class SettingPartida:
    def __init__(self):
        self.jugadores = []
        self.grillas = [GrillaJugador(SEPARACIONES.PADDING_VENTANA_PPAL, SEPARACIONES.PADDING_VENTANA_PPAL),
                        GrillaJugador(SEPARACIONES.PADDING_VENTANA_PPAL, 80)]

        self.botonAgregarJugador = None
        self.botonCazadorAleatorio = None
        self.botonComenzarPartida = None

    def mostrar_pantalla_sentting(self):
        pygame.display.set_caption("SETTING PARTIDA")
        self._dibujar_botones_accion()

        for grilla in self.grillas:
            grilla.dibujar_grilla()

        self.__bucle_setting_partida()

    def __bucle_setting_partida(self):

        while True:
            mouseAction = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseAction = pygame.mouse.get_pos()

            if mouseAction:
                for indice, grilla in enumerate(self.grillas):
                    if grilla.radioButtonCazador.click_elemento(mouseAction):
                        self.verificar_seleccion_radio(grilla)
                        break
                    if grilla.textBox.click_elemento(mouseAction):
                        break
                    if grilla.botonSeleccionAvatar.click_elemento(mouseAction):
                        self._abrir_seleccion_avatar(indice)
                        break
                    if grilla.botonBorrar.click_elemento(mouseAction):
                        if len(self.grillas) > 2:
                            self.grillas[-1].textBox.ocultarTextBox()
                            self.grillas[-1].textBox.ocultarLabel()
                            self.grillas[-1].botonSeleccionAvatar.ocultar()
                            self.grillas[-1].botonBorrar.ocultar()
                            self.grillas[-1].radioButtonCazador.ocultar()

                            self.grillas.pop()

                        if len(self.grillas) < 5 and self.botonAgregarJugador.inactivo:
                            self.botonAgregarJugador.activar()

                        break
                    if self.botonAgregarJugador.click_elemento(mouseAction):
                        self._agregar_grilla()
                        break
                    if self.botonCazadorAleatorio.click_elemento(mouseAction):
                        break
                    if self.botonComenzarPartida.click_elemento(mouseAction):
                        break

    def verificar_seleccion_radio(self, grilla_seleccionada):

        for grilla in self.grillas:
            if grilla != grilla_seleccionada and grilla.radioButtonCazador.seleccionado:
                grilla.radioButtonCazador.quitar_seleccion()

    def _abrir_seleccion_avatar(self, numero_jugador):
        print("aqui llamo a la funcion que abre la lista de avatars con el id: " + str(numero_jugador))

    def _agregar_grilla(self):

        indice_ultima_grilla = len(self.grillas) - 1

        pos_y_nueva_grilla = self.grillas[indice_ultima_grilla].posY + SEPARACIONES.SEPARACION + 56

        grilla = GrillaJugador(SEPARACIONES.PADDING_VENTANA_PPAL, pos_y_nueva_grilla)

        self.grillas.append(grilla)
        grilla.dibujar_grilla()

        if len(self.grillas) == 5:
            self.botonAgregarJugador.desactivar()

    def _dibujar_botones_accion(self):

        self.botonAgregarJugador = Button(300, SEPARACIONES.PADDING_VENTANA_PPAL,
                                          "boton_agregar_jugador_habilitado.png")
        self.botonAgregarJugador.agregar_imagen("boton_agregar_jugador_presionado.png")
        self.botonAgregarJugador.agregar_imagen("boton_agregar_jugador_desactivado.png")
        self.botonAgregarJugador.dibujar()

        posicion_x_botones = pygame.display.Info().current_w - self.botonAgregarJugador.rect[
            RECT.ANCHO] - SEPARACIONES.PADDING_VENTANA_PPAL
        self.botonAgregarJugador.mover(pos_x=posicion_x_botones)

        posicion_y_cazador_aleatorio = self.botonAgregarJugador.rect[RECT.POS_Y] + self.botonAgregarJugador.rect[
            RECT.ALTO] + SEPARACIONES.SEPARACION

        self.botonCazadorAleatorio = Button(posicion_x_botones, posicion_y_cazador_aleatorio,
                                            "boton_cazador_aleatorio_habilitado.png")
        self.botonCazadorAleatorio.agregar_imagen("boton_cazador_aleatorio_presionado.png")
        self.botonCazadorAleatorio.agregar_imagen("boton_cazador_aleatorio_desactivado.png")
        self.botonCazadorAleatorio.dibujar()

        posicion_y_iniciar_partida = self.botonCazadorAleatorio.rect[RECT.POS_Y] + self.botonAgregarJugador.rect[
            RECT.ALTO] + SEPARACIONES.SEPARACION

        self.botonComenzarPartida = Button(posicion_x_botones, posicion_y_iniciar_partida,
                                           "boton_iniciar_partida_habilitado.png")
        self.botonComenzarPartida.agregar_imagen("boton_iniciar_partida_presionado.png")
        self.botonComenzarPartida.agregar_imagen("boton_iniciar_partida_desactivado.png")
        self.botonComenzarPartida.dibujar()


