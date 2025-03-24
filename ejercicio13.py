def resolver_problema_ferry(n, t, m, llegadas):
    tiempo_actual = 0
    tiempo_ultimo_auto = 0
    viajes = 0
    
    # Índice del próximo auto a cargar
    indice_auto = 0
    
    # Orilla donde está el ferry (True = orilla inicial, False = orilla opuesta)
    en_orilla_inicial = True
    
    while indice_auto < m:
        if en_orilla_inicial:
            # Determinar cuándo sale el ferry
            tiempo_salida = tiempo_actual
            
            # Si no hay autos esperando, esperar al próximo
            if indice_auto < m and llegadas[indice_auto] > tiempo_actual:
                tiempo_salida = llegadas[indice_auto]
            
            # Cargar autos
            autos_a_cargar = 0
            while indice_auto < m and autos_a_cargar < n and llegadas[indice_auto] <= tiempo_salida:
                indice_auto += 1
                autos_a_cargar += 1
            
            # Actualizar tiempo y cruzar
            tiempo_actual = tiempo_salida + t
            tiempo_ultimo_auto = tiempo_actual
            viajes += 1
            en_orilla_inicial = False
        else:
            # Regresar solo si quedan autos
            if indice_auto < m:
                tiempo_actual += t
                en_orilla_inicial = True
            else:
                break
    
    return tiempo_ultimo_auto, viajes

def main():
    print("\n=== Problema del Ferry ===")
    print("\nDescripción:")
    print("- Un ferry transporta autos de una orilla a otra")
    print("- El ferry tiene capacidad limitada y tarda un tiempo fijo en cruzar")
    print("- Los autos llegan en momentos específicos")
    
    while True:
        try:
            print("\nIngrese el número de casos de prueba:")
            c = int(input())
            if c > 0:
                break
            print("Error: El número debe ser positivo")
        except ValueError:
            print("Error: Ingrese un número válido")

    for caso in range(c):
        print(f"\n=== Caso de prueba {caso + 1}/{c} ===")
        print("\nIngrese tres números separados por espacios:")
        print("1. n: Capacidad del ferry (autos)")
        print("2. t: Tiempo de cruce (minutos)")
        print("3. m: Número total de autos")
        print("\nEjemplo: 2 10 3")
        
        while True:
            try:
                n, t, m = map(int, input().split())
                if n <= 0 or t <= 0 or m <= 0:
                    print("Error: Todos los valores deben ser positivos")
                    continue
                break
            except ValueError:
                print("Error: Ingrese tres números válidos separados por espacios")

        print(f"\nIngrese los tiempos de llegada de los {m} autos:")
        print("(Un tiempo por línea, en minutos)")
        print("Ejemplo:")
        print("0")
        print("5")
        print("10")
        
        llegadas = []
        for i in range(m):
            while True:
                try:
                    tiempo = int(input(f"Tiempo de llegada del auto {i+1}: "))
                    if tiempo < 0:
                        print("Error: El tiempo no puede ser negativo")
                        continue
                    llegadas.append(tiempo)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido")
        
        tiempo_final, num_viajes = resolver_problema_ferry(n, t, m, llegadas)
        print(f"\nResultado del caso {caso + 1}:")
        print(f"Tiempo final: {tiempo_final} minutos")
        print(f"Número de viajes: {num_viajes}")

if __name__ == "__main__":
    main()