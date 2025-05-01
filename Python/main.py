# Importa o mapa do labirinto
from pkg_resources import empty_provider

from lab import lab_map, start, end
from operator import indexOf

def calc_heuristc (initial_pos, destiny_pos):
    return abs(initial_pos[0] - destiny_pos[0]) + abs(initial_pos[1] - destiny_pos[1])

def get_paths (actual_pos, lab):
    possible_paths = []

    if actual_pos[0] > 0:
        if lab[actual_pos[0] + 1][actual_pos[1]] == 0:
            possible_paths.append(indexOf(lab[actual_pos[0]+1][actual_pos[1]]))
        if lab[actual_pos[0] - 1][actual_pos[1] == 0]:
            possible_paths.append(indexOf(lab[actual_pos[0]-1][actual_pos[1]]))

    if actual_pos[1] > 0:
        if lab[actual_pos[0]][actual_pos[1] + 1] == 0:
            possible_paths.append(lab[actual_pos[0]][actual_pos[1] + 1])
        if lab[actual_pos[0]][actual_pos[1] - 1] == 0:
            possible_paths.append(lab[actual_pos[0]][actual_pos[1] - 1])

    if len(possible_paths) == 0:
        return "Erro! Nenhum caminho possível!"

    return possible_paths

