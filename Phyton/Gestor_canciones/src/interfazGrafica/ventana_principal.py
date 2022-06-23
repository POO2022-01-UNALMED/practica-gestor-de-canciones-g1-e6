import tkinter as tk
class Ventana_principal:
    def __init__(self):
       self.ventana = tk.Tk()
       self.ventana.geometry("680x420")
       self.ventana.title("Spotifoi")
       frame1= tk.Frame(self.ventana, bg="red", height=40)
       frame1.pack(fill='x')

       frame11 = tk.Frame(frame1, bg='blue')
       frame11.place(relx=0.06, rely=0.5, relwidth=0.1, relheight=5, anchor="c")

       frame12= tk.Frame(frame1, bg='violet')
       frame12.place(relx=0.21, rely=0.5, relwidth=0.2, relheight=5, anchor="c")

       archivo= tk.Button(frame11, text="Archivo")
       archivo.place(relx=0.06, rely=0.5, relwidth=1, relheight=1, anchor="w")

       archivo= tk.Button(frame12, text="Procesos y Consultas")
       archivo.place(relx=0, rely=0.5, relwidth=1, relheight=1, anchor="w")


       self.ventana.mainloop()

