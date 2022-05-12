package ElementosLibreria;

import java.util.ArrayList;
import java.io.Serializable;
import Personas.Usuario;

public class Biblioteca  implements Serializable {
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Biblioteca> bibliotecas;
	static {
		bibliotecas = new ArrayList<Biblioteca>();
	}
	
	public Biblioteca( Usuario usuario){
        this.usuario = usuario;
        bibliotecas.add(this);
    }
	
    private Usuario usuario;
    private Cancion cancion_actual;
    private String estado_cancion;

    
    public static ArrayList<Biblioteca> getBibliotecas() {
		return bibliotecas;
	}
	public static void setBibliotecas(ArrayList<Biblioteca> bibliotecas) {
		Biblioteca.bibliotecas = bibliotecas;
	}
	
	public Usuario getUsuario() {
        return usuario;
    }
    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }
    public Cancion getCancion_actual() {
        return cancion_actual;
    }
    public void setCancion_actual(Cancion cancion_actual) {
        this.cancion_actual = cancion_actual;
    }
    public String getEstado_cancion() {
        return estado_cancion;
    }
    public void setEstado_cancion(String estado_cancion) {
        this.estado_cancion = estado_cancion;
    }

    

    public Mis_artistas acceder_misartistas(){
        return this.usuario.getMis_artistas();
    }

    public Playlist acceder_playlist(Playlist playlist){
        for(Playlist c: this.usuario.getPlaylists()) {
            if(c.equals(playlist)){
                return playlist;
            }
        }
        return playlist; //aquÃ­ hay que hacer lo de manejo de exepciones 
    }
    
    //Funcionalidad reproducción aleatoria
	public String repro_aleatoria(Playlist playlist) {
	    if(this.usuario.getPlaylists().contains(playlist)) {
			int index = (int)(Math.random() * playlist.getCanciones().size());
			//Creo que falta poner bien el retorno
			return playlist.getCanciones().get(index).getNombre();
	    } else {
	        return "La playlist"+playlist.getNombre()+"no existe en el usuario "+this.usuario.getNombre();
	    }
	}
	
    //FUNCIONALIDAD RECOMENDAR CANCIONES
    public Cancion recomendar_cancion() {
    	int rock=0;
    	int reggaeton=0;
    	int salsa=0;
    	int rap=0;
    	int pelar_pollos=0;
    	int tusar_calvos=0;
    	//aqui se cuentan cuantas canciones de cada genero existen
    	for(Cancion c: usuario.getMis_me_gusta().getCanciones()) {
    		switch(c.getGenero()) {
    		  case ROCK: rock++; 
    		  case REGGAETON: reggaeton++; 
    		  case SALSA: salsa++; 
    		  case RAP: rap++; 
    		  case MUSICA_PARA_PELAR_POLLOS: pelar_pollos++;
    		  case MUSICA_PARA_TUSAR_CALVOS: tusar_calvos++; 
    		}	
    	} 
    	//aqui se verifica cual es el genero con mas canciones, como son if simples deberia leer cada uno (debería)
    	//el problema sería un caso en que 2 generos tengan el mismo # de canciones, ahi recomendaría la primera en el if
    	int mayor=rock;
    	Genero mayorGen=Genero.ROCK;
    	if (reggaeton>mayor) {
    		mayor=reggaeton;
    		mayorGen=Genero.REGGAETON;
    	}
    	if (salsa>mayor) {
    		mayor=salsa;
    		mayorGen=Genero.SALSA;
    	}
    	if (rap>mayor) {
    		mayor=rap;
    		mayorGen=Genero.RAP;
    	}
    	if (pelar_pollos>mayor) {
    		mayor=pelar_pollos;
    		mayorGen=Genero.MUSICA_PARA_PELAR_POLLOS;
    	}
    	if (tusar_calvos>mayor) {
    		mayor=tusar_calvos;
    		mayorGen=Genero.MUSICA_PARA_TUSAR_CALVOS;
    	}
    	//en este for se recorre la lista de las canciones creadas, y la primera que sea del genero mayor y no este en me gusta, se recomendará
    	Cancion recomendacion= new Cancion();
    	for(Cancion c: Cancion.getCancionesCreadas()) {
    		if (c.getGenero()==mayorGen) {
    			if (usuario.getMis_me_gusta().getCanciones().contains(c)) {
    				continue;
    			}
    			else {
    				recomendacion=c;
    				break;
    			}
    		}
    		else {
    			continue;
    		}
    	}
    	return(recomendacion);
    }

}
