from pygame_functions import drawRect


class Casillero:
    """
    la clase Casillero es la responsable de contener las fichas de los jugadores
    """
    def __init__(self, lado, posicion_x, posicion_y):
        self.lado = lado
        self.posicionX = posicion_x
        self.posicionY = posicion_y
        self.ocupado = False

    def dibujarCasillero(self):
        """
        Método responsable de dibujar los casilleros dentro del área del tablero
        :return: 
        """
        print(self.posicionY)
        print(self.posicionX)
        drawRect(self.posicionX, self.posicionY, self.lado, self.lado, "blue", 1)
