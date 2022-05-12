package gestorAplicacion.Personas;
import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.ElementosLibreria.Me_gusta;
import gestorAplicacion.ElementosLibreria.Mis_artistas;
import gestorAplicacion.ElementosLibreria.Playlist;
import gestorAplicacion.ElementosLibreria.Biblioteca;
import gestorAplicacion.ElementosLibreria.Cancion;

public class Usuario  implements Serializable {
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Usuario> usuarios;
	static {
		usuarios = new ArrayList<Usuario>();
	}
	
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
		usuarios.add(this);
	}
	public static ArrayList<Usuario> getUsuarios() {
		return usuarios;
	}
	public static void setUsuarios(ArrayList<Usuario> usuarios) {
		Usuario.usuarios = usuarios;
	}
	public Biblioteca getMi_biblioteca() {
		return mi_biblioteca;
	}
	public void setMi_biblioteca(Biblioteca mi_biblioteca) {
		this.mi_biblioteca = mi_biblioteca;
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
    		return"ERROR: la cancion no est� en mis me gusta";
    	}
    }
    //Y si ya est� o no existe el artista?
    //vuelve y lo agrega todo bien 
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
    		return"ERROR: el artista no est� en mis artistas";
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
    		return"ERROR: la playlist no existe o no est� agregada";
    	}
    }

	public String cancionSeRepite(Playlist playlist1, Playlist playlist2){
		ArrayList<Cancion> canciones1 = playlist1.getCanciones();
		ArrayList<Cancion> canciones2 = playlist2.getCanciones();

		ArrayList<Cancion> repetidas = new ArrayList<Cancion>();

		for(Cancion c: canciones1){
			if(canciones2.contains(c)){
				repetidas.add(c);
			}
		}
		String respuesta = new String("Se repiten");

		if (repetidas.isEmpty()){
			return "No hay canciones repetidas";
		}else{
			for(Cancion c: repetidas){
				respuesta = respuesta + c.getNombre() + " del artista " + c.getArtista().getNombre();
			}
			return respuesta;
		}
	}
}
