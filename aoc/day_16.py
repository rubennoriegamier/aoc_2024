import fileinput
from itertools import chain
from operator import itemgetter

import networkx as nx


def main():
    grid = list(map(str.rstrip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


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

                edges.append((up, ri, 1_000))
                edges.append((ri, up, 1_000))
                edges.append((ri, do, 1_000))
                edges.append((do, ri, 1_000))
                edges.append((do, le, 1_000))
                edges.append((le, do, 1_000))
                edges.append((le, up, 1_000))
                edges.append((up, le, 1_000))

                if grid[y - 1][x] != '#':
                    edges.append((up, (y - 1, x, 0), 1))
                if grid[y][x + 1] != '#':
                    edges.append((ri, (y, x + 1, 1), 1))
                if grid[y + 1][x] != '#':
                    edges.append((do, (y + 1, x, 2), 1))
                if grid[y][x - 1] != '#':
                    edges.append((le, (y, x - 1, 3), 1))

                if tile == 'S':
                    start = y, x, 1
                elif tile == 'E':
                    end = y, x, 4
                    edges.append((up, (y, x, 4), 0))
                    edges.append((ri, (y, x, 4), 0))
                    edges.append((do, (y, x, 4), 0))
                    edges.append((le, (y, x, 4), 0))

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


if __name__ == '__main__':
    main()
