# Este programa calcula de cuántas formas diferentes se puede dar cambio con monedas y billetes de Nueva Zelanda

# Lista de todas las denominaciones de Nueva Zelanda en centavos
# $100 = 10000 centavos, $50 = 5000 centavos, etc.
billetes_y_monedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]

# Función para contar las formas de dar cambio
def contar_formas_de_cambio(cantidad_total_en_centavos):
    """
    Esta función cuenta de cuántas maneras se puede formar una cantidad de dinero
    utilizando los billetes y monedas de Nueva Zelanda.
    
    Parámetros:
    cantidad_total_en_centavos: La cantidad de dinero en centavos para la que queremos contar las formas
    
    Retorna:
    El número de formas diferentes de dar esa cantidad
    """
    tabla_de_formas = []
    
    for i in range(cantidad_total_en_centavos + 1):
        tabla_de_formas.append(0)
    
    tabla_de_formas[0] = 1
    
    for valor_de_billete_o_moneda in billetes_y_monedas:
        for cantidad_actual in range(valor_de_billete_o_moneda, cantidad_total_en_centavos + 1):
            resto = cantidad_actual - valor_de_billete_o_moneda
            formas_de_formar_el_resto = tabla_de_formas[resto]
            tabla_de_formas[cantidad_actual] += formas_de_formar_el_resto
    
    return tabla_de_formas[cantidad_total_en_centavos]

# Función principal del programa
def programa_principal():
    """
    Esta función maneja la entrada y salida del programa según los requisitos del problema.
    """
    print("\n=== Calculadora de Cambio en Dólares de Nueva Zelanda ===")
    print("Este programa calcula de cuántas formas diferentes se puede dar cambio.")
    print("Instrucciones:")
    print("- Ingrese cantidades de dinero en dólares (ejemplo: 0.05, 1.25, 2.50)")
    print("- Para terminar el programa, ingrese 0.00")
    print("-" * 60 + "\n")

    while True:
        try:
            linea_de_entrada = input("Ingrese una cantidad en dólares (o 0.00 para terminar): ")
            cantidad_en_dolares = float(linea_de_entrada)
            if cantidad_en_dolares == 0.00:
                print("\nPrograma terminado. ¡Gracias por usar la calculadora!")
                break
            
            cantidad_en_centavos = int(cantidad_en_dolares * 100)
            
            numero_de_formas = contar_formas_de_cambio(cantidad_en_centavos)
            
            salida_formateada = f"{cantidad_en_dolares:6.2f}{numero_de_formas:17d}"
            
            print(salida_formateada)
            
        except EOFError:
            break

if __name__ == "__main__":
    programa_principal()