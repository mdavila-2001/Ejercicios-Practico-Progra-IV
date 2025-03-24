def calcular_gatos_y_altura(altura_inicial, trabajadores):
    """
    Calcula el número de gatos que no trabajan y la altura total de todos los gatos.
    
    Args:
        altura_inicial: Altura del gato inicial
        trabajadores: Número de gatos trabajadores (de altura 1)
    
    Returns:
        tuple: (gatos_que_no_trabajan, altura_total)
    """
    # Si no hay trabajadores o la altura inicial es 1, no hay gatos que no trabajen
    if trabajadores == 0 or altura_inicial == 1:
        return 0, altura_inicial
    
    # Calculamos N (número de gatos en cada sombrero)
    # Necesitamos encontrar N tal que el número total de gatos de altura 1 sea igual a 'trabajadores'
    # Para un gato de altura h, el número de gatos de altura 1 que genera es N^(h-1)
    # Por lo tanto: N^(altura_inicial-1) = trabajadores
    # De donde: N = trabajadores^(1/(altura_inicial-1))
    
    N = int(round(trabajadores ** (1 / (altura_inicial - 1))))
    
    # Verificamos que N sea correcto
    if N ** (altura_inicial - 1) != trabajadores:
        # Si no es exacto, calculamos una aproximación
        N = int(round(trabajadores ** (1 / (altura_inicial - 1))))
    
    # Calculamos el número total de gatos (incluyendo trabajadores)
    # La suma total es: 1 + N + N^2 + ... + N^(altura_inicial-1)
    # Esta es una serie geométrica con primer término 1 y razón N
    if N == 1:
        total_gatos = altura_inicial
    else:
        total_gatos = (N ** altura_inicial - 1) // (N - 1)
    
    # Gatos que no trabajan = total_gatos - trabajadores
    gatos_que_no_trabajan = total_gatos - trabajadores
    
    # Altura total de todos los gatos
    # Para cada nivel h, hay N^(altura_inicial-h) gatos, cada uno de altura h
    altura_total = 0
    for h in range(1, altura_inicial + 1):
        num_gatos_altura_h = N ** (altura_inicial - h)
        altura_nivel = h * num_gatos_altura_h
        altura_total += altura_nivel
    
    return gatos_que_no_trabajan, altura_total

def main():
    """
    Función principal que maneja la entrada y salida.
    """
    print("¡Bienvenido al Calculador de Gatos en Sombreros!")
    print("------------------------------------------------")
    print("Este programa calcula, para cada especificación de gato-en-sombrero:")
    print("1. El número de gatos que no están trabajando")
    print("2. La altura total de todos los gatos apilados")
    print()
    print("Instrucciones de uso:")
    print("- Ingrese dos números enteros positivos por línea: la altura del gato inicial y el número de gatos trabajadores.")
    print("- Para terminar el programa, ingrese '0 0'.")
    print("- Por ejemplo: '216 125' significa un gato inicial de altura 216 con 125 gatos trabajadores.")
    print()
    
    resultados = []
    
    while True:
        entrada = input("Ingrese la altura del gato inicial y el número de trabajadores (o '0 0' para terminar): ")
        valores = list(map(int, entrada.split()))
        
        if len(valores) != 2:
            print("Error: Ingrese exactamente dos números separados por espacio.")
            continue
        
        altura_inicial, trabajadores = valores
        
        if altura_inicial == 0 and trabajadores == 0:
            break
        
        try:
            gatos_que_no_trabajan, altura_total = calcular_gatos_y_altura(altura_inicial, trabajadores)
            resultados.append((gatos_que_no_trabajan, altura_total))
            print(f"Resultado: {gatos_que_no_trabajan} {altura_total}")
        except Exception as e:
            print(f"Error al calcular: {e}")
    
    # Mostrar todos los resultados al final
    if resultados:
        print("\nResumen de resultados:")
        for i, (no_trabajadores, altura) in enumerate(resultados, 1):
            print(f"Caso {i}: {no_trabajadores} {altura}")

if __name__ == "__main__":
    main()
