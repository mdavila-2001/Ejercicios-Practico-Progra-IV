def movimientos_caballo(inicio, fin):
    """
    Calcula el número mínimo de movimientos de caballo para ir desde 'inicio' hasta 'fin'
    en un tablero de ajedrez.
    
    Args:
        inicio: Una cadena de dos caracteres (por ejemplo, 'e2')
        fin: Una cadena de dos caracteres (por ejemplo, 'e4')
    
    Returns:
        El número mínimo de movimientos necesarios
    """
    # Si las casillas son iguales, no se necesitan movimientos
    if inicio == fin:
        return 0
    
    # Convertir las posiciones de notación de ajedrez a coordenadas (x, y)
    # donde 'a' es 0 y '1' es 0
    inicio_x = ord(inicio[0]) - ord('a')
    inicio_y = int(inicio[1]) - 1
    
    fin_x = ord(fin[0]) - ord('a')
    fin_y = int(fin[1]) - 1
    
    # Posibles movimientos del caballo (en forma de L)
    movimientos_posibles = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    # Cola para BFS (Búsqueda en Anchura), empezando desde la casilla inicial con 0 movimientos
    cola = [(inicio_x, inicio_y, 0)]
    
    # Conjunto para marcar casillas visitadas
    visitadas = set([(inicio_x, inicio_y)])
    
    # BFS (Búsqueda en Anchura)
    while cola:
        x, y, movimientos = cola.pop(0)
        
        # Verificar si hemos llegado a la casilla destino
        if x == fin_x and y == fin_y:
            return movimientos
        
        # Probar todos los posibles movimientos del caballo
        for dx, dy in movimientos_posibles:
            nuevo_x, nuevo_y = x + dx, y + dy
            
            # Verificar si el nuevo movimiento está dentro del tablero
            if 0 <= nuevo_x < 8 and 0 <= nuevo_y < 8 and (nuevo_x, nuevo_y) not in visitadas:
                cola.append((nuevo_x, nuevo_y, movimientos + 1))
                visitadas.add((nuevo_x, nuevo_y))
    
    # Si no se puede llegar a la casilla destino (no debería ocurrir en un tablero de ajedrez)
    return -1

def main():
    """
    Función principal que lee las entradas, procesa cada caso y muestra los resultados.
    """
    # Lista para almacenar los casos de prueba
    casos_prueba = []
    
    print("Introduce los casos de prueba, uno por línea.")
    print("Cada línea debe contener dos posiciones separadas por un espacio (ejemplo: 'e2 e4').")
    print("Para terminar la entrada, favor pulsa el botón enter en la entrada vacía.")
    
    # Leer la entrada hasta que no haya más líneas
    try:
        while True:
            linea = input("Por favor coloca las casillas origen y destino para el caballo, separadas por un espacio: ")
            if not linea:
                break
            inicio, fin = linea.split()
            casos_prueba.append((inicio, fin))
    except EOFError:
        pass
    
    print("\nResultados:")
    # Procesar cada caso de prueba
    for inicio, fin in casos_prueba:
        movimientos = movimientos_caballo(inicio, fin)
        print(f"Para ir de {inicio} a {fin} el caballo se moverá {movimientos} veces.")

if __name__ == "__main__":
    main()