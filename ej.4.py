'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: 1.0  
Descripción: Calcula el promedio de N calificaciones.
'''
import os

def promedioCalificaciones():
    os.system("cls")
    print("📚 Promedio de calificaciones")

    while True:
        try:
            n = int(input("🔢 ¿Cuántas calificaciones va a ingresar?: "))
            if n > 0:
                break
            else:
                print("⚠️ Número debe ser positivo.")
        except ValueError:
            print("⚠️ Entrada inválida.")
    
    suma = 0
    for i in range(1, n + 1):
        while True:
            try:
                calificacion = float(input(f"📝 Ingrese calificación #{i}: "))
                suma += calificacion
                break
            except ValueError:
                print("⚠️ Calificación inválida.")
    
    promedio = suma / n
    print(f"📈 El promedio es: {promedio:.2f}")

if __name__ == "__main__":
    promedioCalificaciones()

