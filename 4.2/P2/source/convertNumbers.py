"""
convertNumbers.py

Programa para realizar la conversión de números a su version binaria y
hexadecimal.
"""

import sys
import time


def convertir_binario(numero):
    """Convierte un número entero a binario usando complemento a 2 (32 bits)."""

    bits = 32

    if numero == 0:
        return "0"

    if numero < 0:
        numero = (2 ** bits) + numero

        resultado = ""
        for _ in range(bits):
            resultado = str(numero % 2) + resultado
            numero //= 2

        return resultado

    resultado = ""
    n = numero
    while n > 0:
        resultado = str(n % 2) + resultado
        n //= 2

    return resultado

def convertir_hexadecimal(numero):
    """Convierte un número entero a hexadecimal usando complemento a 2 (32 bits)."""

    bits = 32
    digitos = "0123456789ABCDEF"

    if numero == 0:
        return "0"

    if numero < 0:
        numero = (2 ** bits) + numero

        resultado = ""

        while numero > 0:
            residuo = numero % 16
            resultado = digitos[residuo] + resultado
            numero //= 16

        while len(resultado) < 8:
            resultado = "0" + resultado

        return resultado

    resultado = ""
    n = numero
    while n > 0:
        residuo = n % 16
        resultado = digitos[residuo] + resultado
        n //= 16

    return resultado


def main():
    """Función principal del programa."""
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Uso correcto: python convertNumbers.py archivo.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    resultados = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                valor = line.strip()

                if not valor:
                    continue

                try:
                    numero = int(valor)
                    binario = convertir_binario(numero)
                    hexadecimal = convertir_hexadecimal(numero)
                except ValueError:
                    print(
                        f"Advertencia: línea {line_number} "
                        f"no es un número entero válido ({valor})"
                    )
                    binario = "#VALUE!"
                    hexadecimal = "#VALUE!"

                resultados.append((valor, binario, hexadecimal))

    except FileNotFoundError:
        print(f"Error: el archivo '{file_name}' no existe.")
        sys.exit(1)

    resultado = (
        "Resultados de conversión\n"
        "------------------------\n"
    )

    for valor, binario, hexadecimal in resultados:
        resultado += (
            f"Número: {valor}\n"
            f"Binario: {binario}\n"
            f"Hexadecimal: {hexadecimal}\n"
            "--------------------------\n"
        )

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    resultado += f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos\n"

    print(resultado)

    result_path = "../results/ConvertionResults.txt"
    try:
        with open(result_path, "w", encoding="utf-8") as file:
            file.write(resultado)
    except IOError:
        print("Error: no se pudo escribir el archivo de resultados.")

    return 0

if __name__ == "__main__":
    main()
