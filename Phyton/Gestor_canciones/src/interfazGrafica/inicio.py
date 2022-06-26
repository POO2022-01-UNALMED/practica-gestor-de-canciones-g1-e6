from cgitb import text
#from curses import window
from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT, scrolledtext
import tkinter as tk
from interfazGrafica.ventana_principal import Ventana_principal
import pathlib
import os



class Inicio(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('i-Lunch - Inicio')
        self.option_add("*tearOff",  False)
        self.geometry("1400x720")
        self.resizable(False,False)
        #creación de mennú

        self._barraMenu = tk.Menu(self)
        inicio =tk. Menu(self._barraMenu)
        inicio.add_command(label = "Descripcion", command = lambda: self.desplegarDescripcion())
        inicio.add_command(label = "Salir", command = lambda: self.destroy())
        self._barraMenu.add_cascade(label = "Inicio", menu = inicio)
        self.config(menu = self._barraMenu)

        # Marco derecha

        self.frameRight = FrameRight(self)

        # Marco izquierda

        self.frameLeft = FrameLeft(self) 

        self.frameLeft.grid(row = 0, column = 0, padx=(10,10))
        self.frameRight.grid(row = 0, column = 1, padx=(10,10))

        #mostrar descripción
        
    def desplegarDescripcion(self):
        self.frameLeft._descripcion.pack(pady=(10,0))
        self.geometry("1420x840")

class FrameLeft(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        # Guardar la referncia a la ventana 

        self.ventana = ventana

        # Definir los Frames 

        self._p3 = Frame(self)
        self._p4_1 = Frame(self)
        self._p4_2 = Frame(self)
        
        #saludo de bienvenida

        textoSaludo = "Bienvenido de nuevo a i-Lunch."
        self._saludo = Label(self._p3, text = textoSaludo, font = ("Verdana", 16), fg = "#245efd")
        self._saludo.pack()

        #descripción del sistema

        textoDescripcion = f"canciones yupi" 
        self._descripcion = Label(self._p3, text = textoDescripcion, width = 100, justify = "left", font=("Verdana", 8))

        # cargar las imagenes

        self._imagenActual = 0 # Imagen actual
        self._imagenes = []

        for i in range(5):
            archivo = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), f"src\\recursos\imagenApp{i+1}.png")
            imagen = PhotoImage(file = archivo)
            self._imagenes.append(imagen)

        # Imprimir la primera imagen relacionada a la aplicacion en P4

        self._imagen = Label(self._p4_1, image = self._imagenes[0], height = 480, width = 640)
        self._imagen.bind('<Enter>', self.cambiarImagen) # Cambiar de imagen de P4 al pasar el mouse por encima
        self._imagen.pack()

        # Boton de acceso a la aplicacion abajo en P4

        self._boton = Button(self._p4_2, text = "Acceder a la aplicacion", font = ("Verdana", 16), fg = "white", bg = "#245efd", command = self.abrir_ventana_principal)
        self._boton.pack()

        # Colocar todos los elementos en pantalla

        self._p3.grid(row = 0, column = 0, pady=(10,10))
        self._p4_1.grid(row = 1, column = 0, pady=(10,10))
        self._p4_2.grid(row = 2, column = 0, pady=(10,10))
    
    # Cambiar de imagen de P4 al pasar el mouse por encima

    def cambiarImagen(self, args):
        if self._imagenActual == 4:
            self._imagenActual = 0
        else:
            self._imagenActual += 1

        self._imagen.configure(image = self._imagenes[self._imagenActual])
        self._imagen.image = self._imagenes[self._imagenActual]


    #metodo para abrir venana principal

    def abrir_ventana_principal(self):
        self.ventana.destroy()
        Ventana_principal()


class FrameRight(Frame):
    _posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, window):
        super().__init__(window)
        
        self._p5 = Frame(self)
        self._p6 = Frame(self)

        self._text = None
        self._next_hv = 0
        self._photos = [None, None, None, None]


        self.cargarHVTexto(0)
    
        self._p5.grid()
        self._p6.grid()

    # Se usa para mostrar la hoja de vida que sigue, aumentando el atributo next_hv
    def proximo(self, _):
        if self._next_hv < 3:
            self._next_hv = self._next_hv + 1
        else:
            self._next_hv = 0

        self._photos = [None, None, None, None]
        self.cargarHVTexto(self._next_hv)


    # Carga el texto para la hoja de vida respecto al numero asignado

    def cargarHVTexto(self, numero):
        self._text = Text(self._p5, height = 10, font = ("Verdana",10), width = 80)
        self._text.grid(row = 1, column = 0)
        self._text.bind('<Button-1>', self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\recursos\HV{0}4.txt'.format(numero))

        with open(path, "r+") as hv_text:
            self._text.insert(INSERT, hv_text.read())