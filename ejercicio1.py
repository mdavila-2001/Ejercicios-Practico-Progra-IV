import heapq

def solve_maze(n, exit_cell, time_limit, connections):
    graph = [[] for _ in range(n + 1)]
    for a, b, time in connections:
        graph[b].append((a, time))
    
    min_times = [float('inf')] * (n + 1)
    min_times[exit_cell] = 0
    pq = [(0, exit_cell)]
    
    while pq:
        current_time, current_cell = heapq.heappop(pq)
        if current_time > min_times[current_cell]:
            continue
        
        for neighbor, travel_time in graph[current_cell]:
            new_time = current_time + travel_time
            if new_time < min_times[neighbor]:
                min_times[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    
    return sum(1 for cell in range(1, n + 1) if min_times[cell] <= time_limit)

def main():
    print("\n=== SIMULADOR DE ESCAPE DE RATONES ===")
    try:
        num_cases = int(input("Número de casos: "))
        
        for case in range(num_cases):
            print(f"\n--- Caso {case + 1} ---")
            
            if case > 0:
                input()  # Línea en blanco
            
            n = int(input("Número de celdas: "))
            exit_cell = int(input("Celda de salida: "))
            time_limit = int(input("Límite de tiempo: "))
            m = int(input("Número de conexiones: "))
            
            if not all([n > 0, 1 <= exit_cell <= n, time_limit >= 0, m >= 0]):
                print("Error: Valores fuera de rango")
                continue
            
            print("\nIngrese las conexiones (origen destino tiempo):")
            connections = []
            for i in range(m):
                try:
                    a, b, time = map(int, input().split())
                    if 1 <= a <= n and 1 <= b <= n and time >= 0:
                        connections.append((a, b, time))
                    else:
                        raise ValueError("Valores fuera de rango")
                except:
                    print("Error: Formato inválido")
                    break
            else:
                result = solve_maze(n, exit_cell, time_limit, connections)
                print(f"\nRatones que escapan: {result} de {n}")
            
            if case < num_cases - 1:
                print("\nPresione ENTER para continuar...")
    
    except ValueError:
        print("Error: Entrada inválida")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido")
    except:
        print("Error inesperado")

if __name__ == "__main__":
    main()