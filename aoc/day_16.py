import fileinput
from itertools import chain, pairwise
from operator import itemgetter

import networkx as nx


def main():
    grid = list(map(str.rstrip, fileinput.input()))
    grid = fill_dead_ends(grid)

    print(*part_1_and_2(grid), sep='\n')


def fill_dead_ends(grid: list[str]) -> list[str]:
    # noinspection PyTypeChecker
    grid = list(map(list, grid))
    candidates = {(y, x)
                  for y, line in enumerate(grid)
                  for x, tile in enumerate(line)
                  if tile == '.'}

    while candidates:
        y, x = candidates.pop()
        walls = 0
        escape = None

        for y_offset, x_offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if grid[y + y_offset][x + x_offset] == '#':
                walls += 1
            else:
                escape = y + y_offset, x + x_offset
        if walls == 3 and grid[y][x] not in 'SE':
            grid[y][x] = '#'
            candidates.add(escape)

    return list(map(''.join, grid))


def build_graph(grid: list[str]) -> tuple[nx.DiGraph, tuple[int, int, int], tuple[int, int, int]]:
    edges = []
    start = -1, -1, -1
    end = -1, -1, -1

    for y, line in enumerate(grid):
        for x, tile in enumerate(line):
            if tile != '#':
                up = y, x, 0
                ri = y, x, 1
                do = y, x, 2
                le = y, x, 3

                if grid[y - 1][x] != '#':
                    edges.append((up, (y - 1, x, 0), 1))
                    edges.append((ri, up, 1_000))
                    edges.append((le, up, 1_000))
                if grid[y][x + 1] != '#':
                    edges.append((ri, (y, x + 1, 1), 1))
                    edges.append((up, ri, 1_000))
                    edges.append((do, ri, 1_000))
                if grid[y + 1][x] != '#':
                    edges.append((do, (y + 1, x, 2), 1))
                    edges.append((ri, do, 1_000))
                    edges.append((le, do, 1_000))
                if grid[y][x - 1] != '#':
                    edges.append((le, (y, x - 1, 3), 1))
                    edges.append((up, le, 1_000))
                    edges.append((do, le, 1_000))

                if tile == 'S':
                    start = y, x, 1
                elif tile == 'E':
                    end = y, x, 4
                    edges.append((up, end, 0))
                    edges.append((ri, end, 0))
                    edges.append((do, end, 0))
                    edges.append((le, end, 0))

    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges)

    return graph, start, end


def part_1(grid: list[str]) -> int:
    graph, start, end = build_graph(grid)

    return nx.shortest_path_length(graph, start, end, weight='weight')


def part_2(grid: list[str]) -> int:
    graph, start, end = build_graph(grid)
    paths = nx.all_shortest_paths(graph, start, end, weight='weight')

    # noinspection PyTypeChecker
    return len(set(map(itemgetter(0, 1), chain.from_iterable(paths))))


def part_1_and_2(grid: list[str]) -> tuple[int, int]:
    graph, start, end = build_graph(grid)
    paths = list(nx.all_shortest_paths(graph, start, end, weight='weight'))
    part_1_ = sum(1 if a == b else 1_000 for a, b in pairwise(map(itemgetter(2), paths[0]))) - 1_000
    # noinspection PyTypeChecker
    part_2_ = len(set(map(itemgetter(0, 1), chain.from_iterable(paths))))

    return part_1_, part_2_


if __name__ == '__main__':
    main()
