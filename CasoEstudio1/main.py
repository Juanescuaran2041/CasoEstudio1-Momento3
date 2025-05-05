__name__ = "Juan Esteban Cuaran Santander"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.cuaran@campusucc.edu.co" 

from Curso import Curso

if __name__ == "__main__":
    curso = Curso()
    
    # Asignar notas para pruebas
    curso.notas = [1.0, 2.0, 3.0, 5.0, 2.8, 5.0, 4.0, 4.2, 3.5, 5.0, 1.5, 3.0]

    def mostrar_menu():
        print("+----------------------------+")
        print("|    MENÚ DE FUNCIONALIDAD   |")
        print("+----------------------------+")
        print("| 1. MostrarNotas            |")
        print("| 2. RemplazarNotas          |")
        print("| 3. EncontrarRepeticion5    |")
        print("| 4. CalcularMinimoNotas30   |")
        print("| 5. EncontrarPrimerasNotas  |")
        print("| 6. cambiarNotas            |")
        print("| 7. darMenorNota            |")
        print("| 8. darRangoconMasNota      |")
        print("| 9. CalcularMedianaNotas    |")
        print("| 10.Salir                   |")
        print("+----------------------------+")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Notas ingresadas:")
            curso.mostrar_notas()

        elif opcion == "2":
            print("\nHasta la primera nota mayor a 3 se remplazaran las anteriores con 0.0\n")
            resultado = curso.RemplazarNotas()
            curso.RemplazarNotas()
            print(f"\n{resultado}")

        elif opcion == "3":
            resultado = curso.EncontrarRepeticion5()
            print(f"\n{resultado}")

        elif opcion == "4":
            resultado = curso.calcularMinimoNotas3()
            print(f"\n{resultado}")

        elif opcion == "5":
            resultado = curso.EncontrarPrimerasNotas()
            curso.EncontrarPrimerasNotas()
            print(f"\n Primeras Notas 1.5 cambiadas a 2.5 {resultado}")
        
        elif opcion == "6":
            resultado = curso.cambiarNotas()
            curso.cambiarNotas()
            print(f"\n{resultado}")
            
        elif opcion == "7":
            resultado = curso.darMenorNota()
            print(f"\n{resultado}")

        elif opcion == "8":
            resultado = curso.darRangoConMasNotas()
            print(f"\n{resultado}")

        elif opcion == "9":
            resultado = curso.CalcularMediana()
            print(f"\n{resultado}")

        elif opcion == "10":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

    ##A manera de aclaracion, si bien con el comando random se general numeros al azar, a veces no podra generar 3 veces el 5 por ejemplo
    ## por ende, no se podria probar el metodo de encontrarRepetecion5, debido a esto, se opto por asignarlas manualmente

    


