def calcular_crc(mensaje, generador=34943):
    """
    Calcula el valor CRC para un mensaje dado.
    
    Args:
        mensaje: El mensaje para el cual calcular el CRC
        generador: El valor generador (g) para el cálculo CRC
    
    Returns:
        El valor CRC calculado
    """
    # Convertir el mensaje a un número binario largo
    valor_mensaje = 0
    for caracter in mensaje:
        # Desplazar el valor actual a la izquierda 8 bits y agregar el nuevo byte
        valor_mensaje = (valor_mensaje << 8) + ord(caracter)
    
    # Desplazar el valor del mensaje 16 bits a la izquierda (equivalente a agregar 2 bytes de CRC)
    valor_mensaje_con_espacio = valor_mensaje << 16
    
    # Calcular el valor CRC
    # Necesitamos encontrar un valor de CRC tal que (mensaje + CRC) % generador = 0
    # Esto significa que CRC = (-(mensaje << 16) % generador) % generador
    
    # Python calcula el módulo de manera diferente para números negativos,
    # así que usamos esta fórmula equivalente:
    crc = valor_mensaje_con_espacio % generador
    if crc != 0:
        crc = generador - crc
    
    return crc

def main():
    """Función principal del programa"""
    print("Por favor, introduce líneas de texto (termina con '#' en la primera columna):")
    
    while True:
        entrada = input()
        
        # Verificar si es el fin de la entrada
        if entrada and entrada[0] == '#':
            break
        
        # Calcular el CRC para la línea de entrada
        valor_crc = calcular_crc(entrada)
        
        # Imprimir el resultado en formato hexadecimal
        # El primer byte es los 8 bits más significativos, el segundo byte los 8 bits menos significativos
        primer_byte = (valor_crc >> 8) & 0xFF
        segundo_byte = valor_crc & 0xFF
        
        print(f"{primer_byte:02X} {segundo_byte:02X}")

if __name__ == "__main__":
    main()