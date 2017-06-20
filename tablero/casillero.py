from pygame_functions import drawRect, drawLine
from constantes import *


class Casillero:
    """
    la clase Casillero es la responsable de contener las fichas de los jugadores
    """

    def __init__(self, lado, posicion_x, posicion_y,
                 libre=True, paredes=None, visible=True, ):

        if paredes is None:
            paredes = [0, 0, 0, 0]

        self.lado = lado
        self.posicionX = posicion_x
        self.posicionY = posicion_y
        self.libre = libre
        self.visible = visible
        self.paredes = paredes
        self.color = COLORES.BLANCO
        self.zona = None

    def dibujarCasillero(self):
        """
        Método responsable de dibujar los casilleros dentro del área del tablero
         
        """
        self._pintarSuperficie()

    def dibujarDivisiones(self):

        if self.zona != ZONAS.FUERA_TABLERO:
            self._dibujarDivisionDerecha()
            self._dibujarDivicionSuperior()
            self._dibujarDivicionInferior()
            self._dibujarDivisionIzquierda()

    def _dibujarDivicionSuperior(self):
        ancho_division = 1
        color = COLORES.MUROS
        punto_x_inicial = self.posicionX
        punto_y_inicial = self.posicionY
        punto_x_final = punto_x_inicial + self.lado
        punto_y_final = punto_y_inicial

        if self.paredes[DIVISIONES.SUPERIOR]:
            ancho_division = 5

        elif self.zona == ZONAS.DOBLE_LANZAMIENTO:
            color = COLORES.ROJO
            ancho_division = 3

        drawLine(punto_x_inicial, punto_y_inicial, punto_x_final, punto_y_final, color, ancho_division)

    def _dibujarDivisionDerecha(self):
        ancho_division = 1
        punto_x_inicial = self.posicionX + self.lado
        punto_y_inicial = self.posicionY
        punto_x_final = punto_x_inicial
        punto_y_final = punto_y_inicial + self.lado

        if self.paredes[DIVISIONES.DERECHA]:
            ancho_division = 5

        drawLine(punto_x_inicial, punto_y_inicial, punto_x_final, punto_y_final, COLORES.MUROS, ancho_division)

    def _dibujarDivicionInferior(self):
        ancho_division = 1
        color = COLORES.MUROS
        punto_x_inicial = self.posicionX
        punto_y_inicial = self.posicionY + self.lado
        punto_x_final = punto_x_inicial + self.lado
        punto_y_final = punto_y_inicial

        if self.paredes[DIVISIONES.INFERIOR]:
            ancho_division = 5

        elif self.zona == ZONAS.PERRITO_GUARDIAN:
            color = COLORES.AZUl
            ancho_division = 3

        drawLine(punto_x_inicial, punto_y_inicial, punto_x_final, punto_y_final, color, ancho_division)

    def _dibujarDivisionIzquierda(self):
        ancho_division = 1
        punto_x_inicial = self.posicionX
        punto_y_inicial = self.posicionY
        punto_x_final = punto_x_inicial
        punto_y_final = punto_y_inicial + self.lado

        if self.paredes[DIVISIONES.IZQUIERDA]:
            ancho_division = 5

        drawLine(punto_x_inicial, punto_y_inicial, punto_x_final, punto_y_final, COLORES.MUROS, ancho_division)

    def _pintarSuperficie(self):
        drawRect(self.posicionX, self.posicionY, self.lado, self.lado, self.color)

