from gestorAplicacion.elementosLibreria.Genero import Genero
from gestorAplicacion.personas.Persona import Persona
class Artista(Persona):
    id_artista=1
    artistas=[]
    def __init__(self, nombre, presentacion = "Presentación por defecto", genero = Genero.MUSICA_PARA_PELAR_POLLOS):
        self.nombre=nombre
        self._canciones=[]
        self._presentacion=presentacion
        self._genero=genero
        self._id_realA=Artista.id_artista
        Artista.id_artista+=1
        Artista.artistas.append(self)
    def datosPersona(self):
        return "Nombre: " + self.nombre + "\n" + "Tipo: Artista" + "\n" +"Presentacion en app: " + self._presentacion + "\n" + "número de canciones creadas: " + str(len(self._canciones))
    def getCanciones(self):
        return self._canciones
    def setCanciones(self,canciones):
        self._canciones=canciones
    def getPresentacion(self):
        return self._presentacion
    def setPresentacion(self, presentacion):
        self._presentacion=presentacion
    def getGenero(self):
        return self._genero
    def setGenero(self, genero = Genero.MUSICA_PARA_PELAR_POLLOS):
        self._genero=genero
    def getId_artista(self):
        return self._id_realA