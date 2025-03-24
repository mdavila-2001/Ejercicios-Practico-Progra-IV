def main():
    # Diccionario de caracteres y sus reversos
    reversos = {
        'A': 'A', 'B': ' ', 'C': ' ', 'D': ' ', 'E': '3',
        'F': ' ', 'G': ' ', 'H': 'H', 'I': 'I', 'J': 'L',
        'K': ' ', 'L': 'J', 'M': 'M', 'N': ' ', 'O': 'O',
        'P': ' ', 'Q': ' ', 'R': ' ', 'S': '2', 'T': 'T',
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
        'Z': '5', '1': '1', '2': 'S', '3': 'E', '4': ' ',
        '5': 'Z', '6': ' ', '7': ' ', '8': '8', '9': ' '
    }
    
    try:
        while True:
            cadena = input().strip()
            
            es_palindromo = es_palindromo_regular(cadena)
            es_espejo = es_cadena_espejo(cadena, reversos)
            
            # Clasificar según los criterios
            if es_palindromo and es_espejo:
                resultado = f"{cadena} -- es un palíndromo espejo."
            elif es_palindromo:
                resultado = f"{cadena} -- es un palíndromo regular."
            elif es_espejo:
                resultado = f"{cadena} -- es una cadena espejo."
            else:
                resultado = f"{cadena} -- no es un palíndromo."
                
            print(resultado)
            print()  # Línea vacía después de cada resultado
            
    except EOFError:
        pass

def es_palindromo_regular(s):
    return s == s[::-1]

def es_cadena_espejo(s, reversos):
    n = len(s)
    for i in range((n + 1) // 2):
        # Obtener caracteres en posiciones simétricas
        caracter_izq = s[i]
        caracter_der = s[n-1-i]
        
        # Verificar si los caracteres tienen reversos válidos
        if caracter_izq not in reversos or reversos[caracter_izq] == ' ' or caracter_der not in reversos or reversos[caracter_der] == ' ':
            return False
        
        # Verificar si el reverso del carácter izquierdo es igual al carácter derecho
        if reversos[caracter_izq] != caracter_der:
            return False
    
    return True

if __name__ == "__main__":
    main()