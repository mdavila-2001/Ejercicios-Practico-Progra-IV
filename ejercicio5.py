def procesar_casos():
    # Solicitar el número de casos a procesar
    print("Ingrese el número de casos a procesar:")
    num_casos = int(input())
    input()  # Leer línea en blanco

    for caso in range(num_casos):
        if caso > 0:
            print()

        print(f"\n--- Caso {caso + 1} ---")
        print("Ingrese las transacciones en el formato: fecha numero_cheque monto")
        print("(Presione Enter dos veces para finalizar este caso)\n")

        transacciones = []
        while True:
            try:
                linea = input().strip()
                if linea == "":
                    break
                # Parsear la línea: fecha, número de cheque, monto
                fecha, num_cheque, monto = linea.split()
                try:
                    transacciones.append((fecha, int(num_cheque), float(monto)))
                except ValueError:
                    print("Error: Formato inválido. Use: YYYY-MM-DD numero_cheque monto")
                    continue
            except EOFError:
                break
        
        # Ordenar por número de cheque
        transacciones.sort(key=lambda x: x[1])
        
        # Marcar cheques fuera de secuencia
        cheques_marcados = []
        ultimo_num = 0
        
        for fecha, num_cheque, monto in transacciones:
            # Un cheque está fuera de secuencia si no sigue inmediatamente al anterior
            fuera_secuencia = (num_cheque != ultimo_num + 1) and ultimo_num != 0
            cheques_marcados.append((fecha, num_cheque, monto, fuera_secuencia))
            ultimo_num = num_cheque
        
        # Imprimir resultado en formato de columnas
        imprimir_columnas(cheques_marcados)

def imprimir_columnas(cheques):
    # Calcular número de filas necesarias
    num_cheques = len(cheques)
    filas = (num_cheques + 2) // 3  # División con redondeo hacia arriba
    
    # Imprimir cheques en formato de columnas
    for i in range(filas):
        linea = ""
        
        # Primera columna
        if i < num_cheques:
            fecha, num, monto, fuera_secuencia = cheques[i]
            marca = "*" if fuera_secuencia else " "
            # Formatear monto (con cero antes del punto decimal si es menor a 1)
            monto_str = f"{monto:.2f}"
            if monto < 1:
                monto_str = "0" + monto_str
            linea += f"{num}{marca} {monto_str} {fecha}"
        
        # Segunda columna
        idx_col2 = i + filas
        if idx_col2 < num_cheques:
            fecha, num, monto, fuera_secuencia = cheques[idx_col2]
            marca = "*" if fuera_secuencia else " "
            monto_str = f"{monto:.2f}"
            if monto < 1:
                monto_str = "0" + monto_str
            # Añadir espacios entre columnas
            linea += "   " + f"{num}{marca} {monto_str} {fecha}"
        
        # Tercera columna
        idx_col3 = i + 2*filas
        if idx_col3 < num_cheques:
            fecha, num, monto, fuera_secuencia = cheques[idx_col3]
            marca = "*" if fuera_secuencia else " "
            monto_str = f"{monto:.2f}"
            if monto < 1:
                monto_str = "0" + monto_str
            # Añadir espacios entre columnas
            linea += "   " + f"{num}{marca} {monto_str} {fecha}"
        
        print(linea)

# Ejecutar el programa
if __name__ == "__main__":
    procesar_casos()