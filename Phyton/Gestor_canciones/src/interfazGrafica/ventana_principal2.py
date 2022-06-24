import tkinter as tk
from tkinter import *
from baseDatos.Serializador import serializarTodo
from baseDatos.Deserializador import Deserializador
from interfazGrafica.fieldFrame import FieldFrame
from gestorAplicacion.personas.Usuario import *
from gestorAplicacion.personas.Artista import *
from gestorAplicacion.elementosLibreria.Cancion import *

class Ventana_principal2(Tk):
    frames=[]
    def __init__(self, usuario):
       super().__init__()
       self.usuario=usuario
       self.geometry("680x420")
       self.title(f"Biblioteca de {self.usuario.nombre}")
       self.option_add('*tearOff', False)
       self.resizable(False, False)

       #Funcionalidades para la vista de Frames

       # Cambiar vista del frame
       def Vista(frameUtilizado):
            for frame in Ventana_principal2.frames:
                frame.pack_forget()
            frameUtilizado.pack(fill=BOTH,expand=True, pady = (10,10))

        # Mostrar un output
       def mostrarOutput(string, text):
            text.delete("1.0", "end")
            text.insert(INSERT, string)
            text.pack(fill=X, expand=True, padx=(10,10))

        # Funcion para regresar al menú principal
       def salir():
          from interfazGrafica.ventana_principal import Ventana_principal
          self.destroy()
          Ventana_principal()

        # barra de menu

       menuBar= tk.Menu(self)

       archivo= tk.Menu(menuBar)
       procesos= tk.Menu(menuBar)

       

       procesos.add_command(label="*inserte funciones xd", command= lambda:print(""))

       archivo.add_command(label="Regresar a la pantalla principal", command= lambda: salir())

       menuBar.add_cascade(label="Archivo",menu=archivo)
       menuBar.add_cascade(label="Procesos y consultas", menu=procesos)
       self.config(menu=menuBar)

       self.mainloop()