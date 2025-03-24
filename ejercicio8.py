def main():
    print("\n=== Simulador de Mundo de Bloques bajo Algoritmo Ad Hoc ===")
    print("Comandos disponibles:")
    print("- move a onto b: Mueve el bloque a sobre el bloque b")
    print("- move a over b: Mueve el bloque a sobre la pila donde está b")
    print("- pile a onto b: Apila el bloque a y los bloques encima sobre b")
    print("- pile a over b: Apila el bloque a y los bloques encima sobre la pila de b")
    print("- quit: Terminar el programa\n")

    # Leer el número de bloques
    n = int(input("Ingrese el número de bloques (n): "))
    
    # Inicializar el mundo de bloques
    mundo = [[] for _ in range(n)]
    for i in range(n):
        mundo[i].append(i)
    
    print("\nEstado inicial:")
    imprimir_mundo(mundo)
    print("\nIngrese sus comandos (ejemplo: 'move 2 onto 1'):")

    # Procesar comandos hasta encontrar "quit"
    while True:
        comando = input("> ")
        if comando.lower() == "quit":
            break
            
        # Parsear el comando
        partes = comando.split()
        tipo_comando = partes[0]  # "move" o "pile"
        a = int(partes[1])  # bloque a mover
        preposicion = partes[2]  # "onto" o "over"
        b = int(partes[3])  # bloque destino
        
        # Ignorar comandos ilegales
        if a == b or en_misma_pila(mundo, a, b):
            continue
            
        # Encontrar posiciones de a y b
        pos_a, altura_a = encontrar_bloque(mundo, a)
        pos_b, altura_b = encontrar_bloque(mundo, b)
        
        # Ejecutar el comando según su tipo
        if tipo_comando == "move":
            # Devolver bloques encima de a a sus posiciones iniciales
            devolver_bloques_encima(mundo, pos_a, altura_a + 1)
            
            if preposicion == "onto":
                # Devolver bloques encima de b a sus posiciones iniciales
                devolver_bloques_encima(mundo, pos_b, altura_b + 1)
                
            # Mover bloque a
            bloque_a = mundo[pos_a].pop(altura_a)
            mundo[pos_b].append(bloque_a)
            
        elif tipo_comando == "pile":
            if preposicion == "onto":
                # Devolver bloques encima de b a sus posiciones iniciales
                devolver_bloques_encima(mundo, pos_b, altura_b + 1)
                
            # Obtener la pila sobre a (incluyendo a)
            pila_a = mundo[pos_a][altura_a:]
            # Eliminar la pila del origen
            mundo[pos_a] = mundo[pos_a][:altura_a]
            # Añadir la pila al destino
            mundo[pos_b].extend(pila_a)
    
    # Imprimir el estado final
    for i in range(n):
        print(f"{i}:", end="")
        if mundo[i]:
            print(" " + " ".join(str(bloque) for bloque in mundo[i]), end="")
        print()

def encontrar_bloque(mundo, bloque):
    """
    Encuentra la posición y altura de un bloque en el mundo.
    Retorna (posición, altura)
    """
    for pos, pila in enumerate(mundo):
        for altura, b in enumerate(pila):
            if b == bloque:
                return pos, altura
    return -1, -1  # No debería ocurrir si el bloque existe

def en_misma_pila(mundo, a, b):
    """
    Verifica si los bloques a y b están en la misma pila.
    """
    pos_a, _ = encontrar_bloque(mundo, a)
    pos_b, _ = encontrar_bloque(mundo, b)
    return pos_a == pos_b

def devolver_bloques_encima(mundo, pos, altura_inicio):
    """
    Devuelve todos los bloques desde altura_inicio hasta el tope
    a sus posiciones iniciales.
    """
    for altura in range(altura_inicio, len(mundo[pos])):
        bloque = mundo[pos][altura]
        mundo[bloque] = [bloque]  # Devolver a posición inicial
    
    # Recortar la pila hasta altura_inicio
    mundo[pos] = mundo[pos][:altura_inicio]

def imprimir_mundo(mundo):
    """
    Imprime el estado actual del mundo de bloques
    """
    for i in range(len(mundo)):
        print(f"{i}:", end="")
        if mundo[i]:
            print(" " + " ".join(str(bloque) for bloque in mundo[i]), end="")
        print()

if __name__ == "__main__":
    main()