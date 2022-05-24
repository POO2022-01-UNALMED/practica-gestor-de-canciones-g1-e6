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
		System.out.println("Buenos dias Administrador\n");
		System.out.println("los usuarios creados son los siguientes:");
		for (Usuario usuario : Usuario.getUsuarios()) {
			System.out.println(usuario.datosPersona());
		}
		for (Artista artista : Artista.getArtistas()) {
			System.out.println(artista.datosPersona());
		}
		int opcion;
		do {
			System.out.println("Que desea hacer?");
			System.out.println(" 1. Crear usuario");
			System.out.println(" 2. Agregar cancion a playlist");
			System.out.println(" 3. Recomendar cancion a un usuario");
			System.out.println(" 4. Reproducir canción aleatoria de una playlist");
			System.out.println(" 5. Mostrar duración total de todas las canciones en una playlist.");
			System.out.println(" 6. Indicar si una canción se repite en varias playlists.");
			System.out.println(" 7. Generar una playlist con canciones en me gusta de un artista en especifico.");
			System.out.println(" 8. Mostrar canciones existentes");
			System.out.println(" 9. Guardar y cerrar");
			
			System.out.println("Elija una opcion: ");
			opcion = (int) readInt();

			switch (opcion) {

			case 1:
				//menuCreacionUsuario();
				break;
			case 2:
				//menuAgregarCancion();
				break;
			case 3:
				//menuRecomendarCancion();
				break;
			case 4:
				//menuReproAleatoria();
				break;
			case 5:
				//menuDuracionPlaylist();
				break;
			case 6:
				//menuRepeticionCanciones();
			case 7:
				//MenuGeneracionPlaylist();
				break;
			case 8:
				for (Cancion cancion : Cancion.getCancionesCreadas()) {
					System.out.println(cancion.getNombre());
				}
				break;
			case 9:
				guardar();
				System.out.println("Vuelve pronto");
			}
			if (opcion != 9) {
				System.out.println("\nPresione Enter para continuar");
				try {
					System.in.read();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		} while (opcion != 9);

	}
    public static void guardar() {
	    Serializador.serializarTodo();
    }

}
