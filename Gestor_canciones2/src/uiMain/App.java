package uiMain;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.elementosLibreria.*;
import gestorAplicacion.personas.*;

public class App {
	static Scanner sc = new Scanner(System.in);
	//Se crean metodos para utilizar el Scanner de Java.
	static int readInt() {
		return sc.nextInt();
	}

	static String readString() {
		return sc.nextLine();
	}

	static double readDouble() {
		return sc.nextDouble();
	}
	public static void main(String[] args) {
		Deserializador.deserializarTodo();
		System.out.println("\n                               ===¡Saludos!===\n");
		System.out.println("  ********  *******    *******   ********** **  ********   *******     **    **");
		System.out.println("  **//////  /**////**  **/////** /////**/// /** /**/////   **/////**  //**  **");
		System.out.println(" /**        /**   /** **     //**    /**    /** /**       **     //**  //****");
		System.out.println(" /********* /******* /**      /**    /**    /** /******* /**      /**   //** ");
		System.out.println(" ////////** /**////  /**      /**    /**    /** /**////  /**      /**    /** ");
		System.out.println("        /** /**      //**     **     /**    /** /**      //**     **     /**  ");
		System.out.println("  ********  /**       //*******      /**    /** /**       //*******      /** ");
		System.out.println(" ////////   //         ///////       //     //  //         ///////       // \n");
		                                                         	                                    
		int opcion;
		do {
			System.out.println("Que accion desea realizar?\n");
			System.out.println(" 1. Crear usuario");
			System.out.println(" 2. Recomendar cancion a un usuario");
			System.out.println(" 3. Desplegar Biblioteca de un usuario"); //falta
			System.out.println(" 4. Mostrar todas las canciones existentes");
			System.out.println(" 5. Mostrar usuarios/artistas existentes");
			System.out.println(" 6. Guardar y cerrar\n");
			
			System.out.println("Elija una opcion: ");
			opcion = (int) readInt();

			switch (opcion) {

			case 1:
				System.out.println("-----------------------------------------");
				creacionUsuario();
				break;
			case 2:
				System.out.println("-----------------------------------------");
				recomendacion();
				break;
			case 3:
				System.out.println("-----------------------------------------");
				
				//PedirNombre();
				//LA IDEA ES QUE SOLICITE NOMBRE DE USUARIO Y LUEGO PUEDA DESPLEGAR TODAS LAS PLAYLIST QUE TIENE AÃ‘ADIDAS, SE DEBERA INCLUIR OPCION DE AGG O ELIM CANCION DE UNA PLAYLIST, crear playlist Y TAMBIEN REPRODUCIR POR NOMBRE O ALEATORIO.
				//ESTE MENU TAMBIEN DEBE TENER LAS OPCIONES:
				//1. Mostrar duraciÃ³n total de todas las canciones en una playlist.
				//2. Indicar si una canciÃ³n se repite en varias playlists. (en este podriamos aplicar ligadura dinamica, creando un apuntador tipo playlist pero que se le puede asignar a un me gusta o favoritos)
				//3. Generar una playlist con canciones en me gusta de un artista en especifico.
				biblio();
				break;
			case 4:
				System.out.println("-----------------------------------------");
				for (Cancion cancion : Cancion.getCancionesCreadas()) {
					System.out.println(cancion.getNombre());
				}
				break;
			case 5:
				System.out.println("-----------------------------------------");
				System.out.println("los usuarios creados son los siguientes:\n");
				for (Usuario usuario : Usuario.getUsuarios()) {
					System.out.println(usuario.datosPersona());
					System.out.println();
				}
				System.out.println("-----------------------------------------");
				System.out.println("los artistas creados son los siguientes:\n");
				for (Artista artista : Artista.getArtistas()) {
					System.out.println(artista.datosPersona());
					System.out.println();
				}
				System.out.println("-----------------------------------------");
				break;
			case 6:
				guardar();
				System.out.println("Vuelve pronto");
			}
			if (opcion != 6) {
				System.out.println();
				System.out.println("\nPresione Enter para continuar");
				try {
					System.in.read();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		} while (opcion != 6);

	}
	
	static void creacionUsuario() {
		System.out.println("Ingrese nombre del nuevo usuario:");
		readString();
		String nombre= readString();
		for (Usuario usuario: Usuario.getUsuarios()) {
			if (nombre.equals(usuario.getNombre())){
				System.out.println("Usuario ya creado");
				return;
			}
		}
		new Usuario(nombre);
		System.out.println("Usuario "+nombre+" creado exitosamente");
	}
	
	static void recomendacion() {
		System.out.println("Ingrese nombre del usuario a recomendar:");
		readString();
		String nombre= readString();
		for (Usuario usuario: Usuario.getUsuarios()) {
			if (nombre.equals(usuario.getNombre())){
				Cancion recomendacion=usuario.getMi_biblioteca().recomendar_cancion();
				System.out.println("Se recomienda la cancion: "+recomendacion.getNombre());
				return;
			}
		}
		System.out.println("el usuario ingresado no existe");
	}
	
	static void biblio() {
		int opcion2;
		System.out.println("Ingrese nombre del usuario que quiere ver su biblioteca:");
		readString();
		String nombreb= readString();
		for (Usuario usuario: Usuario.getUsuarios()) {
			if (nombreb.equals(usuario.getNombre())){
				do {
					System.out.println("Bienvenido "+usuario.getNombre()+", estas en la biblioteca.\n¿Qué deseas hacer?\n");
					System.out.println(" 1. Mostrar todas las playlists");
					System.out.println(" 2. Agregar una cancion a una playlist");
					System.out.println(" 3. Eliminar una cancion de una playlist");
					System.out.println(" 4. Reproducir una cancion aleatoria de una playlist");
					System.out.println(" 5. Reproducir una cancion de todas las playlists");
					System.out.println(" 6. Ver la duración de una playlist");
					System.out.println(" 7. Ver si una cancion se repite en varias playlists");
					System.out.println(" 8. Crear una playlist");
					System.out.println(" 9. Generar una playlist con canciones en me gusta de un artista en especifico");
					System.out.println(" 10. Salir de la biblioteca");

					opcion2 = (int) readInt();

					switch (opcion2) {
						case 1:
							System.out.println("-----------------------------------------");
							for (Playlist playlist : usuario.getPlaylists()) {
								System.out.println(playlist.getNombre());
							}
							break;
						case 2:
							System.out.println("-----------------------------------------");
							agregarCancionP(usuario);
							break;
						case 3:
							break;
						case 4:
							break;
						case 5:
							break;
						case 6:
							break;
						case 7:
							break;
						case 8:
							System.out.println("-----------------------------------------\nRecuerda que las playlists deben tener nombres diferentes");
							crearplaylist(usuario);
							break;
						case 9:
							break;
						}
				} while (opcion2 != 10);
				System.out.println();
				return;
				}
			}
			System.out.println("el usuario ingresado no existe");
		}
	
	static void agregarCancionP(Usuario usuario) {
		System.out.println("Ingrese nombre de la playlist en la que desea agregar la cancion:");
		readString();
		String nombrep= readString();
		for (Playlist playlist: usuario.getPlaylists()) {
			if (nombrep.equals(playlist.getNombre())){
				System.out.println("Ingrese nombre de la cancion que desea agregar a las playlist:");
				readString();
				String nombrecp= readString();
				for (Cancion cancion: Cancion.getCancionesCreadas()) {
					System.out.println("s");
					if (nombrecp.equals(cancion.getNombre())){
						playlist.agg_cancion(cancion);
						System.out.println("La cancion "+cancion.getNombre()+" se agrego con exito en "+playlist.getNombre());
						return;
					}
				}
				System.out.println("La cancion ingresada no existe");
				return;
			}
			
		}
		System.out.println("La playlist ingresada no existe");
	}
	
	static void crearplaylist(Usuario usuario) {
		System.out.println("Ingrese nombre de la nueva playlist a crear:");
		readString();
		String nombrenp= readString();
		for (Playlist playlist: usuario.getPlaylists()) {
			if (nombrenp.equals(playlist.getNombre())){
				System.out.println("Ya existe una playlist con el nombre "+playlist.getNombre());
				return;
			}
		}
		new Playlist(usuario, nombrenp);
		System.out.println("La playlist ha sido creada exitosamente");
		return;
	}
		
    public static void guardar() {
	    Serializador.serializarTodo();
    }

}
