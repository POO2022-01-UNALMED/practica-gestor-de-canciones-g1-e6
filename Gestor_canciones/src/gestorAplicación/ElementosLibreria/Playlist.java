package ElementosLibreria;
import java.util.ArrayList;
import java.io.*;
import Personas.Usuario;

public class Playlist {
	private String nombre;
	private ArrayList<Cancion> canciones;
	private int duracion;
	private int numero_canciones;
	private Usuario creador;
	private int id_playlist = 1;
	
	public Playlist(Usuario creador, String nombre) {
		this.nombre = nombre;
		canciones = new ArrayList<Cancion>();
		duracion = 0;
		numero_canciones = 0;
		this.creador = creador;
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
	//Cambié el tipo de retorno
	public String agg_cancion(Cancion cancion) {
        if(canciones.contains(cancion)) {
            return "La cancion ya se encuentra presnte en la playlist...";
        } else {
	        //Falta verificar si la canción existo o ya está
	        canciones.add(cancion);
	        numero_canciones++;
	        this.duracion += cancion.getDuracion(); 
	        return "La cancion fue agregada con exito...";
        }
	} 
	//Cambié el tipo de retorno
	public String elim_cancion(Cancion cancion) {
        if(canciones.contains(cancion)) {
    		//Falta verificar si la canción existo o ya está 
    		canciones.remove(cancion);
    		numero_canciones--;
    		this.duracion -= cancion.getDuracion();
            return "La cancion ha sido eliminada de la playlist exitosamente...";
        } else {
	        //Falta verificar si la canción existo o ya está
	        return "La cancion no se encontraba en la lista...";
        }
	}
	
	public Cancion repro_aleatoria() {
		int index = (int)(Math.random() * canciones.size());
		//Creo que falta poner bien el retorno
		return canciones.get(index);
	}
}
