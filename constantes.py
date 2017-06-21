import os


class CASILLAS:
    LADO = 60
    FILA = 1
    COLUMNA = 0

class ESTADOS:
    ESTA_OCUPADO = True
    TIENE_MURO = True


class ESTADOS_BOTONES:
    ACTIVO = 0
    PRESIONADO = 1
    INACTIVO = 2


class DIVISIONES:
    SUPERIOR = 0
    DERECHA = 1
    INFERIOR = 2
    IZQUIERDA = 3


class COLORES:
    PIEDRA_LIBRE = (0, 121, 107)
    ZONA_PROHIBIDA = (117, 117, 117)
    ZONA_ESPCAPE = (178, 223, 219)
    ZONA_LARGADA = (178, 223, 219)
    ZONA_LIBERTAD = (0, 121, 107)
    MUROS = (33, 33, 33)

    ROJO = "red"
    AZUl = "blue"
    AMARILLO = "yellow"
    BLANCO = (255, 255, 255)
    DARK_PRIMARY = (0, 121, 107)
    PRIMARY = (0, 150, 136)
    LIGTH_PRIMARY = (178, 223, 219)
    ACCENT = (0, 188, 212)
    PRIMARY_TEXT = (33, 33, 33)
    SECONDARY_TEXT = (117, 117, 117)
    DIVIDER = (189, 189, 189)


class ZONAS:
    FUERA_TABLERO = 100
    LIBERTAD = 200
    PROHIBIDA = 300
    ESCAPE = 400
    LARGADA = 500
    PERRITO_GUARDIAN = 4
    DOBLE_LANZAMIENTO = 7
    PIEDRA_LIBRE = 700


class PATHS:
    PATH_JUEGO = os.getcwd()
    PATH_IMAGENES = PATH_JUEGO + os.sep + "images" + os.sep


class FONT_SIZE:
    GRANDE = 32
    MEDIANO = 16
    CHICO = 32


class SEPARACIONES:
    SEPARACION = 8
    PADDING_VENTANA_PPAL = 16


class RECT:
    POS_X = 0
    POS_Y = 1
    ANCHO = 2
    ALTO = 3
