import fileinput


def main():
    grid = list(map(str.rstrip, fileinput.input()))

    print(part_1(grid, at_least=100))
    print(part_2(grid, at_least=100, max_ps=20))


def grid_with_path(grid: list[str]) -> list[list[int]]:
    start = -1, -1
    grid_ = [[-1] * len(grid[0]) for _ in range(len(grid))]

    for y, line in enumerate(grid):
        for x, tile in enumerate(line):
            if tile != '#':
                if tile == 'S':
                    start = y, x
                    grid_[y][x] = 1
                else:
                    grid_[y][x] = 0

    grid = grid_
    current = start

    while True:
        y, x = current
        for y_, x_ in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]:
            if grid[y_][x_] == 0:
                grid[y_][x_] = grid[y][x] + 1
                current = y_, x_
                break
        else:
            break

    return grid


def part_1(grid: list[str], *, at_least: int) -> int:
    grid = grid_with_path(grid)

    return sum(0 <= y_ < len(grid) and 0 <= x_ < len(grid[0]) and grid[y_][x_] - grid[y][x] - 2 >= at_least
               for y, line in enumerate(grid)
               for x, tile in enumerate(line)
               if tile >= 1
               for y_, x_ in [(y - 2, x), (y, x + 2), (y + 2, x), (y, x - 2)])


def part_2(grid: list[str], *, at_least: int, max_ps: int) -> int:
    grid = grid_with_path(grid)

    return sum(grid[y_][x_] != -1 and grid[y_][x_] - tile - abs(y - y_) - abs(x - x_) >= at_least
               for y, line in enumerate(grid)
               for x, tile in enumerate(line)
               if tile != -1
               for y_ in range(max(y - max_ps, 0), min(y + max_ps + 1, len(grid)))
               for x_ in range(max(x - max_ps + abs(y - y_), 0), min(x + max_ps - abs(y - y_) + 1, len(grid[0]))))


if __name__ == '__main__':
    main()
