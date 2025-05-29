'''
Autor: Jesy Nicole González Jarquín
Fecha: 29/05/2025
Versión: 1.0  
Descripción: Cuenta vocales en una cadena.
'''
import os

def contarVocales():
    os.system("cls")
    print("🔤 Contador de vocales")

    texto = input("📝 Ingrese una cadena de texto: ").lower()

    vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for letra in texto:
        if letra in vocales:
            vocales[letra] += 1

    for vocal, cantidad in vocales.items():
        print(f"🔡 Vocal '{vocal}': {cantidad} veces")

if __name__ == "__main__":
    contarVocales()

