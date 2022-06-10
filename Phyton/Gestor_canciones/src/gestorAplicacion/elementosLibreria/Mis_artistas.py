class Mis_artistas():
    mis_artistas=[]
    def __init__(self, usuario):
        self._usuario=usuario
        self._artistas=[]
        Mis_artistas.mis_artistas.append(self)
    def getUsuario(self):
        return self._usuario
    def setUsuario(self, usuario):
        self._usuario=usuario
    def getArtistas(self):
        return self._artistas
    def setArtistas(self, artistas):
        self._artistas=artistas
    def agg_artista(self, artista):
        self._artistas.append(artista)
    def elim_artista(self, artista):
        presente=False
        for i in self._artistas:
            if i==artista:
                presente=True
                break
        if presente==True:
            self._artistas.remove(artista)
            return("artista eliminado de mis artistas")
        else:
            return("ERROR: el artista no esta en mis artistas")