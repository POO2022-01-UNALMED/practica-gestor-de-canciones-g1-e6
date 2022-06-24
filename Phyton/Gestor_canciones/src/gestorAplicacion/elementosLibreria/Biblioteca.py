from random import random
from gestorAplicacion.elementosLibreria.Genero import Genero
from gestorAplicacion.elementosLibreria.Cancion import Cancion
class Biblioteca:
    bibliotecas = []
    def __init__(self, usuario):
        self._usuario=usuario
        Biblioteca.bibliotecas.append(self)
        
    def getBibliotecas(self):
        return Biblioteca.bibliotecas
    def setBibliotecas(self, bibliotecas):
        Biblioteca.bibliotecas = bibliotecas
    
    def getUsuario(self):
        return self._usuario
    def setUsuario(self, usuario):
        self._usuario = usuario
        
    def acceder_misartistas(self):
        return self._usuario.getMis_artistas()
    
    
    
    def repo_aleatoria(self, playlist):
        if playlist in self._usuario.getPlaylists():
            index = int(random()* len(playlist.getCanciones()))
            return playlist.getCanciones()[index].play()
        else:
            return "La playlist "+ playlist.getNombre()+"no existe en el usuario "+self._usuario.getNombre()
    
    		