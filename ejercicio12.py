import sys
sys.setrecursionlimit(10000)

def resolver_juego_clavo(longitud, a_min, a_max, b_min, b_max):
    memoria = {}
    
    def puede_ganar(longitud_restante, es_jugador_a):
        if longitud_restante <= 0:
            return False
        if (longitud_restante, es_jugador_a) in memoria:
            return memoria[(longitud_restante, es_jugador_a)]
        
        minimo_actual = a_min if es_jugador_a else b_min
        maximo_actual = a_max if es_jugador_a else b_max
        
        if longitud_restante <= minimo_actual:
            memoria[(longitud_restante, es_jugador_a)] = True
            return True
        
        for golpe in range(minimo_actual, min(maximo_actual, longitud_restante) + 1):
            nuevo_largo = longitud_restante - golpe
            if not puede_ganar(nuevo_largo, not es_jugador_a):
                memoria[(longitud_restante, es_jugador_a)] = True
                return True
        
        memoria[(longitud_restante, es_jugador_a)] = False
        return False
    
    return "A" if puede_ganar(longitud, True) else "B"

def procesar_caso_individual():
    print("\n=== Nuevo Caso de Prueba ===")
    print("Ingrese los siguientes valores separados por espacios:")
    print("1. Longitud del clavo")
    print("2. Golpe mínimo del jugador A")
    print("3. Golpe máximo del jugador A")
    print("4. Golpe mínimo del jugador B")
    print("5. Golpe máximo del jugador B")
    print("\nEjemplo: 10 2 4 1 3")
    
    while True:
        try:
            entrada = input("\nIngrese los valores: ")
            datos = list(map(int, entrada.split()))
            
            if len(datos) != 5:
                print("Error: Debe ingresar exactamente 5 números.")
                continue
                
            longitud, a_min, a_max, b_min, b_max = datos
            
            if longitud <= 0:
                print("Error: La longitud del clavo debe ser positiva.")
                continue
            if a_min > a_max or b_min > b_max:
                print("Error: El golpe mínimo no puede ser mayor que el máximo.")
                continue
            if a_min <= 0 or b_min <= 0:
                print("Error: Los golpes mínimos deben ser positivos.")
                continue
                
            return datos
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")

def procesar_casos_prueba(casos_prueba):
    resultados = []
    for caso in casos_prueba:
        longitud, a_min, a_max, b_min, b_max = caso
        resultados.append(resolver_juego_clavo(longitud, a_min, a_max, b_min, b_max))
    return resultados

def main():
    print("=== Juego del Clavo ===")
    print("\nDescripción:")
    print("- Dos jugadores (A y B) se turnan para golpear un clavo")
    print("- Cada jugador tiene un rango de fuerza para sus golpes")
    print("- Gana quien logre clavar completamente el clavo")
    
    while True:
        try:
            print("\n¿Cuántos casos de prueba desea resolver?")
            numero_casos = int(input("Número de casos: "))
            if numero_casos <= 0:
                print("Por favor, ingrese un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    casos_prueba = []
    for i in range(numero_casos):
        print(f"\nCaso de prueba {i+1}/{numero_casos}")
        casos_prueba.append(procesar_caso_individual())
    
    print("\n=== Resultados ===")
    resultados = procesar_casos_prueba(casos_prueba)
    for i, resultado in enumerate(resultados, 1):
        print(f"\nCaso #{i}:")
        print(f"El jugador {resultado} ganará con juego perfecto")
    
    print("\n¿Desea resolver más casos? (s/n)")
    if input().strip().lower() == 's':
        main()

if __name__ == "__main__":
    main()