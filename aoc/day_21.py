import fileinput
from functools import cache
from itertools import chain, pairwise

import networkx as nx


def main():
    codes = list(map(str.rstrip, fileinput.input()))

    print(sum(resolve(code, 2) for code in codes))
    print(sum(resolve(code, 25) for code in codes))


def path_to_keys(path: list[tuple[int, int]]) -> str:
    keys = []

    for (y_1, x_1), (y_2, x_2) in pairwise(path):
        if y_1 < y_2:
            keys.append('v')
        elif y_2 < y_1:
            keys.append('^')
        elif x_1 < x_2:
            keys.append('>')
        else:
            keys.append('<')

    return ''.join(keys) + 'A'


def get_num_keypad_key_paths() -> list[list[list[str]]]:
    # +---+---+---+
    # | 7 | 8 | 9 |
    # +---+---+---+
    # | 4 | 5 | 6 |
    # +---+---+---+
    # | 1 | 2 | 3 |
    # +---+---+---+
    #     | 0 | A |
    #     +---+---+
    g = nx.grid_2d_graph(4, 3)
    g.remove_node((3, 0))
    translator = {(y, x): tile
                  for y, line in enumerate([[7, 8, 9],
                                            [4, 5, 6],
                                            [1, 2, 3],
                                            [-1, 0, 10]])
                  for x, tile in enumerate(line)
                  if tile != ' '}
    num_keypad_key_paths = [[[] for _ in range(11)] for _ in range(11)]

    # noinspection PyUnresolvedReferences
    for start, stops in nx.all_pairs_all_shortest_paths(g):
        for stop, paths in stops.items():
            num_keypad_key_paths[translator[start]][translator[stop]] = list(map(path_to_keys, paths))

    return num_keypad_key_paths


def get_dir_keypad_key_paths() -> dict[str, dict[str, list[str]]]:
    #     +---+---+
    #     | ^ | A |
    # +---+---+---+
    # | < | v | > |
    # +---+---+---+
    g = nx.grid_2d_graph(2, 3)
    g.remove_node((0, 0))
    translator = {(y, x): tile
                  for y, line in enumerate([[' ', '^', 'A'],
                                            ['<', 'v', '>']])
                  for x, tile in enumerate(line)
                  if tile != ' '}

    # noinspection PyUnresolvedReferences
    return {translator[start]: {translator[stop]: list(map(path_to_keys, paths))
                                for stop, paths in stops.items()}
            for start, stops in nx.all_pairs_all_shortest_paths(g)}


def resolve(code: str, robots: int) -> int:
    num_keypad_key_paths = get_num_keypad_key_paths()
    dir_keypad_key_paths = get_dir_keypad_key_paths()

    @cache
    def min_keys(keys: str, robot: int = 0) -> int:
        if robot == robots:
            return len(keys)

        min_keys_ = float('inf')
        stack = {(0, keys, '')}

        while stack:
            i, keys, next_keys = stack.pop()

            if i == len(keys):
                min_keys_ = min(min_keys_, sum(min_keys(keys_ + 'A', robot + 1)
                                               for keys_ in next_keys.split('A')[:-1]))
            else:
                for next_keys_ in dir_keypad_key_paths['A' if i == 0 else keys[i - 1]][keys[i]]:
                    stack.add((i + 1, keys, next_keys + next_keys_))

        return min_keys_

    return sum(min(map(min_keys, num_keypad_key_paths[int(digit_1, 16)][int(digit_2, 16)]))
               for digit_1, digit_2 in pairwise(chain('A', code))) * int(code[:-1])


if __name__ == '__main__':
    main()
