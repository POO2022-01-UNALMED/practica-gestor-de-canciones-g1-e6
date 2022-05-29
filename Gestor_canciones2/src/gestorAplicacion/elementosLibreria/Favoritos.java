package gestorAplicacion.elementosLibreria;

import java.io.Serializable;
import java.util.ArrayList;

import gestorAplicacion.personas.Usuario;

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
	public String creadorPlaylist() {
		  return"Esta playlist fue creada por defecto"+"\n"+"Spotifoy todos los derechos reservados";	
		}
	public String toString() {
		return"La playlist Favoritos es creada por Spotifoy al crear el usuario"+"\n"+ "y tiene el id "+getId_real();
	}	
}
