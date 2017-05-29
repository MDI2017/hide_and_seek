from .button import Button
from .datos_jugador import GrillaJugador
import pygame
from constantes import SEPARACIONES


class SettingPartida:
    def __init__(self):
        self.jugadores = []
        self.grillas = [GrillaJugador(100, 100),
                        GrillaJugador(100, 180),
                        GrillaJugador(100, 260),
                        GrillaJugador(100, 340),
                        ]

    def mostrar_pantalla_sentting(self):
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

    def verificar_seleccion_radio(self, grilla_seleccionada):

        for grilla in self.grillas:
            if grilla != grilla_seleccionada and grilla.radioButtonCazador.seleccionado:
                grilla.radioButtonCazador.quitar_seleccion()

    def _abrir_seleccion_avatar(self, numero_jugador):
        print("aqui llamo a la funcion que abre la lista de avatars con el id: " + str(numero_jugador))
