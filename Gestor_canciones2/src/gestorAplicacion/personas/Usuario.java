package gestorAplicacion.personas;
import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.elementosLibreria.*;
import java.util.Hashtable;
import java.util.Map;

public class Usuario  implements Serializable, Persona {
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Usuario> usuarios;
	static {
		usuarios = new ArrayList<Usuario>();
	}
	
    public String nombre;
    private ArrayList<Playlist> playlists= new ArrayList<Playlist>();
    private final Me_gusta mis_me_gusta= new Me_gusta(this);
    private Mis_artistas mis_artistas;
    private Biblioteca mi_biblioteca;
    private final Favoritos mis_favoritos= new Favoritos(this);
    public Usuario() {
    	
    }
	public Usuario(String nombre) {
		this.nombre = nombre;
		mis_artistas= new Mis_artistas(this);
		mi_biblioteca= new Biblioteca(this);
		usuarios.add(this);
	}
	public String datosPersona() {
		return 
				"Nombre: " + nombre + "\n" + 
				"Tipo: Usuario normal" + "\n" +
				"numero de playlist: " + playlists.size() + "\n" + 
				"numero de canciones en me gusta: " + (mis_me_gusta.getCanciones().size()) + "\n" +
		        "numero de canciones en favoritos: " + (mis_favoritos.getCanciones().size());
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
    		return"ERROR: la cancion no existe en mis me gusta";
    	}
    }
    //Y si ya estï¿½ o no existe el artista?
    //vuelve y lo agrega todo bien
    public void agg_MisFavoritos(Cancion cancion) {
    	mis_favoritos.agg_cancion(cancion);
    }
    public String elim_MisFavoritos(Cancion cancion) {
    	boolean presente=false;
    	for (Cancion c: mis_favoritos.getCanciones()) {
    		if (cancion==c){
    			presente=true; 
    		}
    
    	}
    	if (presente==true) {
    		mis_favoritos.elim_cancion(cancion);
    		return"cancion eliminada de mis favoritos";
    	}
    	else {
    		return"ERROR: la cancion no existe en mis favoritos";
    	}
    }
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
    		return"ERROR: el artista no existe en mis artistas";
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
    		return"ERROR: la playlist no existe o no esta agregada";
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

	public int duracion_total(){
		ArrayList<Playlist> playlists = getPlaylists();
		int duracion_total = 0;

		for( Playlist p: playlists){
			ArrayList<Cancion> canciones = p.getCanciones();
			int duracion_total_playlist = 0;

			for(Cancion c: canciones){
				duracion_total_playlist = duracion_total_playlist + c.getDuracion();
			}
			duracion_total = duracion_total + duracion_total_playlist;

		}

		Playlist megusta = getMis_me_gusta();
		ArrayList<Cancion> canciones_gustar = megusta.getCanciones();
		for(Cancion c: canciones_gustar){
			duracion_total = duracion_total + c.getDuracion();
		}

		return duracion_total;
	}

	public String artista_favorito(){

		ArrayList<Artista> artistillas = getMis_artistas().getArtistas();

		//AcÃ¡ se crea el diccionario
		Hashtable<Artista, Integer> artistaYNumero = new Hashtable<Artista, Integer>();

		//AcÃ¡ se itera sobre todas las canciones de las playlists y se agregan sus artistas al diccionario
		for(Playlist p: getPlaylists()){
			for(Cancion c: p.getCanciones()){
				if(artistillas.contains(c.getArtista()) && artistaYNumero.containsKey(c.getArtista())){
					artistaYNumero.put(c.getArtista(), artistaYNumero.get(c.getArtista()) + 1);
				}else if(artistillas.contains(c.getArtista())){
					artistaYNumero.put(c.getArtista(), 1);
				}

			}
		}

		int mayorCanciones = 0;
		Artista mayorArtista = artistillas.get(0);

		// AcÃ¡ se itera sobre el diccionario para ver cual es el que tiene mÃ¡s canciones 
		for (Map.Entry<Artista, Integer> entry : artistaYNumero.entrySet()){
			if(entry.getValue() > mayorCanciones){
				mayorCanciones = entry.getValue();
				mayorArtista = entry.getKey();
			}
		}


		// AcÃ¡ se hace mimimimi

		return mayorArtista.getNombre();

	}
}
