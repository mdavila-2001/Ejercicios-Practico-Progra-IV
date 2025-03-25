def solve_target_number(target, numbers):
    """
    Encuentra la secuencia de operaciones para alcanzar el número objetivo.

    Args:
        target (int): El número objetivo a alcanzar.
        numbers (list): La lista de números iniciales.

    Returns:
        list: Una lista de strings que representan las operaciones, o "No solution" si no se encuentra una solución.
    """

    operations = []  # Lista para almacenar las operaciones
    visited = set()  # Conjunto para rastrear los números ya utilizados

    def backtrack(current_numbers):
        """Función recursiva para explorar las posibles operaciones."""
        nonlocal operations

        if target in current_numbers:
            operations.append(f"{target} <-")  # Se encontró la solución
            return True

        for i in range(len(current_numbers)):
            for j in range(i + 1, len(current_numbers)):
                # Evitar operaciones repetidas
                if (current_numbers[i], current_numbers[j]) in visited:
                    continue

                visited.add((current_numbers[i], current_numbers[j]))

                # Probar las cuatro operaciones
                for operator, symbol in [(lambda x, y: x + y, '+'),
                                        (lambda x, y: x * y, 'x'),
                                        (lambda x, y: x - y, '-'),
                                        (lambda x, y: x // y if x % y == 0 else None, '/')]:
                    result = operator(current_numbers[i], current_numbers[j])
                    if result is not None and result > 0:
                        new_numbers = current_numbers[:i] + current_numbers[i + 1:j] + current_numbers[j + 1:]
                        new_numbers.insert(0, result)  # Agregar el resultado al inicio
                        operations.append(f"{current_numbers[i]} {symbol} {current_numbers[j]} = {result}")
                        if backtrack(new_numbers):
                            return True
                        operations.pop()  # Retroceder si no se encontró la solución

        return False

    # Ordenar los números iniciales para aplicar la regla de prioridad
    numbers.sort()
    if backtrack(numbers):
        return operations
    else:
        return "No solution"

# Interfaz interactiva
while True:
    target = int(input("Ingresa el número objetivo (o 0 para salir): "))
    if target == 0:
        break

    numbers_str = input("Ingresa los números iniciales separados por espacios: ")
    numbers = [int(x) for x in numbers_str.split()]

    solution = solve_target_number(target, numbers)
    print("\n".join(solution))
    print("-" * 20)
