def generar_combinaciones_lotto(cantidad_numeros, conjunto_numeros):
    """
    Genera todas las posibles combinaciones de 6 números tomados de un conjunto de números.
    
    Args:
        cantidad_numeros (int): Cantidad de números en el conjunto original
        conjunto_numeros (list): Lista de números del conjunto original
        
    Returns:
        list: Lista de todas las combinaciones posibles de 6 números
    """
    combinaciones = []
    
    # Función recursiva para generar combinaciones usando backtracking
    def generar_recursivamente(indice_inicio, combinacion_actual):
        # Si ya tenemos 6 números en la combinación actual, la guardamos
        if len(combinacion_actual) == 6:
            combinaciones.append(combinacion_actual.copy())
            return
        
        # Probamos añadir cada número restante a la combinación actual
        for i in range(indice_inicio, cantidad_numeros):
            # Añadimos el número actual a la combinación
            combinacion_actual.append(conjunto_numeros[i])
            # Recursivamente continuamos formando la combinación
            generar_recursivamente(i + 1, combinacion_actual)
            # Retrocedemos (backtracking) quitando el último número para probar otra combinación
            combinacion_actual.pop()
    
    # Iniciamos el proceso de generación con una combinación vacía
    generar_recursivamente(0, [])
    
    # Las combinaciones ya deberían estar ordenadas lexicográficamente,
    # pero las ordenamos por seguridad
    combinaciones.sort()
    
    return combinaciones

def programa_principal():
    # Lista para almacenar los resultados de todos los casos de prueba
    resultados_casos = []
    
    # Procesamos casos de prueba hasta encontrar un 0
    while True:
        # Leemos una línea de entrada
        print("Ingrese los números (k seguido del conjunto S) o 0 para terminar:")
        linea_entrada = input().strip()
        
        # Convertimos la línea en una lista de enteros
        valores = list(map(int, linea_entrada.split()))
        
        # Extraemos el primer valor que representa k (cantidad de números)
        cantidad_numeros = valores[0]
        
        # Verificamos si es el fin de la entrada
        if cantidad_numeros == 0:
            print("Fin de la entrada detectado.")
            break
            
        # Extraemos el conjunto S (los k números)
        conjunto_numeros = valores[1:]
        
        print(f"Procesando conjunto: {conjunto_numeros}")
        
        # Generamos todas las combinaciones posibles
        combinaciones = generar_combinaciones_lotto(cantidad_numeros, conjunto_numeros)
        
        # Guardamos las combinaciones para este caso
        resultados_casos.append(combinaciones)
        
        print(f"Se generaron {len(combinaciones)} combinaciones.")
    
    # Imprimimos los resultados de todos los casos
    print("\nRESULTADOS:")
    for indice, combinaciones in enumerate(resultados_casos):
        print(f"Caso #{indice + 1}:")
        
        # Imprimimos cada combinación
        for combinacion in combinaciones:
            # Convertimos los números a strings y los unimos con espacios
            linea = " ".join(map(str, combinacion))
            print(linea)
        
        # Añadimos línea en blanco entre casos de prueba, excepto después del último
        if indice < len(resultados_casos) - 1:
            print()

# Punto de entrada del programa
if __name__ == "__main__":
    print("Programa para generar combinaciones del Lotto alemán")
    print("==================================================")
    print("Para cada caso de prueba, ingrese k seguido de k números en orden ascendente.")
    print("Ejemplo: '7 1 2 3 4 5 6 7' para k=7 y el conjunto S={1,2,3,4,5,6,7}")
    print("Ingrese 0 para terminar la entrada.\n")
    
    programa_principal()