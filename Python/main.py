# Importa o mapa do labirinto
from lab import lab_map, start, end

def print_map (lab, initial_point, finish, actual_position):
    for i in range(10):
        for j in range(10):
            if lab[i][j] == initial_point:
                print("S", end="")
            elif lab[i][j] == finish:
                print("E", end="")
            elif lab[i][j] == actual_position:
                print("A", end="")
            else:
                print(f"{lab[i][j]}", end="")
        print()
    print()
    return

def calc_heuristc (position, destiny_pos):
    return abs(position[0] - destiny_pos[0]) + abs(position[1] - destiny_pos[1])

def get_paths (actual_pos, lab):
    possible_paths = []

    if actual_pos[0] == 0:
        if lab[actual_pos[0] + 1][actual_pos[1]] == 0:
            possible_paths.append([actual_pos[0] + 1, actual_pos[1]])
    elif 0 < actual_pos[0] < 9:
        if lab[actual_pos[0] + 1][actual_pos[1]] == 0:
            possible_paths.append([actual_pos[0] + 1, actual_pos[1]])
        if lab[actual_pos[0] - 1][actual_pos[1] == 0]:
            possible_paths.append([actual_pos[0] - 1, actual_pos[1]])
    else:
        if lab[actual_pos[0] - 1][actual_pos[1] == 0]:
            possible_paths.append([actual_pos[0] - 1, actual_pos[1]])

    if actual_pos[1] == 0:
        if lab[actual_pos[0]][actual_pos[1] + 1] == 0:
            possible_paths.append([actual_pos[0], actual_pos[1] + 1])
    elif 0 < actual_pos[1] < 9:
        if lab[actual_pos[0]][actual_pos[1] + 1] == 0:
            possible_paths.append([actual_pos[0], actual_pos[1] + 1])
        if lab[actual_pos[0]][actual_pos[1] - 1] == 0:
            possible_paths.append([actual_pos[0], actual_pos[1] - 1])
    else:
        if lab[actual_pos[0]][actual_pos[1] - 1] == 0:
            possible_paths.append([actual_pos[0], actual_pos[1] - 1])

    if len(possible_paths) == 0:
        return "Erro! Nenhum caminho possível!"

    return possible_paths

def choose_path (path, last):
    heuristics = []

    for i in range(len(path)):
        heuristics.append(calc_heuristc(path[i], end))

    index_shortest = 0
    shortest = heuristics[index_shortest]

    for i in range(len(heuristics)):
        if heuristics[i] < shortest:
            shortest = heuristics[i]
            index_shortest = i
        elif heuristics[i] == shortest:
            if path[i] == last:
                continue

    return path[index_shortest]

def main ():
    seen_paths = [start]
    position = start
    last_step = 0
    next_step = 0

    print_map(lab_map, start, end,position)

    while position != end:
        possible_path = get_paths(position, lab_map)
        next_step = choose_path(possible_path, last_step)
        last_step = position
        position = next_step
        seen_paths.append(position)
        print_map(lab_map, start, end, position)

    print("Labirinto Concluído!")
    return

if __name__ == "__main__":
    main()