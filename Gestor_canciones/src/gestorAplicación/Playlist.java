package gestorAplicación;
import java.util.ArrayList;

public class Playlist {
	String nombre;
	ArrayList<Cancion> cancion;
	int duracion;
	int numero_canciones;
	private Usuario creador;
	private int id_playlist;
	
	public Playlist(String nombre, ArrayList<Cancion> cancion, int duracion, int numero_canciones, Usuario creador,
			int id_playlist) {
		super();
		this.nombre = nombre;
	}

	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public ArrayList<Cancion> getCancion() {
		return cancion;
	}

	public void setCancion(ArrayList<Cancion> cancion) {
		this.cancion = cancion;
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
}
