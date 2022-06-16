from random import random
from typing_extensions import Self
from Genero import Genero
from Cancion import Cancion
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
    def recomendar_cancion(self):
        rock=0
        reggaeton=0
        salsa=0
        rap=0
        pelar=0
        tusar=0
        for cancion in self.getMis_me_gusta().getCanciones():
            if cancion.getGenero()==Genero.ROCK: rock+=1
            elif cancion.getGenero()==Genero.REGGAETON: reggaeton+=1
            elif cancion.getGenero()==Genero.RAP: rap+=1
            elif cancion.getGenero()==Genero.SALSA: salsa+=1
            elif cancion.getGenero()==Genero.MUSICA_PARA_PELAR_POLLOS: pelar+=1
            elif cancion.getGenero()==Genero.MUSICA_PARA_TUSAR_CALVOS: tusar+=1
        mayor=rock 
        mayorGen=Genero.ROCK   
        if (reggaeton>mayor): mayor=reggaeton, mayorGen=Genero.REGGAETON
        if (salsa>mayor): mayor=salsa, mayorGen=Genero.SALSA
        if (rap>mayor): mayor=rap, mayorGen=Genero.RAP
        if (pelar>mayor): mayor=pelar, mayorGen=Genero.MUSICA_PARA_PELAR_POLLOS
        if (tusar>mayor): mayor=tusar, mayorGen=Genero.MUSICA_PARA_TUSAR_CALVOS
        for cancion in Cancion.getCancionesCreadas():
          igual=False
          if cancion.getGenero()==mayorGen:
            for c1 in self._usuario.getMis_me_gusta().getCanciones():
                if c1.getNombre()==cancion.getNombre:
                    igual=True
                    break
            if igual==False:
                recomendacion=cancion
          else:
            continue
        if recomendacion==None:
            recomendacion=(Cancion.getCancionesCreadas())[0]
        return recomendacion
    		