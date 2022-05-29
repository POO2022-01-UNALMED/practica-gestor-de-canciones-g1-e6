package gestorAplicacion.elementosLibreria;

import java.io.Serializable;
import java.util.ArrayList;
import java.io.*;
import gestorAplicacion.personas.Usuario;

public class Playlist  implements Serializable {
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Playlist> playlists;
	static {
		playlists = new ArrayList<Playlist>();
	}
	
	private String nombre;
	private ArrayList<Cancion> canciones;
	private int duracion;
	private int numero_canciones;
	private Usuario creador;
	private static int id_playlist = 1;
	private int id_real;
	
	public Playlist(Usuario creador, String nombre) {
		this.nombre = nombre;
		canciones = new ArrayList<Cancion>();
		duracion = 0;
		numero_canciones = 0;
		this.creador = creador;
		id_real = id_playlist;
		id_playlist++;
		playlists.add(this);
		creador.agg_Playlist(this);
	}

	//gets y sets de cada atributo
	
	public String getNombre() {
		return nombre;
	}

	public static ArrayList<Playlist> getPlaylists() {
		return playlists;
	}

	public static void setPlaylists(ArrayList<Playlist> playlists) {
		Playlist.playlists = playlists;
	}

	public int getId_real() {
		return id_real;
	}

	public void setId_real(int id_real) {
		this.id_real = id_real;
	}

	public void setDuracion(int duracion) {
		this.duracion = duracion;
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
		this.id_real = id_playlist;
	}
	public String creadorPlaylist() {
	  return"Esta playlist fue creada por "+this.creador.getNombre()+"\n"+"Spotifoy todos los derechos reservados";	
	}
	public String toString() {
		return"La playlist de nombre "+nombre+"\n"+ "fue creada por: "+creador.getNombre()+"\n"+"y tiene el id "+id_real;
	}
	//Mï¿½todos adicionales
	
	//Cambiï¿½ el tipo de retorno
	public String agg_cancion(Cancion cancion) {
        if(canciones.contains(cancion)) {
            return "La cancion ya se encuentra presente en la playlist...";
        } else {
	        //Falta verificar si la canciï¿½n existo o ya estï¿½
	        canciones.add(cancion);
	        numero_canciones++;
	        this.duracion += cancion.getDuracion(); 
	        return "La cancion fue agregada con exito...";
        }
	}
	//Cambiï¿½ el tipo de retorno
	public String elim_cancion(Cancion cancion) {
        if(canciones.contains(cancion)) {
    		//Falta verificar si la canciï¿½n existo o ya estï¿½ 
    		canciones.remove(cancion);
    		numero_canciones--;
    		this.duracion -= cancion.getDuracion();
            return "La cancion ha sido eliminada de la playlist exitosamente...";
        } else {
	        //Falta verificar si la canciï¿½n existo o ya estï¿½
	        return "La cancion no se encontraba en la lista...";
        }
	}
	
}
