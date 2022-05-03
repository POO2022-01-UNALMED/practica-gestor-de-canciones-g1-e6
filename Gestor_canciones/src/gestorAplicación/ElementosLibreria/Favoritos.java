package ElementosLibreria;

import java.util.ArrayList;

import Personas.Usuario;

public class Favoritos extends Playlist{
	
	public Favoritos(Usuario creador){
		super("Favoritos", new ArrayList<Cancion>(), 0, 0, creador, 2);
	}
}
