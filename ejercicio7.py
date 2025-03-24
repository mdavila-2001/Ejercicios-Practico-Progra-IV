def codificar_mensaje(mensaje):
    # Invertir el mensaje para procesarlo desde el último caracter hasta el primero
    mensaje_invertido = mensaje[::-1]
    
    # Inicializar la cadena codificada
    codificado = ""
    
    # Procesar cada caracter
    for caracter in mensaje_invertido:
        # Obtener el valor ASCII
        valor_ascii = ord(caracter)
        # Convertir a string e invertir
        ascii_str = str(valor_ascii)
        ascii_invertido = ascii_str[::-1]
        # Añadir al resultado
        codificado += ascii_invertido
    
    return codificado

def decodificar_mensaje(codificado):
    # Inicializar el mensaje decodificado y el índice para recorrer la cadena codificada
    decodificado = ""
    i = 0
    
    # Recorrer la cadena codificada
    while i < len(codificado):
        # Buscar los posibles valores ASCII
        # Los valores ASCII de los caracteres válidos están entre 32 y 122
        # Por lo tanto, pueden tener 2 o 3 dígitos
        
        # Intentar primero con 2 dígitos (para valores ASCII como 32-99)
        if i + 1 < len(codificado):
            dos_digitos = codificado[i:i+2]
            dos_digitos_invertidos = dos_digitos[::-1]
            ascii_dos = int(dos_digitos_invertidos)
            
            # Verificar si es un valor ASCII válido
            if 32 <= ascii_dos <= 122:
                decodificado += chr(ascii_dos)
                i += 2
                continue
        
        # Si no funcionó con 2 dígitos o no hay suficientes caracteres, 
        # intentar con 3 dígitos (para valores ASCII como 100-122)
        if i + 2 < len(codificado):
            tres_digitos = codificado[i:i+3]
            tres_digitos_invertidos = tres_digitos[::-1]
            ascii_tres = int(tres_digitos_invertidos)
            
            # Verificar si es un valor ASCII válido
            if 32 <= ascii_tres <= 122:
                decodificado += chr(ascii_tres)
                i += 3
                continue
        
        # Si llegamos aquí, hubo un error en el formato del mensaje
        print(f"Error: No se pudo decodificar en la posición {i}")
        return "Error en la decodificación"
    
    # Invertir el mensaje decodificado para obtener el original
    return decodificado[::-1]

def procesar_archivo_entrada(nombre_archivo_entrada, nombre_archivo_salida):
    try:
        with open(nombre_archivo_entrada, 'r') as archivo_entrada, open(nombre_archivo_salida, 'w') as archivo_salida:
            for linea in archivo_entrada:
                linea = linea.strip()
                
                # Determinar si es un mensaje normal o codificado
                es_codificado = all(c.isdigit() for c in linea)
                
                if es_codificado:
                    resultado = decodificar_mensaje(linea)
                else:
                    resultado = codificar_mensaje(linea)
                
                archivo_salida.write(resultado + '\n')
        
        print(f"Procesamiento completado. Resultados guardados en {nombre_archivo_salida}")
    
    except Exception as e:
        print(f"Error al procesar los archivos: {e}")

if __name__ == "__main__":
    while True:
        print("\n=== Mensaje Codificador/Decodificador ===")
        mensaje = input("Ingrese el mensaje (o 'salir' para terminar): ")
        
        if mensaje.lower() == 'salir':
            break
            
        if mensaje.strip():
            if mensaje.isdigit():
                resultado = decodificar_mensaje(mensaje)
                print(f"\nMensaje decodificado: '{resultado}'")
            else:
                resultado = codificar_mensaje(mensaje)
                print(f"\nMensaje codificado: '{resultado}'")
        else:
            print("Por favor ingrese un mensaje válido.")