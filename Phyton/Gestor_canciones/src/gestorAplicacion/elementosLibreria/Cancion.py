from gestorAplicacion.personas.Artista import Artista

class Cancion:
    id_cancion = 0
    cancionesCreadas = []
    def __init__(self, nombre, duracion, artista, genero):
        self.nombre = nombre
        self._duracion = duracion
        self._artista = artista
        self._genero = genero
        Artista.getCanciones.append(self)
        id_cancion += 1
        self._id_realC = id_cancion
        Cancion.cancionesCreadas.append(self)
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setDuracion(self, duracion):
        self._duracion = duracion
    def getDuracion(self):
        return self._duracion
    def setArtista(self, artista):
        self._artista = artista
    def getArtista(self):
        return self._artista
    def setGenero(self, genero):
        self._genero = genero
    def getGenero(self):
        return self._genero
    def setId_cancion(self, id_cancion):
        self._id_realC = id_cancion
    def getId_cancion(self):
        return self._id_realC
    def getCancionesCreadas(self):
        return self.cancionesCreadas
    def setCancionesCreadas(self, cancionesCreadas):
        self.cancionesCreadas = cancionesCreadas
    def play(self):
        return "Reproduciendo: ", self.nombre
    def pause(self):
        return "la cancion", self.nombre ,"ha sido pausada"