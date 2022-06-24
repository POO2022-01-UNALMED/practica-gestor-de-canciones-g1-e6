from gestorAplicacion.personas.Persona import Persona
from gestorAplicacion.elementosLibreria.Me_gusta import Me_gusta
from gestorAplicacion.elementosLibreria.Favoritos import Favoritos
from gestorAplicacion.elementosLibreria.Mis_artistas import Mis_artistas
from gestorAplicacion.elementosLibreria.Biblioteca import Biblioteca

class Usuario(Persona):
    usuarios=[]
    def __init__(self, nombre):
        self.nombre=nombre
        self._mis_artistas= Mis_artistas(self)
        self._biblioteca= Biblioteca(self)
        self._playlists=[]
        self._mis_me_gusta=Me_gusta(self)
        self._mis_favoritos=Favoritos(self)
        Usuario.usuarios.append(self)
    def datosPersona(self):
        return "Nombre: " + self.nombre + "\n" + "Tipo: Usuario normal" + "\n" +"numero de canciones en me gusta: " + len(self._mis_me_gusta.getCanciones()) + "\n" + "número de canciones en favoritos: " + len(self._mis_favoritos.getCanciones())
    def getMis_artistas(self):
        return self._mis_artistas
    def setMis_artistas(self, arti):
        self._mis_artistas=arti
    def getBiblioteca(self):
        return self._biblioteca
    def getPlaylists(self):
        return self._playlists
    def getMis_me_gusta(self):
        return self._mis_me_gusta
    def getMis_favoritos(self):
        return self._mis_favoritos
    def agg_Megusta(self, cancion):
        self._mis_me_gusta.agg_cancion(cancion)
    def elim_Megusta(self, cancion):
        presente=False
        for i in self._mis_me_gusta.getCanciones():
            if i==cancion:
                presente=True
                break
        if presente==True:
            self._mis_me_gusta.elim_cancion(cancion)
            return("cancion eliminada de mis me gusta")
        else:
            return("ERROR: la cancion no existe en mis me gusta")
    def agg_MisFavoritos(self, cancion):
        self._mis_favoritos.agg_cancion(cancion)
    def elim_MisFavoritos(self, cancion):
        presente=False
        for i in self._mis_favoritos.getCanciones():
            if i==cancion:
                presente=True
                break
        if presente==True:
            self._mis_favoritos.elim_cancion(cancion)
            return("cancion eliminada de mis favoritos")
        else:
            return("ERROR: la cancion no existe en mis favoritos")
    def agg_Playlist(self, playlist):
        self._playlists.append(playlist)
    def elim_Playlist(self, playlist):
        presente=False
        for i in self._playlists:
            if i==playlist:
                presente=True
                break
        if presente==True:
            self._playlists.remove(playlist)
            return("playlist eliminada")
        else:
            return("ERROR: la playlist no existe o no esta agregada")
        
        
    def cancionSeRepite(playlist1, playlist2):
        canciones1 = playlist1.getCanciones()
        canciones2 = playlist2.getCanciones()
        
        repetidas = []
        
        for cancion in canciones1:
            if cancion in canciones2:
                repetidas.append(cancion)
            
        respuesta = "se repiten: \n"
        
        if len(repetidas) == 0:
            return "No hay canciones repetidas"
        else:
            for cancion in repetidas:
                respuesta = respuesta + cancion.getNombre() + "del artista " + cancion.getArtista().getNombre() + "\n"
            return respuesta    

    def duracion_total(self):
        playlists = self.getPlaylists()
        duracion_total = 0

        for playlist in playlists:
            canciones = playlist.getCanciones()
            duracion_total_playlist = 0

            for cancion in canciones:
                duracion_total_playlist += cancion.getDuracion()
            duracion_total += duracion_total_playlist

        return duracion_total

    
    def artista_favorito(self):
        artistillas = self.getMis_artistas().getArtistas()

        if len(artistillas) == 0:
            return "no hay ningun artista en mis artistas"

        artistaYNumero = {}

        for playlist in self.getPlaylists():
            for cancion in playlist.getCanciones():
                if cancion.getArtista() in artistillas and cancion.getArtista() in artistaYNumero:
                    artistaYNumero[cancion.getArtista()] += 1
                else:
                    artistaYNumero[cancion.getArtista()] = 1
                    
        #como saben, acá se hace mimimimi
        return  max(artistaYNumero, key=artistaYNumero.get)

            
        


