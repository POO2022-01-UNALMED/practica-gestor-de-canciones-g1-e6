package ElementosLibreria;

import java.util.ArrayList;
import java.io.Serializable;
import Personas.Usuario;

public class Me_gusta extends Playlist{
	
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
	//Cómo hago para que no se puedan crear más objetos de esta clase? servirá el final?
	public Me_gusta(Usuario creador){
		super(creador, "Me gusta");
		me_gustas.add(this);
		//Set del id ya que queremos que sea la uno
	}
	//Falta hacer esto
	public void unlike(Cancion cancion) {
		
	}
}