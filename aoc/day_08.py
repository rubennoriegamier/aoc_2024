import fileinput
from collections import defaultdict
from itertools import combinations, count


def main():
    grid = list(map(str.rstrip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


def part_1(grid: list[str]) -> int:
    antennas = defaultdict(list)
    antinodes = set()

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell != '.':
                antennas[cell].append((y, x))

    for frequency, frequency_antennas in antennas.items():
        for (y_1, x_1), (y_2, x_2) in combinations(frequency_antennas, 2):
            if 0 <= (y_3 := y_1 + y_1 - y_2) < len(grid) and 0 <= (x_3 := x_1 + x_1 - x_2) < len(grid[0]):
                antinodes.add((y_3, x_3))
            if 0 <= (y_3 := y_2 + y_2 - y_1) < len(grid) and 0 <= (x_3 := x_2 + x_2 - x_1) < len(grid[0]):
                antinodes.add((y_3, x_3))

    return len(antinodes)


def part_2(grid: list[str]) -> int:
    antennas = defaultdict(list)
    antinodes = set()

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell != '.':
                antennas[cell].append((y, x))

    for frequency, frequency_antennas in antennas.items():
        for (y_1, x_1), (y_2, x_2) in combinations(frequency_antennas, 2):
            antinodes.add((y_1, x_1))
            antinodes.add((y_2, x_2))
            for y_1_, x_1_, y_2_, x_2_ in [(y_1, x_1, y_2, x_2), (y_2, x_2, y_1, x_1)]:
                for y_3, x_3 in zip(count(y_1_ + y_1_ - y_2_, y_1_ - y_2_), count(x_1_ + x_1_ - x_2_, x_1_ - x_2_)):
                    if 0 <= y_3 < len(grid) and 0 <= x_3 < len(grid[0]):
                        antinodes.add((y_3, x_3))
                    else:
                        break

    return len(antinodes)


if __name__ == '__main__':
    main()
