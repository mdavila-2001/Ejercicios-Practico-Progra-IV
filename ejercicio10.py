def resolver_cantina():
    print("\n=== Bienvenido al Resolvedor de la Cantina ===")
    print("Ejemplo de entrada:")
    print("Para n=3, k=0:")
    print("Secuencia a: 1 2 3")
    print("Secuencia b: 2 1 3")
    print("\nFormato de entrada:")
    print("1. Primero ingrese el número de casos")
    print("2. Para cada caso:")
    print("   - Ingrese n y k en una línea (ejemplo: 3 0)")
    print("   - Ingrese n números para secuencia a")
    print("   - Ingrese n números para secuencia b")
    
    while True:
        try:
            print("\nIntroduce el número de casos de prueba:")
            num_casos = int(input())
            if num_casos > 0:
                break
            print("Error: El número debe ser positivo")
        except ValueError:
            print("Error: Ingrese un número válido")

    resultados = []
    
    for caso in range(num_casos):
        print(f"\n=== Caso #{caso+1} ===")
        while True:
            try:
                print("Introduce n y k separados por un espacio (en esta versión k siempre es 0):")
                n, k = map(int, input().split())
                if n > 0:
                    break
                print("El valor de n debe ser positivo.")
            except ValueError:
                print("Por favor, introduce dos números válidos separados por espacio.")
        
        while True:
            try:
                print(f"Introduce {n} números enteros para la secuencia a:")
                secuencia_a = list(map(int, input().split()))
                if len(secuencia_a) == n:
                    break
                print(f"Debes introducir exactamente {n} números.")
            except ValueError:
                print("Por favor, introduce números válidos separados por espacio.")
        
        while True:
            try:
                print(f"Introduce {n} números enteros para la secuencia b:")
                secuencia_b = list(map(int, input().split()))
                if len(secuencia_b) == n:
                    break
                print(f"Debes introducir exactamente {n} números.")
            except ValueError:
                print("Por favor, introduce números válidos separados por espacio.")
        
        rondas = 0
        while any(secuencia_a):
            rondas += 1
            
            for i in range(n):
                minimo = min(secuencia_a[i], secuencia_b[i])
                secuencia_a[i] -= minimo
                secuencia_b[i] -= minimo
            
            secuencia_c = [0] * n
            for i in range(n):
                secuencia_c[i] = secuencia_a[(i-1) % n]
            secuencia_a = secuencia_c.copy()
        
        print(f"\nProcesando caso #{caso+1}...")
        resultados.append(rondas)
    
    print("\n=== Resultados Finales ===")
    for i, rondas in enumerate(resultados):
        print(f"Caso #{i+1}: {rondas} rondas")
    
    print("\n¿Deseas resolver otro conjunto de casos? (s/n):")
    if input().strip().lower() == 's':
        resolver_cantina()

def main():
    num_casos = int(input())
    resultados = []
    
    for _ in range(num_casos):
        n, k = map(int, input().split())
        secuencia_a = list(map(int, input().split()))
        secuencia_b = list(map(int, input().split()))
        
        rondas = 0
        while any(secuencia_a):
            rondas += 1
            
            for i in range(n):
                minimo = min(secuencia_a[i], secuencia_b[i])
                secuencia_a[i] -= minimo
                secuencia_b[i] -= minimo
            
            secuencia_c = [0] * n
            for i in range(n):
                secuencia_c[i] = secuencia_a[(i-1) % n]
            secuencia_a = secuencia_c.copy()
        
        resultados.append(rondas)
    
    for rondas in resultados:
        print(rondas)

if __name__ == "__main__":
    print("=== Programa Resolvedor de la Cantina ===")
    print("¿Ejecutar en modo interactivo? (s/n):")
    while True:
        modo = input().strip().lower()
        if modo in ['s', 'n']:
            break
        print("Por favor, introduce 's' para sí o 'n' para no.")
    
    if modo == 's':
        resolver_cantina()
    else:
        main()