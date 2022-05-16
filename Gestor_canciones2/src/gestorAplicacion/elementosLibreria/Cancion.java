package gestorAplicacion.elementosLibreria;

import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.personas.Artista;

public class Cancion  implements Serializable {
	
	private static final long serialVersionUID = 1L;
	
    public String nombre;
    private int duracion;
    private Artista artista;
    private Genero genero;
    private static int id_cancion = 1;
	private int id_realC;
    public static ArrayList<Cancion> cancionesCreadas= new ArrayList<Cancion>(); //atributo estatico para buscar en todas las canciones creadas
    
    public Cancion() {
    	
    }
    public Cancion(String nombre, int duracion, Artista artista, Genero genero){
        this.nombre = nombre;
        this.duracion = duracion;
        this.artista = artista;
        this.genero = genero;
        artista.getCanciones().add(this);
		id_realC = id_cancion;
		id_cancion++;
        Cancion.cancionesCreadas.add(this);
    }
    
	public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }
    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }
    public int getDuracion() {
        return duracion;
    }
    public void setArtista(Artista artista) {
        this.artista = artista;
    }
    public Artista getArtista() {
        return artista;
    }
    public void setGenero(Genero genero) {
        this.genero = genero;
    }
    public Genero getGenero() {
        return genero;
    }
    public void setId_cancion(int id_cancion) {
        this.id_realC = id_cancion;
    }
    public int getId_cancion() {
        return id_realC;
    }
    public static ArrayList<Cancion> getCancionesCreadas() {
		return cancionesCreadas;
	}

	public static void setCancionesCreadas(ArrayList<Cancion> cancionesCreadas) {
		Cancion.cancionesCreadas = cancionesCreadas;
	}

	public String play(){
        return "reproduciendo"+ this.nombre;
    }

    public String pause(){
        return "la canción" + this.nombre + "ha sido pausada";
    }
}
