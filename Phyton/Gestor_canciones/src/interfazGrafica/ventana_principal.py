import tkinter as tk
class Ventana_principal:
    def __init__(self):
       self.ventana = tk.Tk()
       self.ventana.geometry("450x300")
       self.ventana.title("Spotifoi")

       self.labelInicio = tk.Label(self.ventana, text="spotifoi")
       self.labelInicio.pack(side="top")

       self.ventana.mainloop()
