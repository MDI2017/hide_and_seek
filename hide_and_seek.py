from pygame_functions import *
from tablero.tablero import Tablero
from constantes import *
from gui.button import Button
from gui.datos_jugador import GrillaJugador
from dado.dado import dado

screenSize(730, 720)
setBackgroundColour(COLORES.BLANCO)

# movRestantes = dado()

juego_iniciado = True
tablero_renderizado = False
renderizar_tablero = False
boton_dibujado = False
tablero = Tablero()
boton = Button(250, 250, 200, 100)
boton_atras = Button(670, 100, 100, 100)

grilla_1 = GrillaJugador(250, 100)
grilla_2 = GrillaJugador(250, 200)


def dibujar_tablero():
    tablero.dibujarTablero()


while juego_iniciado:

    mouseAction = mousePressed()

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()

    if not grilla_1.dibujada:
        grilla_1.dibujar_grilla()

    if not grilla_2.dibujada:
        grilla_2.dibujar_grilla()


    if not boton.dibujado and not tablero.renderizado:
        boton.dibujar()

    if boton.dibujado and boton.boton_precionado(mouseAction):
        clearShapes()
        boton.dibujado = False
        dibujar_tablero()
        boton_atras.dibujar()

        boton.dibujado = False

    grilla_1.imput_click(mouseAction)
    grilla_2.imput_click(mouseAction)


    # boton_atras.boton_precionado((730, 110 ))
    if boton_atras.dibujado and boton_atras.boton_precionado(mouseAction):
        clearShapes()
        tablero.renderizado = False
        boton_atras.dibujado = False
        boton.dibujar()



endWait()
