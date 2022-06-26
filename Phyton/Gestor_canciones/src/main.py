from gestorAplicacion.personas.Usuario import Usuario
from gestorAplicacion.personas.Artista import Artista
from gestorAplicacion.elementosLibreria.Genero import Genero
from gestorAplicacion.elementosLibreria.Cancion import Cancion
from gestorAplicacion.elementosLibreria.Playlist import Playlist
from interfazGrafica.inicio import Inicio
from baseDatos.Deserializador import Deserializador
def main():
    mi_app = Inicio()
    mi_app.mainloop()
    return 0

if __name__ == '__main__':
    Deserializador.deserializarTodo()

    #Casos de prueba creados
    
    """ Cancion.cancionesCreadas=[]
    Usuario.usuarios=[]
    Artista.artistas=[]
    Playlist.playlists=[]
    test9 =Usuario("Carlos")
    test=  Usuario("Manuel")
    test1= Usuario("PachoGOD")
    test6=Artista("El rompe traperas", "Baby brrr brrrr", Genero.REGGAETON)
    test7= Artista("bad chicken", "tssss", Genero.MUSICA_PARA_PELAR_POLLOS)
    test8=Artista("el motila abuelas", "yeah", Genero.MUSICA_PARA_TUSAR_CALVOS)
    test12=Artista("los gansos rosas", "you know where you are", Genero.ROCK)
    test13=Artista("Hector lavoe", "La calle es una selva de cemento", Genero.SALSA)
    test14=Artista("Resibalvin","si", Genero.RAP)
    test2=Cancion("A lavar el patio", 180, test6, Genero.REGGAETON)
    test15=Cancion("baños limpios y relucientes con salvo", 150, test6, Genero.REGGAETON) 
    test10=Cancion("guelkon turi yangol", 120, test12, Genero.ROCK) 
    test16=Cancion("La leyenda de la chucha y el culebrero", 250, test12, Genero.ROCK)
    test3=Cancion("El patito Juan", 180, test7, Genero.MUSICA_PARA_PELAR_POLLOS) 
    test5=Cancion("A pelar pollos", 120, test6, Genero.MUSICA_PARA_PELAR_POLLOS)
    test17=Cancion("La abuela esta de pelos", 75, test8,Genero.MUSICA_PARA_TUSAR_CALVOS) 
    test4= Cancion("Vamo a trapear", 120, test8, Genero.MUSICA_PARA_TUSAR_CALVOS)
    test18= Cancion("Tiraera a marbelle", 546, test14, Genero.RAP)
    test19= Cancion("La visita a bellavista", 134, test14, Genero.RAP) 
    test20= Cancion("El gran baron", 180, test13, Genero.SALSA) 
    test21= Cancion("Juanito alimaña", 180, test13, Genero.SALSA)	  
    test11= Playlist(test1,"Mejores voces femeninas de todos los tiempos") 
    test22= Playlist(test, "Mejores canciones para pelar pollos en rionegro un domingo")
    test23= Playlist(test9, "Aprende a motilar con esta musica para tusar calvos")
    test11.agg_cancion(test2) 
    test11.agg_cancion(test10)
    test11.agg_cancion(test18) 
    test22.agg_cancion(test10)
    test22.agg_cancion(test5) 
    test23.agg_cancion(test2)
    test23.agg_cancion(test17) 
    test23.agg_cancion(test18)
    test.agg_Playlist(test11) 
    test.agg_Playlist(test23)
    test1.agg_Playlist(test22) 
    test9.agg_Megusta(test2)
    test9.agg_Megusta(test3) 
    test9.agg_Megusta(test4)
    test9.agg_Megusta(test10) 
    test.agg_Megusta(test2) 
    test.agg_Megusta(test17)
    test.agg_Megusta(test16) 
    test.agg_Megusta(test15) 
    test1.agg_Megusta(test2)
    test1.agg_Megusta(test19) 
    test1.agg_Megusta(test21)
    test1.agg_Megusta(test10) 
    test9.agg_MisFavoritos(test20)
    test9.agg_MisFavoritos(test2) 
    test9.agg_MisFavoritos(test15)
    test9.agg_MisFavoritos(test17) 
    test.agg_MisFavoritos(test21)
    test.agg_MisFavoritos(test18) 
    test.agg_MisFavoritos(test3)
    test.agg_MisFavoritos(test16) 
    test1.agg_MisFavoritos(test20)
    test1.agg_MisFavoritos(test2) 
    test1.agg_MisFavoritos(test16)
    test1.agg_MisFavoritos(test3) 
    test9.getMis_artistas().getArtistas().append(test14)
    test9.getMis_artistas().getArtistas().append(test12) 
    test9.getMis_artistas().getArtistas().append(test8)
    test.getMis_artistas().getArtistas().append(test6) 
    test.getMis_artistas().getArtistas().append(test7)
    test.getMis_artistas().getArtistas().append(test12) 
    test1.getMis_artistas().getArtistas().append(test6)
    test1.getMis_artistas().getArtistas().append(test12) 
    test1.getMis_artistas().getArtistas().append(test14) """ 
    main()