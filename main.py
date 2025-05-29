'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: 1.0  
Descripción: Este es el menú de los ejercicios de la tarea. Puede revisar los módulos 
de cada ejercicio para ver su funcionamiento o llamarlos desde aquí.
'''

from ejercicio1 import sumaPrimerosN
from ejercicio2 import productoPrimerosPares
from ejercicio3 import contarVocales
from ejercicio4 import promedioCalificaciones
from ejercicio5 import calcularFactorial
from ejercicio6 import sumaParesImpares
from ejercicio7 import mayorYMenor
import os
from time import sleep

def main():
    menu = {
        "1": "Suma de los primeros N números",
        "2": "Producto de los primeros M números pares",
        "3": "Contar vocales en una cadena",
        "4": "Promedio de N calificaciones",
        "5": "Factorial de un número",
        "6": "Suma de números pares e impares",
        "7": "Encontrar el mayor y menor de N números",
        "0": "Salir"
    }

    while True:
        os.system("cls")
        print("📋 Menú de Ejercicios")
        print("-----------------------")

        for key, value in menu.items():
            print(f"{key}. {value}")

        try:
            opcion = input("🔢 Seleccione una opción:\n(Puede visualizar la respuesta por 5 segundos.) ")
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingrese un número.")
            continue

        if opcion == "1":
            sumaPrimerosN()
            sleep(5)
        elif opcion == "2":
            productoPrimerosPares()
            sleep(5)
        elif opcion == "3":
            contarVocales()
            sleep(5)
        elif opcion == "4":
            promedioCalificaciones()
            sleep(5)
        elif opcion == "5":
            calcularFactorial()
            sleep(5)
        elif opcion == "6":
            sumaParesImpares()
            sleep(5)
        elif opcion == "7":
            mayorYMenor()
            sleep(5)
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
