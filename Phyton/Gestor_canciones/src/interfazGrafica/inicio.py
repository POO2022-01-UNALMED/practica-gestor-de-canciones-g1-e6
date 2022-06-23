from cgitb import text
#from curses import window
from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT, scrolledtext
import tkinter as tk
from ventana_principal import Ventana_principal

class Inicio(Frame):

    def __init__(self):

        self.hojaActual = 0
        self.hojasDeVida = ["Carlos", "Manuel", "David"]

        self.ventana = tk.Tk()
        self.ventana.title("Inicio")
        self.ventana.geometry("680x420")



        self.frameLeft = tk.Frame(self.ventana, width=100, height=100, highlightthickness=1, highlightbackground="black")
        self.frameLeft.pack(side="left", fill="y", expand=True)

        self.saludoBienvenida = tk.Label(self.frameLeft, text="acá va la descripción   p3")
        self.saludoBienvenida.pack(side="top", fill="x")

        self.botonAcceso = tk.Button(self.frameLeft, text= "acceder a la pantalla principal:", command=self.abrir_ventana_principal)
        self.botonAcceso.pack(side="bottom", fill="x")
        
        





        self.frameRight = tk.Frame(self.ventana, width=100, height=100, highlightthickness=1, highlightbackground="black")
        self.frameRight.pack(side="right",fill="y", expand=True)

        self.hojaDeVida = tk.Button(self.frameRight, text= self.hojasDeVida[self.hojaActual], command=self.cambiarHoja)
        self.hojaDeVida.pack(side="top", fill="x")

        self.frameImagenes = tk.Frame(self.frameRight, highlightthickness=0.5, highlightbackground="black")
        self.frameImagenes.pack(side="bottom", fill="y")

        self.imagene1 = tk.Label(self.frameImagenes, text="imagen")
        self.imagene2 = tk.Label(self.frameImagenes, text="imagen")
        self.imagene3 = tk.Label(self.frameImagenes, text="imagen")
        self.imagene4 = tk.Label(self.frameImagenes, text="imagen")

        self.imagene1.grid(row=0, column=0)
        self.imagene1.grid(row=0, column=1)
        self.imagene1.grid(row=0, column=2)
        self.imagene1.grid(row=0, column=3)

        self.ventana.mainloop()

    def abrir_ventana_principal(self):
            self.ventana.destroy()
            Ventana_principal()
    def cambiarHoja(self):
        if self.hojaActual == 2:
            self.hojaActual = 0
        else:
            self.hojaActual = self.hojaActual +1

        self.hojaDeVida["text"] = self.hojasDeVida[self.hojaActual]


