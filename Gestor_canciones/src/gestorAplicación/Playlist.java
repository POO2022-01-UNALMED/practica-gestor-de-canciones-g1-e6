package gestorAplicación;
import java.util.ArrayList;
import java.io.*;

public class Playlist {
	String nombre;
	ArrayList<Cancion> canciones = new ArrayList<Cancion>();
	int duracion;
	int numero_canciones;
	private Usuario creador;
	private int id_playlist;
	
	public Playlist(String nombre, ArrayList<Cancion> cancion, int duracion, int numero_canciones, Usuario creador,
			int id_playlist) {
		this.nombre = nombre;
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

	public void setDuracion(int duracion) {
		this.duracion = duracion;
	}

	public int getNumero_canciones() {
		return numero_canciones;
	}

	public void setNumero_canciones(int numero_canciones) {
		this.numero_canciones = numero_canciones;
	}

	public Usuario getCreador() {
		return creador;
	}

	public void setCreador(Usuario creador) {
		this.creador = creador;
	}

	public int getId_playlist() {
		return id_playlist;
	}

	public void setId_playlist(int id_playlist) {
		this.id_playlist = id_playlist;
	}

	public void agg_cancion(Cancion cancion) {
        canciones.add(cancion);
	}
	
	public void elim_cancion(Cancion cancion) {
		canciones.remove(cancion);
	}
	
	public Cancion repro_aleatoria() {
		int index = (int)(Math.random() * canciones.size());
		return canciones.get(index);
	}
}
