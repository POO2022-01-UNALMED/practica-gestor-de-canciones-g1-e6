package ElementosLibreria;
import java.util.ArrayList;
import Personas.Usuario;

public class Biblioteca {
    private Usuario usuario;
    private Cancion cancion_actual;
    private String estado_cancion;

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

    public Biblioteca( Usuario usuario){
        this.usuario = usuario;
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
        return playlist; //aquí hay que hacer lo de manejo de exepciones 
    }

}
