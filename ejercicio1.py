'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: Versionado por Git 
Descripción: Suma de los primeros N números positivos.
'''
import os

def sumaPrimerosN():
    os.system("cls")
    print("➕ Suma de los primeros N números")

    while True:
        try:
            n = int(input("🔢 Ingrese un número entero positivo: "))
            if n > 0: # Verifica que el número sea positivo
                break # Si es positivo, salimos del bucle :)
            else:
                print("⚠️ Debe ser mayor que 0.")
        except ValueError:
            print("⚠️ Entrada inválida.")
    
    suma = 0
    for i in range(1, n + 1):
        suma += i
    
    print(f"🎯 La suma de los primeros {n} números es: {suma}")

if __name__ == "__main__":
    sumaPrimerosN()
