import tkinter as tk
from tkinter import Label
from baseDatos.Serializador import serializarTodo
from baseDatos.Deserializador import Deserializador

class Ventana_principal:
    def __init__(self):
       self.ventana = tk.Tk()
       self.ventana.geometry("680x420")
       self.ventana.title("Spotifoi")
       self.ventana.option_add('*tearOff', False)
       def aplicacion():
            ventana1 = tk.Tk()
            ventana1.geometry("680x420")
            ventana1.title("Spotifoi")
            textoInfo = f"Spotifoi es un gestor de canciones.\n" \
                        f"donde se pueden tener varios usuarios\n" \
                        f"cada uno con su propia biblioteca con playlists\n"\
                        f"tambien con una lista de artistas favoritos de la app." 
            info = Label(ventana1, text = textoInfo, justify = "left", font=("Verdana", 12))
            info.pack(fill=tk.Y, expand=True)

       def acercaDe():
            ventana2 = tk.Tk()
            ventana2.geometry("680x420")
            ventana2.title("Spotifoi")
            textoInfo = f"Autores:\n" \
                        f"David Esteban Toro Arango\n" \
                        f"Manuel Alejandro Gallego Jiménez\n"\
                        f"Carlos David Arango Escobar" 
            info = Label(ventana2, text = textoInfo, justify = "left", font=("Verdana", 12))
            info.pack(fill=tk.Y, expand=True)
       def salir():
        from interfazGrafica.inicio import Inicio
        serializarTodo()
        self.ventana.destroy()
        Inicio()

           

       
       menuBar= tk.Menu(self.ventana)

       archivo= tk.Menu(menuBar)
       procesos= tk.Menu(menuBar)
       ayuda= tk.Menu(menuBar)

       ayuda.add_command(label="Acerca de", command= lambda: acercaDe())

       procesos.add_command(label="*inserte funcionalidades xd*", command= lambda:print(""))

       archivo.add_command(label="Aplicacion", command= lambda: aplicacion())
       archivo.add_command(label="Salir", command= lambda: salir())

       menuBar.add_cascade(label="Archivo",menu=archivo)
       menuBar.add_cascade(label="Procesos y consultas", menu=procesos)
       menuBar.add_cascade(label="Ayuda", menu=ayuda)
       self.ventana.config(menu=menuBar)
      
    
       self.ventana.mainloop()
