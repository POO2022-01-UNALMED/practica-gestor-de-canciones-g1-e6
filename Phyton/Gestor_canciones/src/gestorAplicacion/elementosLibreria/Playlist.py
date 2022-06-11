

class Playlist():
    playlists = []
    
    def __init__(self, creador, nombre):
        self.nombre = nombre
        self._creador = creador
        Playlist.playlists.append(self)
        self.duracion = 0
        self.canciones = []
        self.numero_canciones = 0
        
    def getCreador(self):
        return self._creador
    def setCreador(self, creador):
        self._creador = creador
        
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getDuracion(self):
        return self.duracion
    def setDuracion(self, duracion):
        self.duracion = duracion
        
    def getCanciones(self):
        return self.canciones
    def setCanciones(self, canciones):
        self.canciones = canciones
        
    def getNumeroCanciones(self):
        return self.numero_canciones
    def setNumeroCanciones(self, numero):
        self.numero_canciones = numero
        
    
    def creadorPlaylist(self):
        return "Esta playlist fue creada por " + self.getCreador.getNombre()
    
    def agg_cancion(self, cancion):
        if cancion in self.canciones:
            return "la canción ya se encuentra en la playlist"
        else:
            self.canciones.append(cancion)
            self.numero_canciones += 1
            self.duracion += cancion.getDuracion()
            return "la canción fue agregada con exito..."
        
    def elim_cancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            self.numero_canciones -= 1
            self.duracion -= cancion.getDuracion()
            return "la cancion ha sido eliminada de la playlist exitosamente"
        else:
            return "la cancion no se encontraba en la playlist"        