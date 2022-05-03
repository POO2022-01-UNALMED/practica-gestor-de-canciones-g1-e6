package ElementosLibreria;
import Personas.Usuario;
import java.util.ArrayList;

public class Me_gusta extends Playlist{
	
	public Me_gusta(Usuario creador){
		super("Me gusta", new ArrayList<Cancion>(), 0, 0, creador, 1);
	}
	
	public void unlike(Cancion cancion) {
		
	}
}