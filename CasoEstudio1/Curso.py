import random
class Curso:
   
    TOTAL_EST = 12
   
    def __init__(self):
        self.notas = []
        self.LlenarNotas ()
        
    def LlenarNotas(self):
        for est_Cont in range(Curso.TOTAL_EST):
            self.notas.append(round(random.uniform(4.0, 5.0),1))
   
   
    def promedio (self):
        promedio = 0
        est = 0
        while est < self.TOTAL_EST:
            promedio += self.notas[est]
            est +=1
       
        return promedio/self.TOTAL_EST
   
    def promedioFor (self):
       
        for nota in self.notas:
            promedio +=nota
       
        return promedio/ self.TOTAL_EST
   
   
    def notaMasRecurrente (self):
        notaR:float = 0.0
        Cantidad = 0
       
        for i in range (len(self.TOTAL_EST)):
            notaBuscada = self.notas[i]
            contador = 0
            for j in range (len(self.TOTAL_EST)):
                if self.notas [j] == notaBuscada:
                    contador +=1
           
            if contador > Cantidad:
                notaR = notaBuscada
                Cantidad = contador
               
        return notaR
   

    __method__ = "CalcularMayorNota"
    __params__ = "none"
    __returns__ = "Null"
    __description__ = "Metodo que sirve para calcular la mayor nota"
    def CalcularMayorNota (self):
        notaMayor = 0
        for i in range (len(self.notas)):
            self.notas [i]
            if self.notas[i] > notaMayor:
                notaMayor = self.notas [i]
               
        return notaMayor
    
    def mostrar_notas(self):
        print(self.notas)
                   
    __method__ = "HacerCurva"
    __params__ = "none"
    __returns__ = "Null"
    __description__ = "Metodo que sirve para aumentar las notas de los estudiantes en 5 porciento sin sobrepasarse de 5"

    def HacerCurva(self):
        for i in range(len(self.notas)):
            nuevasNotas = round(self.notas[i] * 1.05, 1)  # Redondear a 1 decimal para facilitar la lectura de los datos
            if nuevasNotas > 5:
                nuevasNotas = 5
            self.notas[i] = nuevasNotas

    __method__ = "EncontrarPrimerasNotas"
    __params__ = "none"
    __returns__ = "Null"
    __description__ = "Metodo que sirve para encontrar las primeras notas iguales a 1.5 y sobreescribirlas como 2.5"

    def EncontrarPrimerasNotas(self):
        Repeticion = 0
        notas_copia = self.notas.copy()
        for i in range(len(self.notas)):
            if self.notas[i] == 1.5 and Repeticion < 3:
                self.notas[i] = 2.5
                Repeticion += 1
            print(f"Nota {i+1}: antes = {notas_copia[i]}, después = {self.notas[i]}")

    __method__ = "EncontrarRepeticion5"
    __params__ = "none"
    __returns__ = "Posicion del tercer 5"
    __description__ = "Metodo que sirve para encontrar la tercera vez que se repite la nota 5.0"

    def EncontrarRepeticion5 (self):
        Repeticion = 0
        for i in range (len(self.notas)):
            if self.notas [i] == 5.0: 
                Repeticion +=1
                if Repeticion == 3:
                    return f'El valor 5 aparece por tercera vez en la posicion {i+1} del arreglo'
           
        
        return -1

    __method__ = "RemplazarNotas"
    __params__ = "none"
    __returns__ = "Null"
    __description__ = "Metodo que sirve para sobreescribir las notas con 0.0 hasta que aparezca el primer 3"

    def RemplazarNotas(self):
        notas_copia = self.notas.copy() ##En esta parte hice una copia del atributo notas porque de lo contrario, los otros metodos se veian afectados con los nuevos valores
        contador = 0

        for i in range(len(notas_copia)):
            if notas_copia[i] > 3.0:
                contador += 1
            if contador == 1:
                notas_copia[i] = notas_copia[i] 
            while contador == 0:
                notas_copia[i] = 0.0
                break

            print(f"La nota {i+1} es {notas_copia[i]}")

    __method__ = "calcularMinimoNotas3"
    __params__ = "none"
    __returns__ = "Cantidad Minima notas"
    __description__ = "Metodo que sirve para saber la cantidad de notas minimas que se deben sumar para llegar a 30"

    def calcularMinimoNotas3 (self):
        suma = 0
        for i in range(len(self.notas)):
            suma +=self.notas [i]
            if suma > 30:
                return f'La cantidad minima de notas para lograr 30 es {i+1}'
        return -1

    __method__ = "cambiarNotas"
    __params__ = "none"
    __returns__ = "Null"
    __description__ = "Metodo que sirve para cambiar las notas"

    def cambiarNotas(self):
        notas_copia = self.notas.copy() 

        for i in range(len(notas_copia)):
            if notas_copia[i] > 4.0:
                notas_copia[i] -= 0.5 
            elif notas_copia[i] < 2.0:
                notas_copia[i] += 0.5  
            else:
                notas_copia[i] = notas_copia[i]

            print(f"La nota {i+1} es igual a {notas_copia[i]}")
    
    __method__ = "darMenorNota"
    __params__ = "none"
    __returns__ = "notaMenor"
    __description__ = "Metodo que sirve para saber cual es la menor nota digitada"

    def darMenorNota (self):
        notaMenor = self.notas[0]
        for i in range(1, len(self.notas)):
            if self.notas[i] < notaMenor:
                notaMenor = self.notas[i]

        return f'La menor nota digitada es {notaMenor}' 
    
    __method__ = "darRangoConMasNotas"
    __params__ = "none"
    __returns__ = "rangoConMasNotas"
    __description__ = "Metodo que sirve en que rango se encuentra la mayor cantidad de notas"

    def darRangoConMasNotas(self):

        contadorRango1 = contadorRango2 = contadorRango3 = 0

        for i in range (len(self.notas)):
            if self.notas [i]>0.0 and self.notas [i] < 2:
                contadorRango1+=1
            elif self.notas [i] >=2.0 and self.notas [i] <3.5:
                contadorRango2 +=1
            else:
                contadorRango3 +=1

            rangos =[contadorRango1, contadorRango2, contadorRango3]
            mayor = max(rangos)     #Recorre los 3 rangos y selecciona el mayor

        return f'El rango con la mayor cantidad de notas es el rango: {rangos.index(mayor) + 1}'
    
        ##Tambien se hubiera podido de la siguiente forma:
        # if contR1 >= contR2 and contR1 >= contR3:
        #     return f'El rango con la mayor cantidad de notas es el rango:1'
        # elif contR2 >= contR1 and contR2 >= contR3:
        #     return f'El rango con la mayor cantidad de notas es el rango:2'
        # else:
        #     return f'El rango con la mayor cantidad de notas es el rango:3'

        #No obstante, no es muy optima y por temas de buenas practicas se prefirio investigar el uso de index para evitar escribir mucho mas codigo 
          

        