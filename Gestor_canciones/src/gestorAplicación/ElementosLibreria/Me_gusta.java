package ElementosLibreria;

import Personas.Usuario;

public class Me_gusta extends Playlist{
	//Cómo hago para que no se puedan crear más objetos de esta clase? servirá el final?
	public Me_gusta(Usuario creador){
		super(creador, "Me gusta");
		//Set del id ya que queremos que sea la uno
		setId_playlist(1);
	}
	//Falta hacer esto
	public void unlike(Cancion cancion) {
		
	}
}