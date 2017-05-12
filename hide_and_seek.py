from pygame_functions import *
from tablero.tablero import Tablero
from constantes import *
from gui.button import Button
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
while juego_iniciado:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()

    if not boton_dibujado:
        boton.dibujar()
        boton_dibujado = True

    if boton and boton.boton_precionado(mousePressed()):
        updateDisplay()
        print('preciono boton')
        renderizar_tablero = True
        boton = None

    if not tablero_renderizado and renderizar_tablero:
        print('tablero no renderizado')
        tablero.dibujarCasilleros()
        tablero.dibujarDivisiones()
        tablero_renderizado = True


endWait()