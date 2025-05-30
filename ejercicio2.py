'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: 1.0  
Descripción: Producto de los primeros M números pares.
'''
import os

def productoPrimerosPares():
    os.system("cls")
    print("✖️ Producto de los primeros M números pares")

    while True:
        try:
            m = int(input("🔢 Ingrese un número entero positivo: "))
            if m > 0:
                break
            else:
                print("⚠️ Debe ser mayor que 0.")
        except ValueError:
            print("⚠️ Entrada inválida.")
    
    producto = 1
    contador = 0
    num = 2

    # Aquí iniciamos el producto de los primeros M números pares
    # el primer número par es 2, luego 4, 6, etc.
    # usamos un bucle while para multiplicar los números pares
    # por ejemplo, si m es 3, multiplicamos 2 * 4 * 6 = 48
    while contador < m:
        producto *= num
        num += 2
        contador += 1

    print(f"🧮 El producto de los primeros {m} pares es: {producto}")

if __name__ == "__main__":
    productoPrimerosPares()
