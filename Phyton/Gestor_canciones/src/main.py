from gestorAplicacion.personas.Usuario import Usuario
from gestorAplicacion.personas.Artista import Artista
from gestorAplicacion.elementosLibreria.Genero import Genero
from gestorAplicacion.elementosLibreria.Cancion import Cancion
from interfazGrafica.inicio import Inicio
from baseDatos.Deserializador import Deserializador
def main():
    mi_app = Inicio()
    return 0

if __name__ == '__main__':
    #Deserializador.deserializarTodo()
    u1=Usuario("Carlos")
    u2=Usuario("Manuel")
    u3=Usuario("David")
    A1= Artista("El pela pollos", "pOLLITOX", Genero.MUSICA_PARA_PELAR_POLLOS)
    A2= Artista("TusaBrr", "Brr Brr", Genero.MUSICA_PARA_TUSAR_CALVOS)
    C1= Cancion("Pollitox locos", 3.20, A1, Genero.MUSICA_PARA_PELAR_POLLOS)
    C2= Cancion("La abuela está de pelos", 2.5, A2, Genero.MUSICA_PARA_TUSAR_CALVOS)
    C3= Cancion("La peladera", 1.50, A1, Genero.MUSICA_PARA_PELAR_POLLOS)
    C4= Cancion("El tuso hernandez", 2.6, A2, Genero.MUSICA_PARA_TUSAR_CALVOS)
    C5= Cancion("Chick chick", 1.50, A1, Genero.MUSICA_PARA_PELAR_POLLOS)
    u1.agg_Megusta(C1)
    u1.agg_Megusta(C4)
    u1.agg_Megusta(C5)
    Inicio()