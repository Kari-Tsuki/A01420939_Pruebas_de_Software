"""
wordCount.py

Programa para contar palabras distintas y su frecuencia."""

import sys
import time


def limpiar_palabra(palabra):
    """
    Limpia signos de puntuación básicos y convierte la palabra a minúsculas.

    :param palabra: la palabra original
    """
    limpia = ""

    for caracter in palabra:
        if caracter.isalnum():
            limpia += caracter.lower()
    return limpia


def contar_palabras(palabras):
    """
    Cuenta cuántas veces aparece cada palabra de la lista

    :param palabras: lista de palabras limpias
    """
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


def main():
    """Función principal del programa"""
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Uso correcto: python wordCount.py archivo.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    palabras = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for _, line in enumerate(file, start=1):
                line = line.strip()
                if line:
                    for palabra in line.split():
                        limpia = limpiar_palabra(palabra)
                        if limpia:
                            palabras.append(limpia)

    except FileNotFoundError:
        print(f"Error: el archivo '{file_name}' no existe.")
        sys.exit(1)

    frecuencia = contar_palabras(palabras)

    resultado = (
        "Resultados de conteo de palabras\n"
        "--------------------------------\n"
    )

    for palabra, cuenta in sorted(frecuencia.items()):
        resultado += f"{palabra}: {cuenta}\n"

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    resultado += f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos\n"

    print(resultado)

    result_path = "../results/WordCountResults.txt"
    try:
        with open(result_path, "w", encoding="utf-8") as file:
            file.write(resultado)
    except IOError:
        print("Error: no se pudo escribir el archivo de resultados.")

    return 0

if __name__ == "__main__":
    main()
