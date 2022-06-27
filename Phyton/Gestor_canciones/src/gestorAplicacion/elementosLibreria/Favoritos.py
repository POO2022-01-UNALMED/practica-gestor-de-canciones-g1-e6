from gestorAplicacion.elementosLibreria.Playlist import Playlist
class Favoritos(Playlist):
    favoritos = []
    def __init__(self, creador):
      super().__init__(creador, "Favoritos")
      Favoritos.favoritos.append(self)
    def creadorPlaylist(self):
        return   "Esta playlist fue creada por defecto"+"\n"+"Spotifoy todos los derechos reservados"
    
    def toString(self):
        return f"La playlist Favoritos es creada por Spotifoy al crear el usuario\n y tiene el id {super().getId_real()}"