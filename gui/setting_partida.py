from .button import Button
from .grilla_jugador import GrillaJugador
import pygame
from pygame_functions import *
from constantes import SEPARACIONES, RECT
import random
from gui.seleccion_avatars import Avatars


class SettingPartida:
    """
    Clase que genera la pantalla inicial de la partida: grilla, botones, seleccion de avatars. Esta clase se encarga de
    que podamos agregar hasta 5 jugadores, borrar estos jugadores hasta 2 (menos no permitido), elegir jugadores aleatoreamente,
    y nos da la opcion de iniciar partida.
    """
    def __init__(self):
        self.jugadores = []
        self.grillas = [GrillaJugador(SEPARACIONES.PADDING_VENTANA_PPAL, SEPARACIONES.PADDING_VENTANA_PPAL),
                        GrillaJugador(SEPARACIONES.PADDING_VENTANA_PPAL, 80)]

        self.botonAgregarJugador = None
        self.botonCazadorAleatorio = None
        self.botonComenzarPartida = None
        self.avatarSeleccionado = [False, False, False, False, False, False, False, False, False]

    def mostrar_pantalla_sentting(self):
        pygame.display.set_caption("SETTING PARTIDA")
        self._dibujar_botones_accion()

        for grilla in self.grillas:
            grilla.dibujar_grilla()

        return self.__bucle_setting_partida()

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
                    if grilla.botonSeleccionAvatar.click_elemento(mouseAction) and grilla.avatar is None:
                            self._abrir_seleccion_avatar(indice)
                            break

                    if grilla.botonBorrar.click_elemento(mouseAction):
                        if len(self.grillas) > 2:
                            grilla.ocultar_grilla()
                            self.grillas.pop(indice)
                            self.mover_grilla(indice)
                            if grilla.avatar is not None:
                                self.avatarSeleccionado[int(grilla.avatar[6])-1] = False

                        if len(self.grillas) < 5 and self.botonAgregarJugador.inactivo:
                            self.botonAgregarJugador.activar()
                        break
                    if self.botonAgregarJugador.click_elemento(mouseAction):
                        self._agregar_grilla()
                        break
                    if self.botonCazadorAleatorio.click_elemento(mouseAction):
                        self.jugador_aleatorio()
                        break
                    if self.botonComenzarPartida.click_elemento(mouseAction):
                            return self._iniciar_partida()

    def verificar_seleccion_radio(self, grilla_seleccionada):

        for grilla in self.grillas:
            if grilla != grilla_seleccionada and grilla.radioButtonCazador.seleccionado:
                grilla.radioButtonCazador.quitar_seleccion()

            if grilla == grilla_seleccionada:
                if grilla.radioButtonCazador.seleccionado:
                    self.botonComenzarPartida.activar()
                else:
                    self.botonComenzarPartida.desactivar()

    def _abrir_seleccion_avatar(self, numero_jugador):
        avatar = Avatars(self.avatarSeleccionado)
        self.grillas[numero_jugador].botonSeleccionAvatar.ocultar()
        self.grillas[numero_jugador].dibujar_boton_selecion_avatar(avatar.nomAvatar)
        self.grillas[numero_jugador].avatar = avatar.nomAvatar
        avatar.fondo.ocultar()
        self.avatarSeleccionado = avatar.seleccionado

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

        posicion_y_iniciar_partida = self.botonCazadorAleatorio.rect[RECT.POS_Y] + \
                                     self.botonAgregarJugador.rect[RECT.ALTO] + SEPARACIONES.SEPARACION

        self.botonComenzarPartida = Button(posicion_x_botones, posicion_y_iniciar_partida,
                                           "boton_iniciar_partida_habilitado.png")
        self.botonComenzarPartida.agregar_imagen("boton_iniciar_partida_presionado.png")
        self.botonComenzarPartida.agregar_imagen("boton_iniciar_partida_desactivado.png")
        self.botonComenzarPartida.inactivo = True

        self.botonComenzarPartida.dibujar()

    def jugador_aleatorio(self, ):
        indice = random.randint(0, len(self.grillas) - 1)
        print(indice)
        self.grillas[indice].radioButtonCazador._al_liberar_click()
        self.verificar_seleccion_radio(self.grillas[indice])
        return indice

    def ocultar_setting(self):
        for grilla in self.grillas:
            grilla.ocultar_grilla()
            self.botonAgregarJugador.ocultar()
            self.botonCazadorAleatorio.ocultar()
            self.botonComenzarPartida.ocultar()

    def mover_grilla(self, indice):
        for i in range(indice, len(self.grillas)):
            # self.grillas[i].mover_grilla(64)
            posY = self.grillas[i].posY
            if self.grillas[i].textBox.texto is None:
                self.grillas[i].textBox.textBox.move(47, posY-64, True)
            else:
                moveLabel(self.grillas[i].textBox.label, 47, posY-64)
            self.grillas[i].botonSeleccionAvatar.mover(None, posY-73)
            self.grillas[i].botonBorrar.mover(None, posY-64)
            self.grillas[i].radioButtonCazador.mover(None,posY-58)

    def _iniciar_partida(self):
        hay_cazador = False
        datos_jugadores = []

        for grilla in self.grillas:
            datos_jugador = grilla.obtener_datos()
            if datos_jugador:
                datos_jugadores.append(grilla.obtener_datos())
                if datos_jugador['es_cazador']:
                    hay_cazador = True

        if hay_cazador and len(datos_jugadores) >= 2:
            return datos_jugadores
        else:
            print('no hay cazador')
