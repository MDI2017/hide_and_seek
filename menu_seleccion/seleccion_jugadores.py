from pygame_functions import *
from constantes import *


class GrillaSeleccion:
    def nuevoJugador(self, posX, posY):
        self.posX = posX
        self.posY = posY
        nombre = makeTextBox(posX, posY, 300, 0, "Nombre jugador", 0, 24)
        showTextBox(nombre)
        jugador = textBoxInput(nombre)
        print(jugador)
        hideTextBox(nombre)
        nomPantalla = makeLabel(jugador, 24, posX, posY + 5)
        showLabel(nomPantalla)

    def grilla(self):
        screenSize(730, 720)
        setBackgroundColour(COLORES.BLANCO)
        x, y = 10, 80
        botonJugador = makeSprite("Nuevo Jugador.png")
        moveSprite(botonJugador,x,1)
        showSprite(botonJugador)
        while x==10:
            if spriteClicked(botonJugador):
                hideSprite(botonJugador)
                for item in range(1, 6):
                    GrillaSeleccion().nuevoJugador(x, y)
                    y += 30



        endWait()



