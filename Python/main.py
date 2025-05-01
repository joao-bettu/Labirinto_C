# Importa o mapa do labirinto
from lab import lab_map, lines, columns, start, end

def print_map (lab, actual_position):
    for i in range(lines):
        for j in range(columns):
            if [i, j] == start:
                print("S", end="")
            elif [i, j] == end:
                print("E", end="")
            elif [i, j] == actual_position:
                print("A", end="")
            else:
                print(f"{lab[i][j]}", end="")
        print()
    print()
    return

def calc_heuristc (position):
    return abs(position[0] - end[0]) + abs(position[1] - end[1])

def get_paths(actual_pos, lab, seen):
    possible_paths = []

    if actual_pos[0] > 0:
        if lab[actual_pos[0] - 1][actual_pos[1]] == 0:
            possible_paths.append([actual_pos[0] - 1, actual_pos[1]])
    if actual_pos[0] < 9:
        if lab[actual_pos[0] + 1][actual_pos[1]] == 0:
            possible_paths.append([actual_pos[0] + 1, actual_pos[1]])

    if actual_pos[1] > 0:
        if lab[actual_pos[0]][actual_pos[1] - 1] == 0:
            possible_paths.append([actual_pos[0], actual_pos[1] - 1])
    if actual_pos[1] < 9:
        if lab[actual_pos[0]][actual_pos[1] + 1] == 0:
            possible_paths.append([actual_pos[0], actual_pos[1] + 1])

    filtered = [pos for pos in possible_paths if pos not in seen]

    if not filtered:
        return None

    return filtered


def choose_path(paths, last):
    heuristics = [calc_heuristc(pos) for pos in paths]
    min_heuristic = min(heuristics)

    candidates = [pos for pos, h in zip(paths, heuristics) if h == min_heuristic]

    if last in candidates and len(candidates) > 1:
        candidates.remove(last)

    return candidates[0]

def main():
    seen_paths = [start]
    position = start
    last_step = position

    print_map(lab_map, position)

    while position != end:
        possible_paths = get_paths(position, lab_map, seen_paths)
        if not possible_paths:
            print("Sem saída!")
            return
        next_step = choose_path(possible_paths, last_step)
        last_step = position
        position = next_step
        seen_paths.append(position)
        print_map(lab_map, position)

    print("Labirinto Concluído!")

if __name__ == "__main__":
    main()