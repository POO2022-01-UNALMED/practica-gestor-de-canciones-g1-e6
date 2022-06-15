import pickle
from gestorAplicacion.elementosLibreria.Cancion import Cancion
from gestorAplicacion.elementosLibreria.Biblioteca import Biblioteca
from gestorAplicacion.elementosLibreria.Favoritos import Favoritos
from gestorAplicacion.elementosLibreria.Me_gusta import Me_gusta
from gestorAplicacion.elementosLibreria.Mis_artistas import Mis_artistas
from gestorAplicacion.elementosLibreria.Playlist import Playlist
from gestorAplicacion.personas.Artista import Artista
from gestorAplicacion.personas.Usuario import Usuario
import pathlib
import os

class Deserializador():
    
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()
        return lista
        # Cierro el archivo
    
    def deserializarTodo():
        Biblioteca.bibliotecas = Deserializador.deserializar(Biblioteca.bibliotecas, "Biblioteca")
        Cancion.cancionesCreadas =  Deserializador.deserializar(Cancion.cancionesCreadas, "Canciones")
        Favoritos.favoritos = Deserializador.deserializar(Favoritos.favoritos, "Favotitos")
        Me_gusta.me_gustas = Deserializador.deserializar(Me_gusta.me_gustas, "Me gusta")
        Mis_artistas.mis_artistas = Deserializador.deserializar(Mis_artistas.mis_artistas, "Mis artistas")
        Playlist.playlists = Deserializador.deserializar(Playlist.playlists, "Playlists")
        Artista.artistas = Deserializador.deserializar(Artista.artistas, "Artistas")
        Usuario.usuarios = Deserializador.deserializar(Usuario.usuarios, "Usuarios")
        
    