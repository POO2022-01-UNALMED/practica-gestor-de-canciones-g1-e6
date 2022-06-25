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

       

       procesos.add_command(label="Ver mis artistas", command= lambda:Vista(frameVerArtistas))
       procesos.add_command(label="Eliminar cancion de playlist", command= lambda:Vista(frameElimCancionPlay))
       procesos.add_command(label="Eliminar un artista de Mis artistas", command= lambda:Vista(frameElimArtista))
       procesos.add_command(label="Ver canciones con duracion de mis playlist", command= lambda:Vista(frameCanDur))

       archivo.add_command(label="Regresar a la pantalla principal", command= lambda: salir())

       menuBar.add_cascade(label="Archivo",menu=archivo)
       menuBar.add_cascade(label="Procesos y consultas", menu=procesos)
       self.config(menu=menuBar)

       #Frame inicial

       frameInicial= Frame(self)
       nombreInicial = Label(frameInicial, text="Como usar la biblioteca?", font=("Verdana", 16), fg = "#31a919")
       descInicial = Label(frameInicial,text="Aqui en la biblioteca puedes acceder a la mayoría de funciones de spotifoi \n desde Procesos y consultas puedes; \n -gestionar mis artistas: ver, agregar y eliminar \n -gestionar playlits: info general, info de las canciones, crear y eliminar \n funciones especiales: \n descubrir artista favorito \n ver duracion total de playlists \n ver si cancion se repite en varias playlist \n para regresar a pantalla principal: \n Archivo -> Regresar a la pantalla principal",font=("Verdana", 12))
       
       Ventana_principal2.frames.append(frameInicial)

       nombreInicial.pack()
       descInicial.pack()

       Ventana_principal2.frames.append(frameInicial)

       Vista(frameInicial)

       #Funcion para ver mis artistas

       def verArtisas():
          string=""
          lista= self.usuario._mis_artistas.getArtistas()
          for i in range(len(lista)):
               string +=f"{lista[i].nombre}\n\n"
          if string == "":
                string += "No hay artistas agregados"
          mostrarOutput(string, outputVerArtistas)

       #Frame usado para ver mis artistas   
      
       frameVerArtistas= Frame(self)
       nombreVerArtistas= Label(frameVerArtistas, text="Mis artistas", font=("Verdana", 16), fg = "#31a919")
       descVerArtistas = Label(frameVerArtistas,text="Mueva la rueda del mouse para ver mas artistas",font=("Verdana", 12))
       refrescarVerArtistas = Button(frameVerArtistas, text="Mostrar", font=("Verdana", 12), fg="white",bg="#31a919", command=verArtisas)
       

       outputVerArtistas= Text(frameVerArtistas, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(frameVerArtistas)

       nombreVerArtistas.pack()
       descVerArtistas.pack()
       refrescarVerArtistas.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameVerArtistas)

       #Funcion para eliminar cancion de playlist
       def ElimCancionPlay():
          cancion=FieldElimCancionPlay.getValue("Cancion")
          playlist=FieldElimCancionPlay.getValue("Playlist")
          play=None
          for i in usuario.getPlaylists():
              if i.nombre==playlist:
                play=i
                break
          if play==None:
              mostrarOutput("la playlist no esta agregada o no existe", outputElimCancionPlay)
              return
          for i in play.getCanciones():
            if i.nombre==cancion:
                mostrarOutput(play.elim_cancion(i), outputElimCancionPlay)
                return
          mostrarOutput("la cancion no esta agregada o no existe", outputElimCancionPlay)

          


       #FieldFrame para eliminar cancion de playlist

       frameElimCancionPlay= Frame(self)
       nombreElimCancionPlay = Label(frameElimCancionPlay, text="Eliminar cancion de una playlist", font=("Verdana", 16), fg = "#31a919")
       descElimCancionPlay = Label(frameElimCancionPlay,text="Por favor ingrese el nombre de la cancion y la playlist",font=("Verdana", 12))
       FieldElimCancionPlay = FieldFrame(frameElimCancionPlay, None, ["Cancion", "Playlist"], None, None, None)
       FieldElimCancionPlay.crearBotones(ElimCancionPlay)

       outputElimCancionPlay= Text(frameElimCancionPlay, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputElimCancionPlay)

       nombreElimCancionPlay.pack()
       descElimCancionPlay.pack()
       FieldElimCancionPlay.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameElimCancionPlay)

       #Funcion para eliminar artista de mis artistas
       def ElimArtista():
          artista=FieldElimArtista.getValue("Artista")
          art=None
          for i in usuario.getMis_artistas().getArtistas():
              if i.nombre==artista:
                art=i
                break
          if art==None:
              mostrarOutput("el artista no esta agregado o no existe", outputElimArtista)
              return
          mostrarOutput(self.usuario.getMis_artistas().elim_artista(art), outputElimArtista)

       #FieldFrame para eliminar artista de mis artistas

       frameElimArtista= Frame(self)
       nombreElimArtista = Label(frameElimArtista, text="Eliminar un artista de mis artistas", font=("Verdana", 16), fg = "#31a919")
       descElimArtista = Label(frameElimArtista,text="Por favor ingrese el nombre del artista",font=("Verdana", 12))
       FieldElimArtista = FieldFrame(frameElimArtista, None, ["Artista"], None, None, None)
       FieldElimArtista.crearBotones(ElimArtista)

       outputElimArtista= Text(frameElimArtista, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputElimArtista)

       nombreElimArtista.pack()
       descElimArtista.pack()
       FieldElimArtista.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameElimArtista)

       #Funcion para ver canciones con duracion

       def verCanDur():
        string=""
        for i in usuario.getPlaylists():
            string+=f"Nombre de la playlist: {i.nombre}\n\n"
            for j in i.getCanciones():
                hora=j.getDuracion()//3600
                min=(j.getDuracion()-(3600*hora))//60
                seg=j.getDuracion()-((hora*3600)+(min*60))
                string+=f"{j.nombre} --> dura {hora} horas con {min} minutos con {seg}\n\n"
        mostrarOutput(string, outputCanDur)

          

       #Frame usado para ver canciones con duracion   
      
       frameCanDur= Frame(self)
       nombreCanDur= Label(frameCanDur, text="Canciones de las playlist con duracion", font=("Verdana", 16), fg = "#31a919")
       descCanDur = Label(frameCanDur,text="Mueva la rueda del mouse para ver mas canciones y playlists",font=("Verdana", 12))
       refrescarCanDur = Button(frameCanDur, text="Mostrar", font=("Verdana", 12), fg="white",bg="#31a919", command=verCanDur)
       

       outputCanDur= Text(frameCanDur, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(frameCanDur)

       nombreCanDur.pack()
       descCanDur.pack()
       refrescarCanDur.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameCanDur)

       self.mainloop()