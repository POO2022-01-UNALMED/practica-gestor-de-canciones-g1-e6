package ElementosLibreria;
import java.util.ArrayList;
import Personas.*;
public class Mis_artistas {
    private ArrayList<Artista> artistas;
    private Usuario usuario;
    public Mis_artistas(Usuario usuario) {
    	this.usuario=usuario;
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
    		return"ERROR: el artista no está en mis artistas";
    	}
    }
}
