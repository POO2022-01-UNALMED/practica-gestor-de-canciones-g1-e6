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
		inicializar();
		System.out.println("\n===¡Saludos!===\n");
		                                                         	                                    
		int opcion;
		do {
			System.out.println(" _____             _   _  __            \r\n"
					+ "/  ___|           | | (_)/ _|           \r\n"
					+ "\\ `--. _ __   ___ | |_ _| |_ ___  _   _ \r\n"
					+ " `--. \\ '_ \\ / _ \\| __| |  _/ _ \\| | | |\r\n"
					+ "/\\__/ / |_) | (_) | |_| | || (_) | |_| |\r\n"
					+ "\\____/| .__/ \\___/ \\__|_|_| \\___/ \\__, |\r\n"
					+ "      | |                          __/ |\r\n"
					+ "      |_|                         |___/ ");
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
					int hor=cancion.getDuracion()/3600;
			        int min=(cancion.getDuracion()-(3600*hor))/60;
			        int seg=cancion.getDuracion()-((hor*3600)+(min*60));
					System.out.println(cancion.getNombre()+" - "+cancion.getArtista().getNombre()+" - "+hor+":"+min+":"+seg);
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
	static void inicializar() {
		Cancion.setCancionesCreadas((new ArrayList<Cancion>()));
		Usuario.setUsuarios((new ArrayList<Usuario>()));
		Artista.setArtistas((new ArrayList<Artista>()));
		Playlist.setPlaylists(new ArrayList<Playlist>());
		Usuario test9 = new Usuario("Carlos");
		Usuario test= new Usuario("Manuel");
		Usuario test1= new Usuario("PachoGOD");
		Artista test6=new Artista("El rompe traperas", "Baby brrr brrrr", Genero.REGGAETON);
		Artista test7=new Artista("bad chicken", "tssss", Genero.MUSICA_PARA_PELAR_POLLOS);
		Artista test8=new Artista("el motila abuelas", "yeah", Genero.MUSICA_PARA_TUSAR_CALVOS);
		Artista test12=new Artista("los gansos rosas", "you know where you are", Genero.ROCK);
		Artista test13=new Artista("Hector lavoe", "La calle es una selva de cemento", Genero.SALSA);
		Artista test14=new Artista("Resibalvin","si", Genero.RAP);
		Cancion test2=new Cancion("A lavar el patio", 180, test6, Genero.REGGAETON);
		Cancion test15=new Cancion("ba�os limpios y relucientes con salvo", 150, test6, Genero.REGGAETON);
		Cancion test10=new Cancion("guelkon turi yangol", 120, test12, Genero.ROCK);
		Cancion test16=new Cancion("La leyenda de la chucha y el culebrero", 250, test12, Genero.ROCK);
		Cancion test3=new Cancion("El patito Juan", 180, test7, Genero.MUSICA_PARA_PELAR_POLLOS);
		Cancion test5= new Cancion("A pelar pollos", 120, test6, Genero.MUSICA_PARA_PELAR_POLLOS);
		Cancion test17= new Cancion("La abuela esta de pelos", 75, test8, Genero.MUSICA_PARA_TUSAR_CALVOS);
		Cancion test4= new Cancion("Vamo a trapear", 120, test8, Genero.MUSICA_PARA_TUSAR_CALVOS);
		Cancion test18= new Cancion("Tiraera a marbelle", 546, test14, Genero.RAP);
		Cancion test19= new Cancion("La visita a bellavista", 134, test14, Genero.RAP);
		Cancion test20= new Cancion("El gran baron", 180, test13, Genero.SALSA);
		Cancion test21= new Cancion("Juanito alima�a", 180, test13, Genero.SALSA);
		
		
		
		Playlist test11= new Playlist(test1, "Mejores voces femeninas de todos los tiempos");
		Playlist test22= new Playlist(test, "Mejores canciones para pelar pollos en rionegro un domingo");
		Playlist test23= new Playlist(test9, "Aprende a motilar con esta musica para tusar calvos");
		test11.agg_cancion(test2);
		test11.agg_cancion(test10);
		test11.agg_cancion(test18);
		test22.agg_cancion(test10);
		test22.agg_cancion(test5);
		test23.agg_cancion(test2);
		test23.agg_cancion(test17);
		test23.agg_cancion(test18);
		test.agg_Playlist(test11);
		test.agg_Playlist(test23);
		test1.agg_Playlist(test22);
		test9.agg_Megusta(test2);
		test9.agg_Megusta(test3);
		test9.agg_Megusta(test4);
		test9.agg_Megusta(test10);
		test.agg_Megusta(test2);
		test.agg_Megusta(test17);
		test.agg_Megusta(test16);
		test.agg_Megusta(test15);
		test1.agg_Megusta(test2);
		test1.agg_Megusta(test19);
		test1.agg_Megusta(test21);
		test1.agg_Megusta(test10);
		test9.agg_MisFavoritos(test20);
		test9.agg_MisFavoritos(test2);
		test9.agg_MisFavoritos(test15);
		test9.agg_MisFavoritos(test17);
		test.agg_MisFavoritos(test21);
		test.agg_MisFavoritos(test18);
		test.agg_MisFavoritos(test3);
		test.agg_MisFavoritos(test16);
		test1.agg_MisFavoritos(test20);
		test1.agg_MisFavoritos(test2);
		test1.agg_MisFavoritos(test16);
		test1.agg_MisFavoritos(test3);
		test9.agg_Miartistas(test14);
		test9.agg_Miartistas(test12);
		test9.agg_Miartistas(test8);
		test.agg_Miartistas(test6);
		test.agg_Miartistas(test7);
		test.agg_Miartistas(test12);
		test1.agg_Miartistas(test6);
		test1.agg_Miartistas(test12);
		test1.agg_Miartistas(test14);
		
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
					System.out.println("______ _ _     _ _       _                 \r\n"
							+ "| ___ (_) |   | (_)     | |                \r\n"
							+ "| |_/ /_| |__ | |_  ___ | |_ ___  ___ __ _ \r\n"
							+ "| ___ \\ | '_ \\| | |/ _ \\| __/ _ \\/ __/ _` |\r\n"
							+ "| |_/ / | |_) | | | (_) | ||  __/ (_| (_| |\r\n"
							+ "\\____/|_|_.__/|_|_|\\___/ \\__\\___|\\___\\__,_|\r\n"
							+ "                                           \r\n"
							+ "                                           ");
					System.out.println("Bienvenido "+usuario.getNombre());
					System.out.println(" 1. Ver mis artistas");
					System.out.println(" 2. Agregar una cancion a una playlist");
					System.out.println(" 3. Eliminar una cancion de una playlist");
					System.out.println(" 4. Ver info general de playlists");
					System.out.println(" 5. Ver canciones con duracion de mis playlists");
					System.out.println(" 6. verificar quien creo una playlist");
					System.out.println(" 7. Reproducir una cancion aleatoria de una playlist");
					System.out.println(" 8. Reproducir una cancion de una playlist");
					System.out.println(" 9. Ver la duracion total de todas las playlists (incluido Me gusta y Favoritos)");
					System.out.println(" 10. Ver si una cancion se repite en varias playlists");
					System.out.println(" 11. Crear una playlist");
					System.out.println(" 12. Descubrir a mi artista favorito");
					System.out.println(" 13. Salir de la biblioteca");

					opcion2 = (int) readInt();

					switch (opcion2) {
						case 1:
							System.out.println("-----------------------------------------");
							for (Artista artista : usuario.getMis_artistas().getArtistas()) {
								System.out.println(artista.getNombre());
							}
							break;
						case 2:
							System.out.println("-----------------------------------------");
							agregarCancionP(usuario);
							break;
						case 3:
							System.out.println("-----------------------------------------");
							eliminarCancionP(usuario);
							break;
						case 4:
							System.out.println("-----------------------------------------");
							infoPlaylist(usuario);
							break;
						case 5:
							System.out.println("-----------------------------------------");
							for (Playlist playlist : usuario.getPlaylists()) {
								System.out.println("Nombre de la playlist: "+playlist.getNombre()+"\n");
								for (Cancion cancion : playlist.getCanciones()) {
									int hor=cancion.getDuracion()/3600;
							        int min=(cancion.getDuracion()-(3600*hor))/60;
							        int seg=cancion.getDuracion()-((hor*3600)+(min*60));
									System.out.println("-"+cancion.getNombre()+" - "+cancion.getArtista().getNombre()+" - "+hor+":"+min+":"+seg);
								}
								System.out.println();
							}
							break;
						case 6:
							System.out.println("-----------------------------------------");
							creador(usuario);
							break;
						case 7:
							System.out.println("-----------------------------------------");
							repPlayl(usuario);
							break;
						case 8:
							System.out.println("-----------------------------------------");
							playl(usuario);
							break;
						case 9:
							System.out.println("-----------------------------------------");
							duracion(usuario);
							break;
						case 10:
							System.out.println("-----------------------------------------");
							repite(usuario);
							break;
						case 11:
							System.out.println("-----------------------------------------\nRecuerda que las playlists deben tener nombres diferentes");
							crearplaylist(usuario);
							break;
						case 12:
							System.out.println("-----------------------------------------\nEnhorabuena!\nTu artista favorito es: "+usuario.artista_favorito());
							break;
						}
					if (opcion2 != 13) {
						System.out.println();
						System.out.println("\nPresione Enter para continuar");
						try {
							System.in.read();
						} catch (IOException e) {
							e.printStackTrace();
						}
					}
				} while (opcion2 != 13);
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
				String nombrecp= readString();
				for (Cancion cancion: Cancion.getCancionesCreadas()) {
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
	
	static void eliminarCancionP(Usuario usuario) {
		System.out.println("Ingrese nombre de la playlist en la que desea eliminar la cancion:");
		readString();
		String nombreep= readString();
		for (Playlist playlist: usuario.getPlaylists()) {
			if (nombreep.equals(playlist.getNombre())){
				System.out.println("Ingrese nombre de la cancion que desea eliminar en la playlist "+playlist.getNombre()+":");
				String nombreecp= readString();
				for (Cancion cancion: Cancion.getCancionesCreadas()) {
					if (nombreecp.equals(cancion.getNombre())){
						playlist.elim_cancion(cancion);
						System.out.println("La cancion "+cancion.getNombre()+" se elimino con exito en "+playlist.getNombre());
						return;
					}
				}
				System.out.println("La cancion ingresada no existe");
				return;
			}
			
		}
		System.out.println("La playlist ingresada no existe");
	}
	static void creador(Usuario usuario) {
		System.out.println("Ingrese nombre de la playlist"+"\n");
		Playlist p;
		readString();
		String nombrep= readString();
		for (Playlist playlist: usuario.getPlaylists()) {
			if (nombrep.equals(playlist.getNombre())){
				p=playlist;
				System.out.println(playlist.creadorPlaylist());
				return;
			}
		}
		System.out.println("Playlist "+nombrep+" no esta agregada o no existe.");
		return;
	}
	static void infoPlaylist(Usuario usuario) {
		for (Playlist playlist: usuario.getPlaylists()) {
			Playlist p=playlist;
			System.out.println(p);
		}
	}
	static void repPlayl(Usuario usuario) {
		System.out.println("Ingrese nombre de la playlist de la que desea reproducir una cancion aleatoria:");
		readString();
		String nombrer= readString();
		for (Playlist playlist: usuario.getPlaylists()) {
			if (nombrer.equals(playlist.getNombre())){
				System.out.println(usuario.getMi_biblioteca().repro_aleatoria(playlist));
				return;
			}
			
		}
		System.out.println("La playlist ingresada no existe");
	}
	
	static void playl(Usuario usuario) {
		System.out.println("Ingrese nombre de la playlist en la que desea reproducir una canción:");
		readString();
		String nombreep= readString();
		for (Playlist playlist: usuario.getPlaylists()) {
			if (nombreep.equals(playlist.getNombre())){
				System.out.println("Ingrese nombre de la cancion que desea reproducir de la playlist "+playlist.getNombre()+":");
				String nombreecp= readString();
				for (Cancion cancion: Cancion.getCancionesCreadas()) {
					if (nombreecp.equals(cancion.getNombre())){
						System.out.println(cancion.play());
						return;
					}
				}
				System.out.println("La cancion ingresada no existe");
				return;
			}
			
		}
		System.out.println("La playlist ingresada no existe");
	}
	
	static void duracion(Usuario usuario) {
        int hor=usuario.duracion_total()/3600;
        int min=(usuario.duracion_total()-(3600*hor))/60;
        int seg=usuario.duracion_total()-((hor*3600)+(min*60));
		System.out.println("La duracion total de todas las playlists es de: "+hor+" horas, "+min+" minutos y "+seg+" segundos");
		return;
	}
	
	static void repite(Usuario usuario) {
		System.out.println("Ingrese nombre de una de las playlists a comparar:");
		readString();
		String nombreep= readString();
		for (Playlist playlist: usuario.getPlaylists()) {
			if (nombreep.equals(playlist.getNombre())){
				System.out.println("Ingrese nombre de la segunda playlist a comparar con "+playlist.getNombre()+":");
				String nombreecp2= readString();
				if(nombreecp2=="") {
					System.out.println("Se compara por defecto con me gusta o con favoritos si la playlist ingresada es me gusta");
					System.out.println(usuario.cancionSeRepite(playlist));
					return;
				}
				for (Playlist playlist2: usuario.getPlaylists()) {
					if (nombreecp2.equals(playlist2.getNombre())){
						System.out.println(usuario.cancionSeRepite(playlist, playlist2));
						return;
					}
				}
				System.out.println("La playlist2 ingresada no existe");
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
