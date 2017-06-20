class Posicionable:
    """
    Clase que declara las posiciones que necesita y utiliza la grilla 
    """

    def __init__(self, posicion_x, posicion_y, ancho=None, alto=None):
        self.posicionX = posicion_x
        self.posicionY = posicion_y
        self.alto = alto
        self.ancho = ancho
