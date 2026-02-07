"""
computeStatistics.py

Programa para calcular estadísticas descriptivas a partir de un archivo
de números.
"""

import sys
import time


def calcular_mediana(datos):
    """Calcular la mediana de los datos."""

    if not datos:
        return None

    n = len(datos)
    datos_ordenados = sorted(datos)
    medio = n // 2

    if n % 2 == 1:
        return datos_ordenados[medio]

    return (datos_ordenados[medio - 1] + datos_ordenados[medio]) / 2


def calcular_media(datos):
    """Calcular la media de los datos."""
    if not datos:
        return None
    suma = 0
    for num in datos:
        suma += num
    return suma / len(datos)


def calcular_moda(datos):
    """Calcular la moda de los datos."""
    if not datos:
        return None

    frecuencia = {}
    for num in datos:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    max_frecuencia = max(frecuencia.values())

    modas = [valor for valor, freq in frecuencia.items() if freq == max_frecuencia]
    if max_frecuencia == 1:
        return None

    return modas[0]


def calcular_varianza(datos, media):
    """Calcular la varianza poblacional de los datos"""
    if not datos:
        return None

    suma_cuadrados = 0
    for num in datos:
        diferencia = num - media
        suma_cuadrados += diferencia ** 2

    return suma_cuadrados / len(datos)


def calcular_desviacion(varianza):
    """Calcular la desviación estándar de los datos."""
    if varianza is None:
        return None

    return varianza ** 0.5


def main():
    """Función principal del programa."""
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Uso correcto: python computeStatistics.py archivo.txt")
        sys.exit(1)

    file_name = sys.argv[1]

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            numbers = []

            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if line:
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print(f"Advertencia: línea {line_number} no es un número válido. ({line})")

    except FileNotFoundError:
        print(f"Error: el archivo '{file_name}' no existe.")
        sys.exit(1)

    print("Datos leídos correctamente:")
    print(numbers)
    mediana = calcular_mediana(numbers)
    media = calcular_media(numbers)
    moda = calcular_moda(numbers)
    varianza = calcular_varianza(numbers, media)
    desviacion = calcular_desviacion(varianza)

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    resultado = (
        "Resultados de estadisticas descriptivas\n"
        "---------------------------------------\n"
        f"Media: {media}\n"
        f"Mediana: {mediana}\n"
        f"Moda: {moda}\n"
        f"Varianza Poblacional: {varianza}\n"
        f"Desviación Estandar: {desviacion}\n"
        f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos\n"
    )
    print(resultado)
    result_path = "../results/StatisticsResult.txt"
    try:
        with open(result_path, "w", encoding="utf-8") as file:
            file.write(resultado)
    except IOError:
        print("Error: no se pudo escribir el archivo de resultados.")

    return 0


if __name__ == "__main__":
    main()
