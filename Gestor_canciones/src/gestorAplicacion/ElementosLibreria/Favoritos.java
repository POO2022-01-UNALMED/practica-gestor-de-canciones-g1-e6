package gestorAplicacion.ElementosLibreria;

import java.io.Serializable;
import java.util.ArrayList;

import gestorAplicacion.Personas.Usuario;

public class Favoritos extends Playlist{
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Favoritos> favoritos;
	static {
		favoritos = new ArrayList<Favoritos>();
	}
	
	public static ArrayList<Favoritos> getFavoritos() {
		return favoritos;
	}

	public static void setFavoritos(ArrayList<Favoritos> favoritos) {
		Favoritos.favoritos = favoritos;
	}

	public Favoritos(Usuario creador){
		super(creador, "Favoritos");
		favoritos.add(this);
	}
}
