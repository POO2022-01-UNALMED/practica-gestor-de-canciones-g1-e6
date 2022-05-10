package Personas;
import java.util.ArrayList;
import ElementosLibreria.Me_gusta;
import ElementosLibreria.Mis_artistas;
import ElementosLibreria.Playlist;
import ElementosLibreria.Biblioteca;
import ElementosLibreria.Cancion;

public class Usuario {
    public String nombre;
    private Me_gusta mis_me_gusta;
    private Mis_artistas mis_artistas;
    private ArrayList<Playlist> playlists;
    private Biblioteca mi_biblioteca;
    public Usuario() {
    	
    }
	public Usuario(String nombre) {
		super();
		this.nombre = nombre;
		mis_me_gusta= new Me_gusta(this);
		mis_artistas= new Mis_artistas(this);
		playlists= new ArrayList<Playlist>();
		mi_biblioteca= new Biblioteca(this);
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public Me_gusta getMis_me_gusta() {
		return mis_me_gusta;
	}
	public void setMis_me_gusta(Me_gusta mis_me_gusta) {
		this.mis_me_gusta = mis_me_gusta;
	}
	public Mis_artistas getMis_artistas() {
		return mis_artistas;
	}
	public void setMis_artistas(Mis_artistas mis_artistas) {
		this.mis_artistas = mis_artistas;
	}
	public ArrayList<Playlist> getPlaylists() {
		return playlists;
	}
	public void setPlaylists(ArrayList<Playlist> playlists) {
		this.playlists = playlists;
	}
    public void agg_Megusta(Cancion cancion) {
    	mis_me_gusta.agg_cancion(cancion);
    }
    public String elim_Megusta(Cancion cancion) {
    	boolean presente=false;
    	for (Cancion c: mis_me_gusta.getCanciones()) {
    		if (cancion==c){
    			presente=true; 
    		}
    
    	}
    	if (presente==true) {
    		mis_me_gusta.elim_cancion(cancion);
    		return"cancion eliminada de mis me gusta";
    	}
    	else {
    		return"ERROR: la cancion no está en mis me gusta";
    	}
    }
    //Y si ya está o no existe el artista?
    public void agg_Miartistas(Artista artista) {
    	mis_artistas.agg_artista(artista);
    }
    public String elim_Misartistas(Artista artista) {
    	boolean presente=false;
    	for (Artista c: mis_artistas.getArtistas()) {
    		if (artista==c){
    			presente=true; 
    		}
    
    	}
    	if (presente==true) {
    		mis_artistas.elim_artista(artista);
    		return"artista eliminado de mis artistas";
    	}
    	else {
    		return"ERROR: el artista no está en mis artistas";
    	}
    }
    public void agg_Playlist(Playlist playlist) {
    	playlists.add(playlist);
    }
    public String elim_Playlist(Playlist playlist) {
    	boolean presente=false;
    	for (Playlist c: playlists) {
    		if (playlist==c){
    			presente=true; 
    		}
    
    	}
    	if (presente==true) {
    		playlists.remove(playlist);
    		return"playlist eliminada";
    	}
    	else {
    		return"ERROR: la playlist no existe o no está agregada";
    	}
    }
}
