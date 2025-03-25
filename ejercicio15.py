import heapq

class Table:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = 0  # 0: vacio, 1: un espacio ocupado, 2: lleno

    def __lt__(self, other):
        # Prioriza las mesas más cercanas al origen
        return (self.x + self.y) < (other.x + other.y)

    def __repr__(self):
        return f"Mesa({self.x}, {self.y}, {self.occupied})"

def find_nearest_table(guest_type, occupied_tables, current_x, current_y):
    """
    Encuentra la mesa más cercana según el tipo de invitado.

    Args:
        guest_type: 0 para un invitado que busca una mesa vacía, 1 para un invitado que busca una mesa con espacio.
        occupied_tables: Conjunto de mesas ocupadas.
        current_x: Coordenada x actual del invitado.
        current_y: Coordenada y actual del invitado.

    Returns:
        La mesa más cercana que cumple los requisitos.
    """
    candidates = []
    for x in range(current_x // 3 + 1):
        for y in range(current_y // 3 + 1):
            table = Table(x, y)
            # Verifica si la mesa está dentro de los límites de búsqueda
            if (table.x * 3 + 1 <= current_x) and (table.y * 3 + 1 <= current_y):
                # Verifica si la mesa está ocupada o no, según el tipo de invitado
                if guest_type == 0 and table not in occupied_tables:
                    heapq.heappush(candidates, table)
                elif guest_type == 1 and table in occupied_tables and table.occupied < 2:
                    heapq.heappush(candidates, table)
    if candidates:
        return heapq.heappop(candidates)
    else:
        return None

def assign_seats(guests):
    """
    Asigna asientos a los invitados.

    Args:
        guests: Lista de invitados con sus características (0 o 1).

    Returns:
        Lista de asientos asignados a cada invitado.
    """
    occupied_tables = set()
    seats = []
    for i, guest_type in enumerate(guests):
        # Encuentra la mesa más cercana
        table = find_nearest_table(guest_type, occupied_tables, 0, 0)
        if table:
            # Asigna el asiento y actualiza el estado de la mesa
            if table.occupied == 0:
                table.occupied = 1
            else:
                table.occupied = 2
            occupied_tables.add(table)
            seats.append(f"({table.x * 3 + 1}, {table.y * 3 + 1})")
        else:
            seats.append("Sin asiento disponible")
    return seats

# Interfaz de usuario
print("¡Bienvenido al comedor infinito!")
num_guests = int(input("Ingresa el número de invitados: "))
guests = []
print("Ingresa las características de los invitados (0 o 1):")
for i in range(num_guests):
    guests.append(int(input(f"Invitado {i+1}: ")))

assigned_seats = assign_seats(guests)
print("\nAsientos asignados:")
for i, seat in enumerate(assigned_seats):
    print(f"Invitado {i+1}: {seat}")