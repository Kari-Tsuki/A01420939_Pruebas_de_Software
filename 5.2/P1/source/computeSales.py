"""
computeSales.py

Este programa calcula el ingreso total de ventas de una empresa
a partir de un catálogo de precios (archivo JSON) y un registro
de ventas (archivo JSON).
"""


import sys
import json
import time
import os


def main():

    if len(sys.argv) != 3:
        print("Uso: python computeSales.py <archivo_catalogo_productos.json> <archivo_registro_ventas.json>")
        sys.exit(1)

    product_file = sys.argv[1]
    sales_file = sys.argv[2]

    if not os.path.isfile(product_file):
        print(f"Error: El archivo {product_file} no existe.")
        sys.exit(1)

    if not os.path.isfile(sales_file):
        print(f"Error: El archivo {sales_file} no existe.")
        sys.exit(1)

    try:
        with open(product_file, "r", encoding="utf-8") as f:
            product_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: El archivo {product_file} no tiene un formato JSON válido.")
        sys.exit(1)

    try:
        with open(sales_file, "r", encoding="utf-8") as f:
            sales_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: El archivo {sales_file} no tiene un formato JSON válido.")
        sys.exit(1)

    print(f"{len(product_data)} productos cargados desde {product_file}")
    print(f"{len(sales_data)} registros de ventas cargados desde {sales_file}")

if __name__ == "__main__":
    main()