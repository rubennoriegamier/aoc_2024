import fileinput

import networkx as nx


def main():
    bytes_ = [tuple(map(int, line.split(','))) for line in fileinput.input()]

    # noinspection PyTypeChecker
    print(part_1(bytes_, 71, 1024))
    # noinspection PyTypeChecker
    print(part_2(bytes_, 71, 1024))


def part_1(bytes_: list[tuple[int, int]], size: int, first: int) -> int:
    g = nx.grid_2d_graph(size, size)
    g.remove_nodes_from(bytes_[:first])

    return nx.shortest_path_length(g, (0, 0), (size - 1, size - 1))


def part_2(bytes_: list[tuple[int, int]], size: int, first: int) -> str:
    g = nx.grid_2d_graph(size, size)
    g.remove_nodes_from(bytes_[:first])
    start = 0, 0
    end = size - 1, size - 1

    path = set(nx.shortest_path(g, start, end))

    for byte in bytes_[first:]:
        g.remove_node(byte)
        if byte in path:
            try:
                path = set(nx.shortest_path(g, start, end))
            except nx.NetworkXNoPath:
                return f'{byte[0]},{byte[1]}'


if __name__ == '__main__':
    main()
