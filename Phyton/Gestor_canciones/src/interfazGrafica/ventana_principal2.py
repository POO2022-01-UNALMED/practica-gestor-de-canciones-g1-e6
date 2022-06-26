import tkinter as tk
from tkinter import *
from baseDatos.Serializador import serializarTodo
from baseDatos.Deserializador import Deserializador
from gestorAplicacion.elementosLibreria.Playlist import Playlist
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
       procesos.add_command(label="Agregar una cancion a una playlist", command= lambda:Vista(frameAggCancionPlay))
       procesos.add_command(label="Eliminar cancion de playlist", command= lambda:Vista(frameElimCancionPlay))
       procesos.add_command(label="Agregar un artista a Mis artistas", command= lambda:Vista(frameAggArtista))
       procesos.add_command(label="Eliminar un artista de Mis artistas", command= lambda:Vista(frameElimArtista))
       procesos.add_command(label="Ver info general de playlsits", command= lambda:Vista(framePlaDesc))
       procesos.add_command(label="Ver canciones con duracion de mis playlist", command= lambda:Vista(frameCanDur))
       procesos.add_command(label="Verificar quien creo una playlsit", command= lambda:Vista(frameVeriCrea))
       procesos.add_command(label="Reproducir una cancion aleatoria de una playlist", command= lambda:Vista(frameAleatoria))
       procesos.add_command(label="Reproducir una cancion de una playlist", command= lambda:Vista(frameNoAleatoria))
       procesos.add_command(label="Ver duracion total de las playlist", command= lambda:Vista(frameDuracion))
       procesos.add_command(label="Crear una playlist", command= lambda:Vista(frameCrearPlay))
       procesos.add_command(label="Agregar una playlist", command= lambda:Vista(frameAggPlay))

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

       #Funcion para agregar una cancion a una playlist
       def AggCancionPlay():
          cancion=FieldAggCancionPlay.getValue("Cancion")
          playlist=FieldAggCancionPlay.getValue("Playlist")
          play=None
          for i in usuario.getPlaylists():
              if i.nombre==playlist:
                play=i
                break
          if play==None:
              mostrarOutput("la playlist no esta agregada o no existe", outputAggCancionPlay)
              return
          for i in Cancion.cancionesCreadas:
            if i.nombre==cancion:
                mostrarOutput(play.agg_cancion(i), outputAggCancionPlay)
                return
          mostrarOutput("la cancion no esta agregada o no existe", outputAggCancionPlay)      

       #FieldFrame para agregar cancion a playlist

       frameAggCancionPlay= Frame(self)
       nombreAggCancionPlay = Label(frameAggCancionPlay, text="Agregar una cancion a una playlist", font=("Verdana", 16), fg = "#31a919")
       descAggCancionPlay = Label(frameAggCancionPlay,text="Por favor ingrese el nombre de la cancion y la playlist",font=("Verdana", 12))
       FieldAggCancionPlay = FieldFrame(frameAggCancionPlay, None, ["Cancion", "Playlist"], None, None, None)
       FieldAggCancionPlay.crearBotones(AggCancionPlay)

       outputAggCancionPlay= Text(frameAggCancionPlay, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputAggCancionPlay)

       nombreAggCancionPlay.pack()
       descAggCancionPlay.pack()
       FieldAggCancionPlay.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameAggCancionPlay)

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
       def AggArtista():
          artista=FieldAggArtista.getValue("Artista")
          art=None
          for i in Artista.artistas:
              if i.nombre==artista:
                art=i
                break
          if art==None:
              mostrarOutput("El artistas ingresado no existe", outputAggArtista)
              return
          for j in usuario.getMis_artistas().getArtistas():
              if j.nombre==artista:
                mostrarOutput("El artistas ingresado ya se encuentra en Mis artistas", outputAggArtista)
                return
          self.usuario.getMis_artistas().agg_artista(art)
          mostrarOutput("El artistas ingresado fue agregado exitosamente", outputAggArtista)

       #FieldFrame para agregar artista a mis artistas

       frameAggArtista= Frame(self)
       nombreAggArtista = Label(frameAggArtista, text="Agregar un artista a mis artistas", font=("Verdana", 16), fg = "#31a919")
       descAggArtista = Label(frameAggArtista,text="Por favor ingrese el nombre del artista",font=("Verdana", 12))
       FieldAggArtista = FieldFrame(frameAggArtista, None, ["Artista"], None, None, None)
       FieldAggArtista.crearBotones(AggArtista)

       outputAggArtista= Text(frameAggArtista, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputAggArtista)

       nombreAggArtista.pack()
       descAggArtista.pack()
       FieldAggArtista.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameAggArtista)

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

       #Funcion para ver info de playlists

       def verPlaDesc():
        string=""
        for i in usuario.getPlaylists():
            if i.nombre == "Me gusta":
                string+=f"La playlist Me gusta es creada por Spotifoy al crear el usuario\n\n"
            elif i.nombre == "Favoritos":
                string+=f"La playlist Favoritos es creada por Spotifoy al crear el usuario\n\n"
            else:
                 string+=f"La playlist de nombre {i.getNombre()}\n fue creada por: {i.getCreador().nombre}\n\n"
            
            string+=f"----------------------------------------\n\n"
        mostrarOutput(string, outputPlaDesc)

       #Frame usado para ver info de playlists 
      
       framePlaDesc= Frame(self)
       nombrePlaDesc= Label(framePlaDesc, text="Descripcion de las playlists", font=("Verdana", 16), fg = "#31a919")
       descPlaDesc = Label(framePlaDesc,text="Mueva la rueda del mouse para ver la descripcion de  las playlists",font=("Verdana", 12))
       refrescarPlaDesc = Button(framePlaDesc, text="Mostrar", font=("Verdana", 12), fg="white",bg="#31a919", command=verPlaDesc)
       

       outputPlaDesc= Text(framePlaDesc, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(framePlaDesc)

       nombrePlaDesc.pack()
       descPlaDesc.pack()
       refrescarPlaDesc.pack(pady=(10,10))

       Ventana_principal2.frames.append(framePlaDesc)

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
            string+=f"----------------------------------------\n\n"
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







       #Funcion para verificar creador de playlist

       def VeriCrea():
        playlist=FieldVeriCrea.getValue("Nombre")
        for i in Playlist.playlists:
            if i.nombre==playlist:
                if i.nombre == "Me gusta" or i.nombre == "Favoritos":
                    string = f"Esta playlist fue creada por defecto\nSpotifoy todos los derechos reservados"
                else:
                    string = f"Esta playlist fue creada por {i.getCreador().nombre}\nSpotifoy todos los derechos reservados"
                mostrarOutput(string, outputVeriCrea)
                return
            else:
                mostrarOutput("La playlist ingresada no esta agregada o no existe", outputVeriCrea)  

       #FieldFrame usado para verificar creador de playlist
      
       frameVeriCrea= Frame(self)
       nombreVeriCrea= Label(frameVeriCrea, text="Verificar creador de playlist", font=("Verdana", 16), fg = "#31a919")
       descVeriCrea = Label(frameVeriCrea,text="Ingrese el nombre de la playlist que desea verificar su creador",font=("Verdana", 12))
       FieldVeriCrea= FieldFrame(frameVeriCrea, None, ["Nombre"], None, None, None)
       FieldVeriCrea.crearBotones(VeriCrea)

       outputVeriCrea= Text(frameVeriCrea, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputVeriCrea)

       nombreVeriCrea.pack()
       descVeriCrea.pack()
       FieldVeriCrea.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameVeriCrea)

       #Funcion para reproducir cancion aleatoria

       def Aleatoria():
        playlist=FieldAleatoria.getValue("Playlist")
        play=None
        for i in Playlist.playlists:
            if i.nombre==playlist:
                play=i
                break
        if play==None:
              mostrarOutput("la playlist no existe", outputAleatoria)
              return
        mostrarOutput(self.usuario.getBiblioteca().repo_aleatoria(play), outputAleatoria)

       #FieldFrame usado para reproducir cancion aleatoria   
      
       frameAleatoria= Frame(self)
       nombreAleatoria= Label(frameAleatoria, text="Reproduccion aleatoria de cancion de una playlist", font=("Verdana", 16), fg = "#31a919")
       descAleatoria = Label(frameAleatoria,text="Ingrese el nombre de la playlist que desea reproducir",font=("Verdana", 12))
       FieldAleatoria= FieldFrame(frameAleatoria, None, ["Playlist"], None, None, None)
       FieldAleatoria.crearBotones(Aleatoria)

       outputAleatoria= Text(frameAleatoria, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputAleatoria)

       nombreAleatoria.pack()
       descAleatoria.pack()
       FieldAleatoria.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameAleatoria)









       #Funcion para reproducir cancion aleatoria

       def NoAleatoria():
        playlist=FieldNoAleatoria.getValue("Playlist")
        nombrec=FieldNoAleatoria.getValue("Nombre")
        play=None
        for i in Playlist.playlists:
            if i.nombre==playlist:
                play=i
                break
        if play==None:
              mostrarOutput("la playlist no existe", outputNoAleatoria)
              return
        play2=None
        for i in Cancion.cancionesCreadas:
            if i.nombre==nombrec:
                play2=i
                break
        if play2==None:
              mostrarOutput("La cancion no existe", outputNoAleatoria)
              return
        mostrarOutput(play2.play(), outputNoAleatoria)

       #FieldFrame usado para reproducir cancion aleatoria   
      
       frameNoAleatoria= Frame(self)
       nombreNoAleatoria= Label(frameNoAleatoria, text="Reproduccion de cancion de una playlist", font=("Verdana", 16), fg = "#31a919")
       descNoAleatoria = Label(frameNoAleatoria,text="Ingrese el nombre de la playlist que desea reproducir",font=("Verdana", 12))
       nombreNoAleatoria = Label(frameNoAleatoria,text="y de la cancion que desea reproducir",font=("Verdana", 12))


       
       FieldNoAleatoria= FieldFrame(frameNoAleatoria, None, ["Playlist", "Nombre"], None, None, None)
       FieldNoAleatoria.crearBotones(NoAleatoria)

       outputNoAleatoria= Text(frameNoAleatoria, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputNoAleatoria)

       nombreNoAleatoria.pack()
       descNoAleatoria.pack()
       FieldNoAleatoria.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameNoAleatoria)








       #Funcion para ver duracion total

       def Duracion():
        duracion=self.usuario.duracion_total()
        hora=duracion//3600
        min=(duracion-(3600*hora))//60
        seg=duracion-((hora*3600)+(min*60))
        string=f"La duracion de todas las playlist es de {hora} horas con {min} minutos con {seg}\n\n"
        mostrarOutput(string, outputDuracion)

          

       #Frame usado para ver duracion total  
      
       frameDuracion= Frame(self)
       nombreDuracion= Label(frameDuracion, text="Duracion total de las playlist", font=("Verdana", 16), fg = "#31a919")
       descDuracion = Label(frameDuracion,text="Aqui puede observar cuanto duran las canciones de sus playlist en total",font=("Verdana", 12))
       refrescarDuracion = Button(frameDuracion, text="Mostrar", font=("Verdana", 12), fg="white",bg="#31a919", command=Duracion)
       

       outputDuracion= Text(frameDuracion, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(frameDuracion)

       nombreDuracion.pack()
       descDuracion.pack()
       refrescarDuracion.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameDuracion)

       #Funcion para crear playlist

       def CrearPlay():
        playlist=FieldCrearPlay.getValue("Nombre")
        for i in Playlist.playlists:
            if i.nombre==playlist:
                mostrarOutput("la playlist ya existe", outputCrearPlay)
                return
        play=Playlist(self.usuario, playlist)    
        mostrarOutput(f"playlist {playlist} creada exitosamente", outputCrearPlay)

          

       #FieldFrame usado para crear playlist
      
       frameCrearPlay= Frame(self)
       nombreCrearPlay= Label(frameCrearPlay, text="Crear una playlist", font=("Verdana", 16), fg = "#31a919")
       descCrearPlay = Label(frameCrearPlay,text="Ingrese el nombre de la playlist, \n recuerde que debe ser diferente a otra creada, incluso por otro usuario",font=("Verdana", 12))
       FieldCrearPlay= FieldFrame(frameCrearPlay, None, ["Nombre"], None, None, None)
       FieldCrearPlay.crearBotones(CrearPlay)

       outputCrearPlay= Text(frameCrearPlay, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputCrearPlay)

       nombreCrearPlay.pack()
       descCrearPlay.pack()
       FieldCrearPlay.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameCrearPlay)

       #Funcion para agregar playlist

       def AggPlay():
        playlist=FieldAggPlay.getValue("Nombre")
        for i in Playlist.playlists:
            if i.nombre==playlist:
                for j in self.usuario.getPlaylists():
                    if i==j:
                        mostrarOutput(f"La playlist ya fue agregada anteriormente", outputAggPlay)
                        return
                self.usuario.agg_Playlist(i)
                mostrarOutput(f"Playlist {i.nombre} agregada exitosamente", outputAggPlay)
                return
        mostrarOutput("La playlist no existe", outputAggPlay)

          

       #FieldFrame usado para agregar playlist
      
       frameAggPlay= Frame(self)
       nombreAggPlay= Label(frameAggPlay, text="Agregar una playlist", font=("Verdana", 16), fg = "#31a919")
       descAggPlay = Label(frameAggPlay,text="Ingrese el nombre de la playlist",font=("Verdana", 12))
       FieldAggPlay= FieldFrame(frameAggPlay, None, ["Nombre"], None, None, None)
       FieldAggPlay.crearBotones(AggPlay)

       outputAggPlay= Text(frameAggPlay, height=100, font=("Verdana", 10))
       Ventana_principal2.frames.append(outputAggPlay)

       nombreAggPlay.pack()
       descAggPlay.pack()
       FieldAggPlay.pack(pady=(10,10))

       Ventana_principal2.frames.append(frameAggPlay)

       self.mainloop()