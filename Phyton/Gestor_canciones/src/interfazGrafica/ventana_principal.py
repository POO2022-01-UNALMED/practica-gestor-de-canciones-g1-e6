import tkinter as tk
from tkinter import *
from baseDatos.Serializador import serializarTodo
from baseDatos.Deserializador import Deserializador
from interfazGrafica.fieldFrame import FieldFrame
from gestorAplicacion.personas.Usuario import *
from gestorAplicacion.personas.Artista import *
from gestorAplicacion.elementosLibreria.Cancion import *

class Ventana_principal(Tk):
    frames=[]
    def __init__(self):
       super().__init__()
       self.geometry("680x420")
       self.title("Spotifoi")
       self.option_add('*tearOff', False)
       self.resizable(False, False)

       #Funcionalidades para la vista de Frames

     # Cambiar vista del frame
       def Vista(frameUtilizado):
            for frame in Ventana_principal.frames:
                frame.pack_forget()
            frameUtilizado.pack(fill=BOTH,expand=True, pady = (10,10))

        # Mostrar un output
       def mostrarOutput(string, text):
            text.delete("1.0", "end")
            text.insert(INSERT, string)
            text.pack(fill=X, expand=True, padx=(10,10))
       
      
       #Funciones basicas de archivo y ayuda
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
        self.destroy()
        Inicio()
       

        #Funcionalidades de los procesos
           

       #barra de menu
       menuBar= tk.Menu(self)

       archivo= tk.Menu(menuBar)
       procesos= tk.Menu(menuBar)
       ayuda= tk.Menu(menuBar)

       ayuda.add_command(label="Acerca de", command= lambda: acercaDe())

       procesos.add_command(label="Crear usuario", command= lambda:Vista(frameCrearUsuario))
       procesos.add_command(label="Recomendar cancion a un usuario", command= lambda:Vista(frameRecomendacion))
       procesos.add_command(label="Desplegar biblioteca de un usuario", command= lambda:Vista(frameBiblioteca))
       procesos.add_command(label="Ver Canciones creadas", command= lambda:Vista(frameVerCanciones))
       procesos.add_command(label="Ver Usuarios creados", command= lambda:Vista(frameVerUsuarios))
      

       archivo.add_command(label="Aplicacion", command= lambda: aplicacion())
       archivo.add_command(label="Salir", command= lambda: salir())

       menuBar.add_cascade(label="Archivo",menu=archivo)
       menuBar.add_cascade(label="Procesos y consultas", menu=procesos)
       menuBar.add_cascade(label="Ayuda", menu=ayuda)
       self.config(menu=menuBar)

       #Frame inicial

       frameInicial= Frame(self)
       nombreInicial = Label(frameInicial, text="Como usar Spotifoi?", font=("Verdana", 16), fg = "#31a919")
       descInicial = Label(frameInicial,text="En spotifoi puedes crear varios usuarios y gestionar sus bibliotecas \n todas las funcionalidades las encuentras en procesos y consultas \n desde este pestaña puedes crear y visualizar usuarios \n tambien visualizar las canciones subidas por artistas \n ademas de recomendar una cancion a un usuario \n para ingresar en la biblioteca de un usuario sigue la ruta: \n Procesos y consultas -> Desplegar la biblioteca de un usuario -> ingresa nombre \n desde allí gestionas playlist, artistas y demas de un usuario \n para obtener información de los creadores: \n ayuda -> acerca de \n para info general de Spotifoi: \n Archivo -> Aplicacion \n para regresar a la pantalla inicial: \n Archivo -> Guardar y salir",font=("Verdana", 12))
       
       Ventana_principal.frames.append(frameInicial)

       nombreInicial.pack()
       descInicial.pack()

       Ventana_principal.frames.append(frameInicial)

       Vista(frameInicial)

       #Funcion para crear un usuario
       def crearUsuario():
          nombre=FieldCrearUsuario.getValue("Nombre")
          creacion=Usuario(nombre)
          resultado=f"el usuario {creacion.nombre} fue creado con exito"
          mostrarOutput(resultado,outputCrearUsuario)

       #FieldFrame para crear usuario

       frameCrearUsuario= Frame(self)
       nombreCrearUsuario = Label(frameCrearUsuario, text="Crear un usuario", font=("Verdana", 16), fg = "#31a919")
       descCrearUsuario = Label(frameCrearUsuario,text="Por favor ingrese el nombre del nuevo usuario",font=("Verdana", 12))
       FieldCrearUsuario = FieldFrame(frameCrearUsuario, None, ["Nombre"], None, None, None)
       FieldCrearUsuario.crearBotones(crearUsuario)

       outputCrearUsuario= Text(frameCrearUsuario, height=100, font=("Verdana", 10))
       Ventana_principal.frames.append(outputCrearUsuario)

       nombreCrearUsuario.pack()
       descCrearUsuario.pack()
       FieldCrearUsuario.pack(pady=(10,10))

       Ventana_principal.frames.append(frameCrearUsuario)

       #Funcion para recomendar cancion
       def crearRecomendacion():
          username=FieldRecomendacion.getValue("Nombre")
          usuario=None
          for i in Usuario.usuarios:
               if i.nombre==username:
                    usuario=i
          if usuario==None:
               resultado="No existe el usuario"
          else:
               result=usuario.recomendar_cancion()
               resultado=f"se recomienda {result.getNombre()}"
          mostrarOutput(resultado,outputRecomendacion)

       #FieldFrame para recomendar cancion
       frameRecomendacion= Frame(self)
       nombreRecomendacion = Label(frameRecomendacion, text="Recomendar cancion a un usuario", font=("Verdana", 16), fg = "#31a919")
       descRecomendacion = Label(frameRecomendacion,text="Por favor ingrese el nombre del usuario a recomendar",font=("Verdana", 12))
       FieldRecomendacion = FieldFrame(frameRecomendacion, None, ["Nombre"], None, None, None)
       FieldRecomendacion.crearBotones(crearRecomendacion)

       outputRecomendacion= Text(frameRecomendacion, height=100, font=("Verdana", 10))
       Ventana_principal.frames.append(outputRecomendacion)

       nombreRecomendacion.pack()
       descRecomendacion.pack()
       FieldRecomendacion.pack(pady=(10,10))

       Ventana_principal.frames.append(frameRecomendacion)

       #Funcion para abrir biblioteca
       def abrirBiblioteca():
          username=FieldBiblioteca.getValue("Nombre")
          usuario=None
          for i in Usuario.usuarios:
               if i.nombre==username:
                    usuario=i
          if usuario==None:
              resultado="No existe el usuario"
              mostrarOutput(resultado,outputBiblioteca)
          else:
               from interfazGrafica.ventana_principal2 import Ventana_principal2
               self.destroy()
               Ventana_principal2(usuario)
               
          

       #FieldFrame para abrir biblioteca
       frameBiblioteca= Frame(self)
       nombreBiblioteca = Label(frameBiblioteca, text="Abrir la biblioteca de un usuario", font=("Verdana", 16), fg = "#31a919")
       descBiblioteca = Label(frameBiblioteca,text="Por favor ingrese el nombre del usuario",font=("Verdana", 12))
       FieldBiblioteca = FieldFrame(frameBiblioteca, None, ["Nombre"], None, None, None)
       FieldBiblioteca.crearBotones(abrirBiblioteca)

       outputBiblioteca= Text(frameBiblioteca, height=100, font=("Verdana", 10))
       Ventana_principal.frames.append(outputBiblioteca)

       nombreBiblioteca.pack()
       descBiblioteca.pack()
       FieldBiblioteca.pack(pady=(10,10))

       Ventana_principal.frames.append(frameBiblioteca)

        #Funcion para ver usuarios
       def refrescarUsuarios():
          string=""
          listaUsuarios= Usuario.usuarios
          listaArtistas= Artista.artistas
          for i in range(len(listaUsuarios)):
               string += f"ID: {i}\n"\
                     f"{listaUsuarios[i].datosPersona()}\n\n"
          for i in range(len(listaArtistas)):
               string += f"ID: {i}\n"\
                     f"{listaArtistas[i].datosPersona()}\n\n"
          if string == "":
                string += "No hay usuarios creados"
          mostrarOutput(string, outputVerUsuarios)

       #Frame usado para ver usuarios   
      
       frameVerUsuarios= Frame(self)
       nombreVerUsuarios = Label(frameVerUsuarios, text="Usuarios creados en la app", font=("Verdana", 16), fg = "#31a919")
       descVerUsuarios = Label(frameVerUsuarios,text="Recuerde que puede que inicialmente no se observe la totalidad de los usuarios \n Puebe a mover rueda del mouse para ver más usuarios",font=("Verdana", 12))
       refrescarVerUsuarios = Button(frameVerUsuarios, text="Mostrar/Refescar", font=("Verdana", 12), fg="white",bg="#31a919", command=refrescarUsuarios)
       

       outputVerUsuarios= Text(frameVerUsuarios, height=100, font=("Verdana", 10))
       Ventana_principal.frames.append(frameVerUsuarios)

       nombreVerUsuarios.pack()
       descVerUsuarios.pack()
       refrescarVerUsuarios.pack(pady=(10,10))

       Ventana_principal.frames.append(frameVerUsuarios)

       #Funcion para ver las canciones creadas
       def refrescarCanciones():
          string=""
          listaCanciones= Cancion.cancionesCreadas
          for i in range(len(listaCanciones)):
               string += f"ID: {i}\n"\
                     f"{listaCanciones[i].getNombre()} del artista {listaCanciones[i].getArtista().nombre}\n\n"
          if string == "":
                string += "No hay canciones creadas"
          mostrarOutput(string, outputVerCanciones)
       
       #Frame usado para ver canciones

       frameVerCanciones= Frame(self)
       nombreVerCanciones = Label(frameVerCanciones, text="Canciones creadas en la app", font=("Verdana", 16), fg = "#31a919")
       descVerCanciones = Label(frameVerCanciones,text="Recuerde que puede que inicialmente no se observe la totalidad de las canciones \n Puebe a mover rueda del mouse para ver más canciones",font=("Verdana", 12))
       refrescarVerCanciones = Button(frameVerCanciones, text="Mostrar/Refescar", font=("Verdana", 12), fg="white",bg="#31a919", command=refrescarCanciones)
       


       outputVerCanciones= Text(frameVerCanciones, height=100, font=("Verdana", 10))
       Ventana_principal.frames.append(frameVerCanciones)

       nombreVerCanciones.pack()
       descVerCanciones.pack()
       refrescarVerCanciones.pack(pady=(10,10))

       Ventana_principal.frames.append(frameVerCanciones)

      
    
       self.mainloop()
