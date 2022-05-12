package gestorAplicacion.Personas;

import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.ElementosLibreria.*;

public class Artista implements Serializable {

	private static final long serialVersionUID = 1L;
	private static ArrayList<Artista> artistas;
	static {
		artistas = new ArrayList<Artista>();
	}
	
    public String nombre;
    private ArrayList<Cancion> canciones;
    private String presentacion;
    private Genero genero;
    private int id_artista;
    
	public Artista(String nombre, ArrayList<Cancion> canciones, String presentacion, Genero genero, int id_artista) {
		super();
		this.nombre = nombre;
		this.canciones = canciones;
		this.presentacion = presentacion;
		this.genero = genero;
		this.id_artista = id_artista;
		artistas.add(this);
	}
	
	public static ArrayList<Artista> getArtistas() {
		return artistas;
	}

	public static void setArtistas(ArrayList<Artista> artistas) {
		Artista.artistas = artistas;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void setPresentacion(String presentacion) {
		this.presentacion = presentacion;
	}

	public ArrayList<Cancion> getCanciones() {
		return canciones;
	}

	public void setCanciones(ArrayList<Cancion> canciones) {
		this.canciones = canciones;
	}

	public String getPresentacion() {
		return presentacion;
	}

	public void change_Presentacion(String nuevo) {
		this.presentacion = nuevo;
	}

	public Genero getGenero() {
		return genero;
	}

	public void setGenero(Genero genero) {
		this.genero = genero;
	}

	public int getId_artista() {
		return id_artista;
	}

	public void setId_artista(int id_artista) {
		this.id_artista = id_artista;
	}
	
	public void agg_Cancion(Cancion cancion) {
		canciones.add(cancion);
	}
	public String elim_Cancion(Cancion cancion) {
    	boolean presente=false;
    	for (Cancion c: canciones) {
    		if (cancion==c){
    			presente=true; 
    		}
    
    	}
    	if (presente==true) {
    		canciones.remove(cancion);
    		return"cancion eliminada";
    	}
    	else {
    		return"ERROR: la cancion no est� subida o no es del artista";
    	}
    }
    
    
}
