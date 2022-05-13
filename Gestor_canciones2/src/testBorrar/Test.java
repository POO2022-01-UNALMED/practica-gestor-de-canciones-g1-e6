package testBorrar;
import baseDatos.*;
import gestorAplicacion.personas.*;
import gestorAplicacion.elementosLibreria.*;
public class Test {

	public static void main(String[] args) {
		Deserializador.deserializarTodo();
		
		for(Artista i: Artista.getArtistas()) {
			System.out.println(i.getNombre());
		}
		
		Serializador.serializarTodo();
	}
}