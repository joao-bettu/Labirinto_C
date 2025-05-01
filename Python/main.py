from operator import indexOf
# Importa o mapa do labirinto
from lab import lab_map, start, end

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

def choose_path (path):
    heuristics = []

    for i in path:
        heuristics.append(calc_heuristc(path[i], end))

    shortest = heuristics[0]
    index_shortest = 0

    for i in heuristics:
        if heuristics[i] < shortest:
            shortest = heuristics[i]
            index_shortest = indexOf(heuristics[i])

    return path[index_shortest]