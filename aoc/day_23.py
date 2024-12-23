import fileinput
from collections import defaultdict
from itertools import chain


def main():
    # noinspection PyTypeChecker
    edges: list[tuple[str, str]] = [tuple(line.rstrip().split('-')) for line in fileinput.input()]

    print(part_1(edges))
    print(part_2(edges))


def part_1(edges: list[tuple[str, str]]) -> int:
    connections = defaultdict(list)
    triplets = set()

    for comp_1, comp_2 in edges:
        connections[comp_1].append(comp_2)
        connections[comp_2].append(comp_1)

    for comp_1, comps_2 in connections.items():
        if comp_1[0] == 't':
            for comp_2 in comps_2:
                for comp_3 in connections[comp_2]:
                    if comp_3 in connections[comp_1]:
                        triplets.add(tuple(sorted([comp_1, comp_2, comp_3])))

    return len(triplets)


def part_2(edges: list[tuple[str, str]]) -> str:
    connections = defaultdict(set)

    for comp_1, comp_2 in edges:
        connections[comp_1].add(comp_2)
        connections[comp_2].add(comp_1)

    networks = {tuple(sorted(pair)) for pair in edges}

    while len(networks) > 1:
        networks_ = set()

        for network in networks:
            candidates = None

            for computer in network:
                if candidates is None:
                    candidates = connections[computer].copy()
                else:
                    candidates.intersection_update(connections[computer])
                    if not candidates:
                        break
            else:
                networks_.update(tuple(sorted(chain(network, [candidate])))
                                 for candidate in candidates)

        networks = networks_

    return ','.join(sorted(networks.pop()))


if __name__ == '__main__':
    main()
