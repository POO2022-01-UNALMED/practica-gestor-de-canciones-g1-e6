from curses import window
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("450x300")

labelInicio = tk.Label(ventana, text="inicio")
labelInicio.pack(side="top")



frameLeft = tk.Frame(ventana, width=100, height=100, highlightthickness=1, highlightbackground="black")
frameLeft.pack(side="left", fill="y", expand=True)

saludoBienvenida = tk.Label(frameLeft, text="acá va la descripción   p3")
saludoBienvenida.pack(side="top", fill="x")

botonAcceso = tk.Button(frameLeft, text= "acá se accede al sistema  p4")
botonAcceso.pack(side="bottom", fill="x")





frameRight = tk.Frame(ventana, width=100, height=100, highlightthickness=1, highlightbackground="black")
frameRight.pack(side="right",fill="y", expand=True)

hojaDeVida = tk.Button(frameRight, text="acá va la hoja de vida p5")
hojaDeVida.pack(side="top", fill="x")

frameImagenes = tk.Frame(frameRight, highlightthickness=0.5, highlightbackground="black")
frameImagenes.pack(side="bottom", fill="y")

imagene1 = tk.Label(frameImagenes, text="imagen")
imagene2 = tk.Label(frameImagenes, text="imagen")
imagene3 = tk.Label(frameImagenes, text="imagen")
imagene4 = tk.Label(frameImagenes, text="imagen")

imagene1.grid(row=0, column=0)
imagene1.grid(row=0, column=1)
imagene1.grid(row=0, column=2)
imagene1.grid(row=0, column=3)





ventana.mainloop()