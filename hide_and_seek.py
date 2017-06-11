from pygame_functions import *
from tablero.tablero import Tablero
from constantes import *
from gui.button import Button
from gui.setting_partida import SettingPartida
from dado.dado import dado
from partida.partida import Partida

screenSize(730, 720)
setBackgroundColour(COLORES.BLANCO)

# movRestantes = dado()

juego_iniciado = True
tablero_renderizado = False
renderizar_tablero = False
boton_dibujado = False
boton = Button(250, 250, "boton_iniciar_partida_habilitado.png")
boton.agregar_imagen("boton_iniciar_partida_presionado.png")
boton.agregar_imagen("boton_iniciar_partida_desactivado.png")


jugadores = [
    {'nombre': "Jugador 1", 'es_contador': True, 'avatar': "avatar1.png"},
    {'nombre': "Jugador 2", 'es_contador': False, 'avatar': "avatar2.png"},
    {'nombre': "Jugador 3", 'es_contador': False, 'avatar': "avatar3.png"},
    {'nombre': "Jugador 4", 'es_contador': False, 'avatar': "avatar4.png"},
    {'nombre': "Jugador 5", 'es_contador': False, 'avatar': "avatar5.png"}

]
#
partida = Partida()
#
# print(partida.jugadores)

setting = SettingPartida()

def iniciar_partida():
    global partida
    partida.iniciar_partida()
    jugadores = [
        {}
    ]

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

    if not boton.dibujado and not partida.tablero.renderizado:
        boton.dibujar()

    if boton.dibujado and boton.click_elemento(mouseAction):
        boton.ocultar()
        # mostrar_setting()
        iniciar_partida()

endWait()
