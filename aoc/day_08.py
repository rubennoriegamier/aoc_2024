import fileinput
from collections import defaultdict
from itertools import count, permutations


def main():
    grid = list(map(str.rstrip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


def part_1(grid: list[str]) -> int:
    antennas = defaultdict(list)

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell != '.':
                antennas[cell].append((y, x))

    # noinspection PyUnboundLocalVariable
    return len({(y_3, x_3)
                for frequency, frequency_antennas in antennas.items()
                for (y_1, x_1), (y_2, x_2) in permutations(frequency_antennas, 2)
                if 0 <= (y_3 := y_1 + y_1 - y_2) < len(grid) and 0 <= (x_3 := x_1 + x_1 - x_2) < len(grid[0])})


def part_2(grid: list[str]) -> int:
    antennas = defaultdict(list)
    antinodes = set()

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell != '.':
                antennas[cell].append((y, x))

    for frequency, frequency_antennas in antennas.items():
        for (y_1, x_1), (y_2, x_2) in permutations(frequency_antennas, 2):
            antinodes.add((y_1, x_1))
            antinodes.add((y_2, x_2))
            for y_3, x_3 in zip(count(y_1 + y_1 - y_2, y_1 - y_2), count(x_1 + x_1 - x_2, x_1 - x_2)):
                if 0 <= y_3 < len(grid) and 0 <= x_3 < len(grid[0]):
                    antinodes.add((y_3, x_3))
                else:
                    break

    return len(antinodes)


if __name__ == '__main__':
    main()
