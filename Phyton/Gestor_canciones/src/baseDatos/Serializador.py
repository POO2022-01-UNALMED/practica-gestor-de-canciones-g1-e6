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

def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        try:
            # Creo el archivo pickle para guardar los objetos
            picklefile = open(camino(className), 'wb')
            # pickle el objeto en el archivo
            pickle.dump(lista, picklefile)
            # cierro el archivo para guardar
            picklefile.close()
            
        except:
            print("paila tuqui tuqui muñeco")

def serializarTodo():

        serializar(Biblioteca.bibliotecas, "Biblioteca")
        serializar(Cancion.cancionesCreadas, "Canciones")
        serializar(Favoritos.favoritos, "Favotitos")
        serializar(Me_gusta.me_gustas, "Me gusta")
        serializar(Mis_artistas.mis_artistas, "Mis artistas")
        serializar(Playlist.playlists, "Playlists")
        serializar(Artista.artistas, "Artistas")
        serializar(Usuario.usuarios, "Usuarios")

