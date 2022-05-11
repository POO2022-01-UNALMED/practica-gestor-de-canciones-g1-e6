package Personas;
import java.util.ArrayList;
import ElementosLibreria.*;
public class Artista {
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
    		return"ERROR: la cancion no está subida o no es del artista";
    	}
    }
    
    
}
