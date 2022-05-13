package testBorrar;
import baseDatos.*;
import gestorAplicacion.personas.*;
import gestorAplicacion.elementosLibreria.*;
public class Test {

	public static void main(String[] args) {
		Deserializador.deserializarTodo();
		Artista test3 = new Artista("El pela pollos de Antioquia", null);
		for(Artista i: Artista.getArtistas()) {
			System.out.println(i.getNombre());
		}
		
		Serializador.serializarTodo();
	}
}