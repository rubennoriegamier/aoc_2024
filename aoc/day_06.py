import fileinput
from collections.abc import Iterable


def main():
    grid, guard = parse_grid(map(str.rstrip, fileinput.input()))

    print(part_1(grid, guard))
    print(part_2(grid, guard))


def parse_grid(raw_grid: Iterable[str]) -> tuple[list[list[bool]], tuple[int, int]]:
    grid = []
    guard = None

    for y, row in enumerate(raw_grid):
        grid.append([])

        for x, cell in enumerate(row):
            if cell == '^':
                guard = y, x
            grid[-1].append(cell == '#')

    return grid, guard


def part_1(grid: list[list[bool]], guard: tuple[int, int]) -> int:
    guard_y, guard_x = guard
    move_y = [-1, 0, 1, 0]
    move_x = [0, 1, 0, -1]
    move_i = 0
    positions = {guard}

    while True:
        next_guard_y = guard_y + move_y[move_i]
        next_guard_x = guard_x + move_x[move_i]

        if 0 <= next_guard_y < len(grid) and 0 <= next_guard_x < len(grid[0]):
            if grid[next_guard_y][next_guard_x]:
                move_i = (move_i + 1) % 4
            else:
                guard_y = next_guard_y
                guard_x = next_guard_x
                positions.add((guard_y, guard_x))
        else:
            return len(positions)


def part_2(grid: list[list[bool]], guard: tuple[int, int]) -> int:
    guard_y, guard_x = guard
    move_y = [-1, 0, 1, 0]
    move_x = [0, 1, 0, -1]
    move_i = 0
    path = {guard}
    turns = set()
    obstructions = 0

    while True:
        next_guard_y = guard_y + move_y[move_i]
        next_guard_x = guard_x + move_x[move_i]

        if 0 <= next_guard_y < len(grid) and 0 <= next_guard_x < len(grid[0]):
            if grid[next_guard_y][next_guard_x]:
                move_i = (move_i + 1) % 4
                turns.add((guard_y, guard_x, move_y[move_i], move_x[move_i]))
            else:
                if (next_guard_y, next_guard_x) not in path:
                    # BEGIN OBSTRUCTION
                    grid[next_guard_y][next_guard_x] = True

                    move_i_ = move_i
                    turns_ = turns.copy()

                    while True:
                        next_guard_y_ = guard_y + move_y[move_i_]
                        next_guard_x_ = guard_x + move_x[move_i_]

                        if 0 <= next_guard_y_ < len(grid) and 0 <= next_guard_x_ < len(grid[0]):
                            if grid[next_guard_y_][next_guard_x_]:
                                move_i_ = (move_i_ + 1) % 4

                                if (turn := (guard_y, guard_x, move_y[move_i_], move_x[move_i_])) in turns_:
                                    obstructions += 1
                                    break
                                turns_.add(turn)
                            else:
                                guard_y = next_guard_y_
                                guard_x = next_guard_x_
                        else:
                            break

                    grid[next_guard_y][next_guard_x] = False
                    # END OBSTRUCTION

                guard_y = next_guard_y
                guard_x = next_guard_x
                path.add((guard_y, guard_x))
        else:
            return obstructions


if __name__ == '__main__':
    main()
