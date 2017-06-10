from pygame_functions import *
from tablero.tablero import Tablero
from constantes import *
from gui.button import Button
from gui.setting_partida import SettingPartida
from dado.dado import dado
from partida import Partida

screenSize(730, 720)
setBackgroundColour(COLORES.BLANCO)

# movRestantes = dado()

juego_iniciado = True
tablero_renderizado = False
renderizar_tablero = False
boton_dibujado = False
tablero = Tablero()
boton = Button(250, 250, "boton_iniciar_partida_habilitado.png")
boton.agregar_imagen("boton_iniciar_partida_presionado.png")
boton.agregar_imagen("boton_iniciar_partida_desactivado.png")

boton_atras = Button(670, 100, "boton_iniciar_partida_habilitado.png")
boton_atras.agregar_imagen("boton_iniciar_partida_presionado.png")
boton_atras.agregar_imagen("boton_iniciar_partida_desactivado.png")


# jugadores = [
#     {'nombre': "un nombre", 'numero': 2, 'es_contador': True},
#     {'nombre': "otro nombre", 'numero': 1, 'es_contador': False},
#     {'nombre': "mas nombre", 'numero': 4, 'es_contador': False}
#
# ]
#
# partida = Partida(jugadores)
#
# print(partida.jugadores)

setting = SettingPartida()

def dibujar_tablero():
    tablero.dibujarTablero()

def mostrar_setting():
    setting.mostrar_pantalla_sentting()

pygame.display.set_caption("VENTANA PRINCIPAL")


while juego_iniciado:
    """
    bucle principal del juego
    """
    # pygame.event.clear()
    # print(pygame.mouse.get_pressed())

    mouseAction = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseAction = pygame.mouse.get_pos()

    if not boton.dibujado and not tablero.renderizado:
        boton.dibujar()

    if boton.dibujado and boton.click_elemento(mouseAction):
        boton.ocultar()
        mostrar_setting()
        # dibujar_tablero()
        # boton_atras.dibujar()

    if boton_atras.dibujado and boton_atras.click_elemento(mouseAction):
        clearShapes()
        tablero.renderizado = False
        boton_atras.ocultar()
        boton.dibujar()

endWait()
