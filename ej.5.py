'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: 1.0  
Descripción: Calcula el factorial de un número.
'''
import os

def calcularFactorial():
    os.system("cls")
    print("🧪 Cálculo de factorial")

    while True:
        try:
            num = int(input("🔢 Ingrese un número entero positivo: "))
            if num >= 0:
                break
            else:
                print("⚠️ No puede ser negativo.")
        except ValueError:
            print("⚠️ Entrada inválida.")
    
    factorial = 1
    contador = 1
    while contador <= num:
        factorial *= contador
        contador += 1

    print(f"🎯 {num}! = {factorial}")

if __name__ == "__main__":
    calcularFactorial()


