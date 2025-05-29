'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: 1.0  
Descripción: Suma de pares e impares hasta que se ingrese 0.
'''
import os

def sumaParesImpares():
    os.system("cls")
    print("➕➖ Suma de pares e impares")

    sumaPares = 0
    sumaImpares = 0

    while True: #me gusta usar bucles para 
        #manejar las entradas porque es más flexible 
        #y evita tener que volver a correrlo si no pongo bien la entrada.
        try:
            num = int(input("🔢 Ingrese un número (0 para terminar): "))
            if num == 0:
                break
            if num % 2 == 0:
                sumaPares += num
            else:
                sumaImpares += num
        except ValueError:
            print("⚠️ Entrada inválida.")

    print(f" Suma de pares: {sumaPares}")
    print(f" Suma de impares: {sumaImpares}")

if __name__ == "__main__":
    sumaParesImpares()
