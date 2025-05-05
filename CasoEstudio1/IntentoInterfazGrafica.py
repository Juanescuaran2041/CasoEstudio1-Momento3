__name__ = "Juan Esteban Cuaran Santander"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.cuaran@campusucc.edu.co" 

import tkinter as tk            #importo la libreria tkinter que sirve para crear interfaces graficas en python
from tkinter import messagebox  #Desde la libreria tkinter importo la messagebox que es lo que se muestra cada de presiono un boton
from Curso import Curso

class InterfazCurso:
    def __init__(self, root):
        self.curso = Curso()
        self.curso.notas = [1.0, 2.0, 3.0, 5.0, 2.8, 5.0, 4.0, 4.2, 3.5, 5.0, 1.5, 3.0]

        root.title("Gestión de Notas - Curso")

        titulo = tk.Label(root, text="MENÚ DE FUNCIONALIDAD", font=("Arial", 18, "bold"))
        titulo.pack(pady=12) ##Definir el tamaño de la ventana de visualizacion

        # Lista de botones
        botones = [
            ("Mostrar Notas", self.mostrar_notas),
            ("Reemplazar Notas", self.reemplazar_notas),
            ("Encontrar Repetición de 5", self.encontrar_repeticion_5),
            ("Calcular Mínimo Notas >= 3", self.calcular_minimo_notas_3),
            ("Encontrar Primeras Notas", self.encontrar_primeras_notas),
            ("Cambiar Notas", self.cambiar_notas),
            ("Dar Menor Nota", self.dar_menor_nota),
            ("Rango con Más Notas", self.dar_rango_con_mas_notas),
            ("Calcular Mediana", self.calcular_mediana),
            ("Salir", root.quit)
        ]
        ##En los botones defino el comando de cada uno para que lo relacione con el metodo, de lo contrario, si presiono el boton sin el comando
        ##El programa no sabria como relacionar los metodos con los botones

        for texto, comando in botones:
            tk.Button(root, text=texto, width=40, command=comando).pack(pady=5) 
        #Text tiene el texto del boton, witdth determina el ancho del boton, comand copia el comando que definimos y pack le da un espacio visual

    def mostrar_notas(self):
        notas = "\n".join([str(n) for n in self.curso.notas]) #Convierto las notas a str para que se puedan mostrar, el print en este caso no funciona
        messagebox.showinfo("Notas", f"Notas actuales:\n{notas}") #Muestra una ventana que muestra una tupla con un texto y ejecuta el comando indicado

    def reemplazar_notas(self):
        notas_temporales = self.curso.RemplazarNotas()
        notas_str = "\n".join([str(n) for n in notas_temporales])
        messagebox.showinfo("Notas Reemplazadas", f"Notas:\n{notas_str}")

    def encontrar_repeticion_5(self):
        resultado = self.curso.EncontrarRepeticion5()
        messagebox.showinfo("Repetición de 5", resultado)

    def calcular_minimo_notas_3(self):
        resultado = self.curso.calcularMinimoNotas3()
        messagebox.showinfo("Mínimo >= 3", f"Resultado: {resultado}")

    def encontrar_primeras_notas(self):
        resultado = self.curso.EncontrarPrimerasNotas()
        messagebox.showinfo("Notas de 1.5 remplazadas a 2.5:", f"Notas remplazadas de 1.5 a 2.5: {resultado}")

    def cambiar_notas(self):
        notas_temporales = self.curso.cambiarNotas()
        notas_str = "\n".join([str(n) for n in notas_temporales])
        messagebox.showinfo("Notas Reemplazadas", f"Notas:\n{notas_str}")

    def dar_menor_nota(self):
        resultado = self.curso.darMenorNota()
        messagebox.showinfo("Menor Nota", f"La menor nota es: {resultado}")

    def dar_rango_con_mas_notas(self):
        resultado = self.curso.darRangoConMasNotas()
        messagebox.showinfo("Rango Más Frecuente", f"{resultado}")

    def calcular_mediana(self):
        resultado = self.curso.CalcularMediana()
        messagebox.showinfo("Mediana", f"La mediana es: {resultado}")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCurso(root)
    root.mainloop()