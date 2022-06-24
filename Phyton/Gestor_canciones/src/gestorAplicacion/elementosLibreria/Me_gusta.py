from gestorAplicacion.elementosLibreria.Playlist import Playlist
class Me_gusta(Playlist):
    #Es broma, pero si quieres no lo es
    me_gustas = []

    def __init__(self, creador):
      super().__init__( creador, "Me gusta")
      Me_gusta.me_gustas.append(self)
    def creadorPlaylist(self):
        return   "Esta playlist fue creada por defecto"+"\n"+"Spotifoy todos los derechos reservados"
    def toString():
        return "La playlist Me gusta es creada por Spotifoy al crear el usuario"+"\n"+ "y tiene el id "+super().getId_real()