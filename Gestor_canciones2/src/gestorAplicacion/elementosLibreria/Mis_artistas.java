package gestorAplicacion.elementosLibreria;

import java.io.Serializable;
import java.util.ArrayList;
import gestorAplicacion.personas.*;

public class Mis_artistas  implements Serializable {
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Mis_artistas> mis_artistas;
	static {
		mis_artistas = new ArrayList<Mis_artistas>();
	}
    public static ArrayList<Mis_artistas> getMis_artistas() {
		return mis_artistas;
	}
	public static void setMis_artistas(ArrayList<Mis_artistas> mis_artistas) {
		Mis_artistas.mis_artistas = mis_artistas;
	}
	private ArrayList<Artista> artistas;
    private Usuario usuario;
    public Mis_artistas(Usuario usuario) {
    	this.usuario=usuario;
    	mis_artistas.add(this);
    }
	public ArrayList<Artista> getArtistas() {
		return artistas;
	}
	public void setArtistas(ArrayList<Artista> artistas) {
		this.artistas = artistas;
	}
	public Usuario getUsuario() {
		return usuario;
	}
	public void setUsuario(Usuario usuario) {
		this.usuario = usuario;
	}
    public void agg_artista(Artista artista) {
    	artistas.add(artista);
    }
    public String elim_artista(Artista artista) {
    	boolean presente=false;
    	for (Artista c: artistas) {
    		if (artista==c){
    			presente=true; 
    		}
    
    	}
    	if (presente==true) {
    		artistas.remove(artista);
    		return"artista eliminado de mis artistas";
    	}
    	else {
    		return"ERROR: el artista no est� en mis artistas";
    	}
    }
}
