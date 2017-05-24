
import os, sys, webbrowser, platform
from tkinter import *
from tkinter import ttk, font, messagebox




class DropMenu():

    # DECLARAR MÉTODO CONSTRUCTOR DE LA APLICACIÓN

    def __init__(self, img_carpeta, iconos):
        ''' Definir ventana de la aplicación, menú, submenús, 
            menú contextual, barra de herramientas, barra de
            estado y atajos del teclado '''

        # INICIALIZAR VARIABLES

        self.img_carpeta = img_carpeta
        self.iconos = iconos

        # DEFINIR VENTANA DE LA APLICACIÓN:

        self.raiz = Tk()

        # ESTABLECER PROPIEDADES DE LA VENTANA DE APLICACIÓN:

        self.raiz.title("Hide and Seek " )  # Título
        self.icono1 = PhotoImage(file=self.iconos[0])  # Icono app
        self.raiz.iconphoto(self.raiz, self.icono1)  # Asigna icono app
        self.raiz.option_add("*Font", "Helvetica 12")  # Fuente predeterminada
        self.raiz.option_add('*tearOff', False)  # Deshabilita submenús flotantes
        self.raiz.attributes('-fullscreen', True)  # Maximiza ventana completa
        self.raiz.minsize(400, 300)  # Establece tamaño minimo ventana

        # ESTABLECER ESTILO FUENTE PARA ALGUNOS WIDGETS:

        self.fuente = font.Font(weight='normal')  # normal, bold, etc...

        # DECLARAR VARIABLES PARA OPCIONES PREDETERMINADAS:
        # (Estos valores se podrían leer de un archivo de
        # configuración)

        self.CFG_TIPOCONEX = IntVar()
        self.CFG_TIPOCONEX.set(1)  # shh
        self.CFG_TIPOEMUT = IntVar()
        self.CFG_TIPOEMUT.set(1)  # xterm
        self.CFG_TIPOEXP = IntVar()
        self.CFG_TIPOEXP.set(1)  # thunar

        # DECLARAR VARIABLE PARA MOSTRAR BARRA DE ESTADO:

        self.estado = IntVar()
        self.estado.set(1)  # Mostrar Barra de Estado

        # DEFINIR BARRA DE MENÚ DE LA APLICACION:

        barramenu = Menu(self.raiz)
        self.raiz['menu'] = barramenu

        # DEFINIR SUBMENÚS 'Avatars', 'Opciones' y 'Ayuda':

        menu1 = Menu(barramenu)
        self.menu2 = Menu(barramenu)
        menu3 = Menu(barramenu)
        barramenu.add_cascade(menu=menu1, label='Avatars')
        barramenu.add_cascade(menu=self.menu2, label='Opciones')
        barramenu.add_cascade(menu=menu3, label='Ayuda')

        # DEFINIR SUBMENÚ 'Avatars':

        icono2 = PhotoImage(file=self.iconos[1])
        icono3 = PhotoImage(file=self.iconos[2])

        menu1.add_command(label='Avatar 1',
                          command=self.f_conectar,
                          underline=0, accelerator="Ctrl+c",
                          image=icono2, compound=LEFT)
        menu1.add_separator()  # Agrega un separador
        menu1.add_command(label='Avatar 2',
                          command=self.f_conectar,
                          underline=0, accelerator="Ctrl+c",
                          image=icono2, compound=LEFT)
        menu1.add_separator()
        menu1.add_command(label='Avatar 3',
                          command=self.f_conectar,
                          underline=0, accelerator="Ctrl+c",
                          image=icono2, compound=LEFT)
        menu1.add_separator()
        menu1.add_command(label='Salir', command=self.f_salir,
                          underline=0, accelerator="Ctrl+q",
                          image=icono3, compound=LEFT)

        # DEFINIR SUBMENÚ 'Opciones':



        # DEFINIR SUBMENÚ 'Ayuda':

        menu3.add_command(label='Web', command=self.f_web)



        # DEFINIR BARRA DE ESTADO:
        # Muestra información del equipo

        info1 = platform.system()
        info2 = platform.node()
        info3 = platform.machine()

        # Otro modo de obtener la información:
        # (No disponible en algunas versiones de Windows)

        # info1 = os.uname().sysname
        # info2 = os.uname().nodename
        # info3 = os.uname().machine



        # DEFINIR MENU CONTEXTUAL

        self.menucontext = Menu(self.raiz, tearoff=0)


        # DECLARAR TECLAS DE ACCESO RAPIDO:

        self.raiz.bind("<Control-c>",
                       lambda event: self.f_conectar())
        self.raiz.bind("<Control-q>",
                       lambda event: self.f_salir())

        self.raiz.mainloop()

    # DECLARAR OTROS MÉTODOS DE LA APLICACIÓN:

    def f_conectar(self):
        ''' Definir ventana de diálogo para conectar con equipos '''
        print("Conectando")

    def f_web(self):
        ''' Abrir página web en navegador Internet '''

        pag1 = 'https://github.com/MDI2017/hide_and_seek'
        webbrowser.open_new_tab(pag1)

    def f_salir(self):
        ''' Salir de la aplicación '''
        self.raiz.destroy()


# FUNCIONES DE LA APLICACIÓN

def f_verificar_iconos(iconos):
    ''' Verifica existencia de iconos

    iconos -- Lista de iconos '''

    for icono in iconos:
        if not os.path.exists(icono):
            print('Icono no encontrado:', icono)
            return (1)
    return (0)


def main():
    ''' Iniciar aplicación '''

    # INICIALIZAR VARIABLES CON RUTAS

    app_carpeta = os.getcwd()
    img_carpeta = app_carpeta + os.sep + "images" + os.sep

    print(img_carpeta)

    # DECLARAR Y VERIFICAR ICONOS DE LA APLICACIÓN:

    iconos = (img_carpeta + "ficha-roja (3rd copy).png",
              img_carpeta + "ficha-roja (4th copy).png",
              img_carpeta + "ficha-roja (5th copy).png",
              img_carpeta + "ficha-roja (another copy).png",
              img_carpeta + "ficha-roja (copy).png",
              img_carpeta + "ficha-roja.png")
    error1 = f_verificar_iconos(iconos)

    if not error1:
        mi_app = DropMenu(img_carpeta, iconos)
    return (0)


if __name__ == '__main__':
    main()