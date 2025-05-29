'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: 1.0  
Descripción: Encuentra el número mayor y menor entre N valores.
'''
import os

def mayorYMenor():
    os.system("cls")
    print("🔍 Buscar mayor y menor")

    while True:
        try:
            n = int(input("🔢 ¿Cuántos números va a ingresar?: "))
            if n > 0:
                break
            else:
                print("⚠️ Ingrese un número mayor a 0.")
        except ValueError:
            print("⚠️ Entrada inválida.")

    mayor = None
    menor = None

    for i in range(n):
        while True:
            try:
                num = float(input(f"📝 Ingrese número #{i+1}: "))
                if mayor is None or num > mayor:
                    mayor = num
                if menor is None or num < menor:
                    menor = num
                break
            except ValueError:
                print("⚠️ Número inválido.")

    print(f"📈 Mayor: {mayor}")
    print(f"📉 Menor: {menor}")

if __name__ == "__main__":
    mayorYMenor()

