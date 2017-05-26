from constantes import RECT


class Clickeable:
    @staticmethod
    def click_elemento(posicion_mouse, posicion_x, posicion_y, alto, ancho):
        """
        Esta funcion recibe un tupla con un con las coordenadas de el lugar donde el mouse hizo click
        :param posicion:  
        :return: 
        """

        if not posicion_mouse:
            return False

        return Clickeable._clickeado(posicion_mouse, posicion_x, posicion_x + ancho, posicion_y, posicion_y + alto)

    @staticmethod
    def click_sprite(posicion_mouse, rect_sprite):
        if not posicion_mouse:
            return False
        x_final = rect_sprite[RECT.POS_X] + rect_sprite[RECT.ANCHO]
        y_final = rect_sprite[RECT.POS_Y] + rect_sprite[RECT.ALTO]
        return Clickeable._clickeado(posicion_mouse, rect_sprite[RECT.POS_X], x_final, rect_sprite[RECT.POS_Y], y_final)

    @staticmethod
    def _clickeado(posicion_mouse, x_inicial, x_final, y_inicial, y_final):
        return x_inicial < posicion_mouse[0] < x_final and y_inicial < posicion_mouse[1] < y_final
