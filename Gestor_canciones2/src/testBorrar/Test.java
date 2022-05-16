package testBorrar;
import java.util.ArrayList;

import baseDatos.*;
import gestorAplicacion.personas.*;
import gestorAplicacion.elementosLibreria.*;
public class Test {

	public static void main(String[] args) {
		Deserializador.deserializarTodo();
		Usuario test9 = new Usuario("Carlos");
		Biblioteca test11 = new Biblioteca(test9);
		Artista test6 = new Artista("El rompe traperas", "Baby brrr brrrr", Genero.REGGAETON);
		Cancion test8 = new Cancion("A lavar el patio", 180, test6, Genero.REGGAETON);
		Cancion test12 = new Cancion("El patito Juan", 180, test6, Genero.MUSICA_PARA_PELAR_POLLOS);
		Cancion test7 = new Cancion("Vamo a trapear", 120, test6, Genero.MUSICA_PARA_PELAR_POLLOS);
		Cancion test10 = new Cancion("A pelar pollos", 120, test6, Genero.MUSICA_PARA_PELAR_POLLOS);
		test9.agg_Megusta(test8);
		test9.agg_Megusta(test7);
		test9.agg_Megusta(test10);
		System.out.println(test9.datosPersona());
		
		System.out.println("Canción a recomendar: "+test11.recomendar_cancion().getNombre());
		for(Artista i: Artista.getArtistas()) {
			System.out.println(i.getNombre());
		}
		
		Serializador.serializarTodo();
	}
}