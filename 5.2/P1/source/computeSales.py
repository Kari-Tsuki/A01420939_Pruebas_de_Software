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


def main():  # pylint: disable=too-many-locals, too-many-statements
    """Función principal del programa    """

    start_time = time.time()
    if len(sys.argv) != 3:
        print(
            "Uso: python computeSales.py "
            "<archivo_catalogo_productos.json> "
            "<archivo_registro_ventas.json>"
        )
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
        print(
            f"Error: El archivo {product_file}"
            "no tiene un formato JSON válido."
            )
        sys.exit(1)

    try:
        with open(sales_file, "r", encoding="utf-8") as f:
            sales_data = json.load(f)
    except json.JSONDecodeError:
        print(
            f"Error: El archivo {sales_file}"
            "no tiene un formato JSON válido."
            )
        sys.exit(1)

    print(f"{len(product_data)} productos cargados desde {product_file}")
    print(f"{len(sales_data)} registros de ventas cargados desde {sales_file}")

    price_dict = {item["title"]: item["price"] for item in product_data}
    total_sales = 0
    errors = []

    for sale in sales_data:
        product_name = sale.get("Product")
        quantity = sale.get("Quantity", 0)
        if product_name not in price_dict:
            errors.append(f"Producto desconocido, {product_name}")
            continue
        total_sales += price_dict[product_name] * quantity
    print("\n--- Resultados de ventas ---")
    print(f"Total de ventas: ${total_sales:.2f}")

    if errors:
        print("\nErrores encontrados:")
        for e in errors:
            print(f"- {e}")

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time

    result_file = "../results/SalesResults.txt"
    with open(result_file, "w", encoding="utf8") as f:
        f.write("--- Resultado de Ventas --- \n")

        f.write(f"Total de ventas: ${total_sales}")
        if errors:
            f.write("Errores encontrados:\n")
            for e in errors:
                f.write(f"- {e}\n")

        f.write(f"\nTiempo de ejecución: {tiempo_ejecucion:.2f} segundos\n")


if __name__ == "__main__":
    main()
