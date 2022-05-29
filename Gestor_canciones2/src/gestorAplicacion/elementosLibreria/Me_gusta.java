package gestorAplicacion.elementosLibreria;

import java.util.ArrayList;
import java.io.Serializable;
import gestorAplicacion.personas.Usuario;

public class Me_gusta extends Playlist{
	private final String nombre="Me gusta";
	private static final long serialVersionUID = 1L;
	private static ArrayList<Me_gusta> me_gustas;
	static {
		me_gustas = new ArrayList<Me_gusta>();
	}
	
	public static ArrayList<Me_gusta> getMe_gustas() {
		return me_gustas;
	}
	public static void setMe_gustas(ArrayList<Me_gusta> me_gustas) {
		Me_gusta.me_gustas = me_gustas;
	}
	public Me_gusta(Usuario creador){
		super(creador, "Me gusta");
		me_gustas.add(this);
		//Set del id ya que queremos que sea la uno
	}
	public String creadorPlaylist() {
		  return"Esta playlist fue creada por defecto"+"\n"+"Spotifoy todos los derechos reservados";	
		}
	public String toString() {
		return"La playlist Me gusta es creada por Spotifoy al crear el usuario"+"\n"+ "y tiene el id "+getId_real();
	}	
	public void unlike(Cancion cancion) {
		boolean presente=false;
    	for (Cancion c: this.getCanciones()) {
    		if (cancion==c){
    			presente=true; 
    		}
    	}
    	if (presente==true) {
    		this.getCanciones().remove(cancion);
    	}
	}
}