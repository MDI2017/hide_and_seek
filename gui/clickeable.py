from .posicionable import Posicionable


class Clickeable:


    @staticmethod
    def elemento_precionado (posicion_mouse, posicion_x, posicion_y, alto, ancho):
        """
        Esta funcion recibe un tupla con un con las coordenadas de el lugar donde el mouse hizo click
        :param posicion:  
        :return: 
        """

        if not posicion_mouse:
            return False

        if posicion_x < posicion_mouse[0] < posicion_x + alto \
                and posicion_y < posicion_mouse[1] < posicion_y + ancho:
            return True
