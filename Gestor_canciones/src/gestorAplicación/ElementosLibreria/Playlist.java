package ElementosLibreria;
import java.util.ArrayList;
import java.io.*;
import Personas.Usuario;

public class Playlist {
	private String nombre;
	private ArrayList<Cancion> canciones;
	private int duracion;
	private int numero_canciones;
	private String creador;
	private int id_playlist = 1;
	
	public Playlist(String nombre) {
		this.nombre = nombre;
		canciones = new ArrayList<Cancion>();
		duracion = 0;
		numero_canciones = 0;
		creador = Usuario.getNombre();
		id_playlist++;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public ArrayList<Cancion> getCanciones() {
		return canciones;
	}

	public void setCanciones(ArrayList<Cancion> canciones) {
		this.canciones = canciones;
	}

	public int getDuracion() {
		return duracion;
	}

	public int getNumero_canciones() {
		return numero_canciones;
	}

	public void setNumero_canciones(int numero_canciones) {
		this.numero_canciones = numero_canciones;
	}

	public String getCreador() {
		return creador;
	}

	public void setCreador(String creador) {
		this.creador = creador;
	}

	public int getId_playlist() {
		return id_playlist;
	}

	public void setId_playlist(int id_playlist) {
		this.id_playlist = id_playlist;
	}
	//se le ingresa la clase canción o el id?
	public void agg_cancion(Cancion cancion) {
		//Falta verificar si la canción existo o ya está
        canciones.add(cancion);
        numero_canciones++;
        this.duracion += cancion.getDuracion();
	} 
	//se le ingresa la clase canción o el id?
	public void elim_cancion(Cancion cancion) {
		//Falta verificar si la canción existo o ya está 
		canciones.remove(cancion);
		numero_canciones--;
		this.duracion -= cancion.getDuracion();
	}
	
	public Cancion repro_aleatoria() {
		int index = (int)(Math.random() * canciones.size());
		//Creo que falta poner bien el retorno
		return canciones.get(index);
	}
}
