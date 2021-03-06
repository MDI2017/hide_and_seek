import pygame

from gui.button import Button
from jugadores.cazador import Cazador
from jugadores.corredor import Corredor
from pygame_functions import clearShapes
from tablero.tablero import Tablero
from partida.dado import Dado
from pygame_functions import *
from constantes import DIVISIONES, ZONAS, CASILLAS, COLORES
from .turno import Turno


class Partida:
    """
    Clase encargada de dibujar el tablero, iniciar la partida, crear los jugadores (cazador y corredor/es), del 
    movimiento de las fichas durante cada turno y del cambio de turno.
    Esta clase es la que contiene las reglas del juego y la encargada de verificar cuando un jugador gano la partida
    
    """

    def __init__(self):

        self.tablero = Tablero()
        self.corredores = []
        self.cazador = None
        self.boton_atras = Button(880, 680, "boton_iniciar_partida_habilitado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_presionado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_desactivado.png")
        self.turno = None
        self.primer_turno = True
        self.linea_doble_turno = False
        self.dado = None
        self.info = None

    def iniciar_partida(self, jugadores):
        self.tablero.dibujar_tablero()
        self.turno = Turno(self.tablero)

        self.dado = Dado(670, 100)
        self.dado.dibujar()

        self.boton_atras.dibujar()
        self._crear_jugadores(jugadores)
        self.turno.cambio_turno(self.corredores[0])
        self.turno.set_movimientos(0)
        self.__bucle_partida()

    def _crear_jugadores(self, jugadores):
        for numero_jugador, data_jugador in enumerate(jugadores):

            if data_jugador['es_cazador']:
                casillero_cazador = self.tablero.casilleros[5][4]
                self.cazador = Cazador(data_jugador['nombre'], data_jugador['avatar'])
                self.cazador.crear_ficha(casillero_cazador)
            else:
                corredor = Corredor(data_jugador['nombre'], data_jugador['avatar'])
                self.corredores.append(corredor)
                pos_inicial = corredor.set_position(len(self.corredores) - 1)
                casillero_corredor = self.tablero.casilleros[pos_inicial[CASILLAS.COLUMNA]][pos_inicial[CASILLAS.FILA]]
                corredor.crear_ficha(casillero_corredor)

    def __bucle_partida(self):
        en_partida = True
        while en_partida:
            mouseAction = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseAction = pygame.mouse.get_pos()

                if event.type == pygame.KEYDOWN:
                    # Controla tecla Enter durante la partida
                    if event.key == pygame.K_RETURN:
                        self._enter_presionado()

                    # Controla las teclasr arrow del teclado durante la partida
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN \
                            or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self._arrow_presionado(event.key)

            if mouseAction:
                if self.boton_atras.dibujado and self.boton_atras.click_elemento(mouseAction):
                    self.tablero.renderizado = False
                    clearShapes()
                    self.cazador.ficha.ocultar()
                    for corredor in self.corredores:
                        corredor.ficha.ocultar()
                    self.boton_atras.ocultar()
                    hideLabel(self.info.movimientos)
                    self.dado.ocultar()
                    clearShapes()
                    en_partida = False

                if self.dado.dibujado and self.dado.click_elemento(mouseAction):
                    # self.turno.set_movimientos(1000)
                    self.turno.set_movimientos(self.dado.tirar_dado())
                    self._posibles_movimientos(self.turno.jugador.ficha.casillero)
                    pause(500)
                    self.dado.ocultar()

    def _enter_presionado(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self._fin_turno()
                        self._cambio_turno()
                        return

    def _arrow_presionado(self, tecla_precionada):
        """
        funcion que controla las acciones de las teclas arrow durante la partida. La función se ejecuta al momento de
        precionar alguna de las arrows del teclado y entra en un bucle esperando antes que se suelte para realizar una
        acción. En este caso, mover una ficha en el tablero.
        :param tecla_precionada: 
        :return: 
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == tecla_precionada:
                        self._mover_ficha(tecla_precionada)
                        return

    def _mover_ficha(self, direccion):
        """
        Funcion que recibe la dirección hacia la que se desea mover la ficha. Si el movimiento es posible, muefe la
        ficha al nuevo casillero. Caso contrario no realiza ninguna acción.
        :param direccion: 
        :return: 
        """

        columna_ficha = self.turno.jugador.ficha.casillero.indice[CASILLAS.COLUMNA]
        fila_ficha = self.turno.jugador.ficha.casillero.indice[CASILLAS.FILA]

        nuevo_casillero = None

        if direccion == pygame.K_UP:
            nuevo_casillero = self.tablero.casilleros[columna_ficha][fila_ficha - 1]

            if fila_ficha == 0:
                return False
            if self.tablero.casilleros[columna_ficha][fila_ficha].paredes[DIVISIONES.SUPERIOR]:
                return False
            elif nuevo_casillero.esta_ocupado:
                return False

        if direccion == pygame.K_DOWN:
            nuevo_casillero = self.tablero.casilleros[columna_ficha][fila_ficha + 1]

            if fila_ficha == 10:
                return False
            if self.tablero.casilleros[columna_ficha][fila_ficha].paredes[DIVISIONES.INFERIOR]:
                return False
            elif nuevo_casillero.esta_ocupado:
                return False

        if direccion == pygame.K_RIGHT:
            nuevo_casillero = self.tablero.casilleros[columna_ficha + 1][fila_ficha]

            if columna_ficha == 9:
                return False
            if self.tablero.casilleros[columna_ficha][fila_ficha].paredes[DIVISIONES.DERECHA]:
                return False
            elif nuevo_casillero.esta_ocupado:
                return False

        if direccion == pygame.K_LEFT:
            nuevo_casillero = self.tablero.casilleros[columna_ficha - 1][fila_ficha]

            if columna_ficha == 0:
                return False
            if self.tablero.casilleros[columna_ficha][fila_ficha].paredes[
                DIVISIONES.IZQUIERDA]:
                return False
            if nuevo_casillero.esta_ocupado:
                return False

        # Si todas las comprobaciones son exitosas, se mueve la ficha
        self.restore_casilleros(self.turno.jugador.ficha.casillero)
        self.turno.mover_ficha(nuevo_casillero)
        # Si aún quedan movimientos, se muestran los posibles movimientos que puede realizar
        if self.turno.jugador.ficha.movimientos > 0:
            self._posibles_movimientos(self.turno.jugador.ficha.casillero)

    def _posibles_movimientos(self, casillero):

        """
        Funcion que chequea los posibles movimientos de una ficha y señala esos casilleros
        :param casillero: 
        :return: 
        """
        columna_ficha = casillero.indice[CASILLAS.COLUMNA]
        fila_ficha = casillero.indice[CASILLAS.FILA]

        # Sanity check
        if fila_ficha == 0:
            casillero_superior = None
        else:
            casillero_superior = self.tablero.casilleros[columna_ficha][fila_ficha - 1]

        if columna_ficha == 9:
            casillero_derecha = None
        else:
            casillero_derecha = self.tablero.casilleros[columna_ficha + 1][fila_ficha]

        if fila_ficha == 11:
            casillero_inferior = None
        else:
            casillero_inferior = self.tablero.casilleros[columna_ficha][fila_ficha + 1]

        if columna_ficha == 0:
            casillero_izquierza = None
        else:
            casillero_izquierza = self.tablero.casilleros[columna_ficha - 1][fila_ficha]

        if casillero_superior \
                and not casillero_superior.paredes[DIVISIONES.INFERIOR] \
                and not casillero_superior.esta_ocupado \
                and fila_ficha > 0:
            casillero_superior.highlight()

        if casillero_derecha \
                and not casillero_derecha.paredes[DIVISIONES.IZQUIERDA] \
                and not casillero_derecha.esta_ocupado \
                and columna_ficha < 9:
            casillero_derecha.highlight()

        if casillero_inferior \
                and not casillero_inferior.paredes[DIVISIONES.SUPERIOR] \
                and not casillero_inferior.esta_ocupado \
                and fila_ficha < 10:
            casillero_inferior.highlight()

        if casillero_izquierza \
                and not casillero_izquierza.paredes[DIVISIONES.DERECHA] \
                and not casillero_izquierza.esta_ocupado \
                and columna_ficha > 0:
            casillero_izquierza.highlight()

    def restore_casilleros(self, casillero):

        """
        Vuelve al color normal los casilleros resaltados por self._posibles_movimientos()
        :param casillero: 
        :return: 
        """

        columna_ficha = casillero.indice[CASILLAS.COLUMNA]
        fila_ficha = casillero.indice[CASILLAS.FILA]

        # Sanity check
        if fila_ficha == 0:
            casillero_superior = None
        else:
            casillero_superior = self.tablero.casilleros[columna_ficha][fila_ficha - 1]

        if columna_ficha == 9:
            casillero_derecha = None
        else:
            casillero_derecha = self.tablero.casilleros[columna_ficha + 1][fila_ficha]

        if fila_ficha == 11:
            casillero_inferior = None
        else:
            casillero_inferior = self.tablero.casilleros[columna_ficha][fila_ficha + 1]

        if columna_ficha == 0:
            casillero_izquierza = None
        else:
            casillero_izquierza = self.tablero.casilleros[columna_ficha - 1][fila_ficha]

        if casillero_superior and casillero_superior.highlighted:
            casillero_superior.restore()

        if casillero_derecha and casillero_derecha.highlighted:
            casillero_derecha.restore()

        if casillero_inferior and casillero_inferior.highlighted:
            casillero_inferior.restore()

        if casillero_izquierza and casillero_izquierza.highlighted:
            casillero_izquierza.restore()

    def _cambio_turno(self):
        """
        Cambia de turno y saltea a cazador en la primera ronda.
        """

        if isinstance(self.turno.jugador, Cazador):
            self.turno.cambio_turno(self.corredores[0])
        else:
            numero_jugador = self.corredores.index(self.turno.jugador)

            if numero_jugador < len(self.corredores) - 1:
                self.turno.cambio_turno(self.corredores[numero_jugador + 1])
            else:
                self.turno.cambio_turno(self.cazador)

        self.turno.set_movimientos(0)
        self.dado.dibujar()

# TODO: Revisar usilidad de esta función
    def _chequear_zona(self, direccion):
        if direccion == pygame.K_DOWN:
            if self.tablero.casilleros[columna_ficha][fila_ficha].zona is ZONAS.PIEDRA_LIBRE:
                self.corredores[int(self.turno)].ficha.piso_piedra_libre = True
            if self.tablero.casilleros[columna_ficha][fila_ficha].zona is ZONAS.LIBERTAD and \
                            self.corredores[int(self.turno)].ficha.piso_piedra_libre is True:
                self.corredores.pop(int(self.turno))

    def _fin_turno(self):

        self.turno.fin_turno()
