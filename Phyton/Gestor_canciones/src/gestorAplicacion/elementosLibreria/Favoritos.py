from Playlist import Playlist
class Favoritos(Playlist):
    favoritos = []
    def _init_(self, creador):
      super()._init_(self, creador, "Favoritos")
      Favoritos.favoritos.append(self)
    def creadorPlaylist(self):
        return   "Esta playlist fue creada por defecto"+"\n"+"Spotifoy todos los derechos reservados"
    def toString():
        return "La playlist Favoritos es creada por Spotifoy al crear el usuario"+"\n"+ "y tiene el id "+super().getId_real()