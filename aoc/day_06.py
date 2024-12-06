import fileinput
from collections import deque
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
    move_y = deque([-1, 0, 1, 0])
    move_x = deque([0, -1, 0, 1])
    positions = {guard}

    while True:
        next_guard = guard[0] + move_y[0], guard[1] + move_x[0]

        if 0 <= next_guard[0] < len(grid) and 0 <= next_guard[1] < len(grid[0]):
            if grid[next_guard[0]][next_guard[1]]:
                move_y.rotate()
                move_x.rotate()
            else:
                guard = next_guard
                positions.add(guard)
        else:
            return len(positions)


def part_2(grid: list[list[bool]], guard: tuple[int, int]) -> int:
    move_y = deque([-1, 0, 1, 0])
    move_x = deque([0, -1, 0, 1])
    positions = {guard}
    positions_with_moves = {(guard[0], guard[1], move_y[0], move_x[0])}
    obstructions = 0

    while True:
        next_guard = guard[0] + move_y[0], guard[1] + move_x[0]

        if 0 <= next_guard[0] < len(grid) and 0 <= next_guard[1] < len(grid[0]):
            if grid[next_guard[0]][next_guard[1]]:
                move_y.rotate()
                move_x.rotate()
                positions_with_moves.add((guard[0], guard[1], move_y[0], move_x[0]))
            else:
                if next_guard not in positions:
                    # BEGIN OBSTRUCTION
                    grid[next_guard[0]][next_guard[1]] = True

                    move_y_ = move_y.copy()
                    move_x_ = move_x.copy()
                    positions_with_moves_ = set()

                    while True:
                        next_guard_ = guard[0] + move_y_[0], guard[1] + move_x_[0]

                        if 0 <= next_guard_[0] < len(grid) and 0 <= next_guard_[1] < len(grid[0]):
                            if grid[next_guard_[0]][next_guard_[1]]:
                                move_y_.rotate()
                                move_x_.rotate()

                                next_position_with_move = guard[0], guard[1], move_y_[0], move_x_[0]

                                if next_position_with_move in positions_with_moves \
                                        or next_position_with_move in positions_with_moves_:
                                    obstructions += 1
                                    break
                                positions_with_moves_.add(next_position_with_move)
                            else:
                                guard = next_guard_
                                next_position_with_move = guard[0], guard[1], move_y_[0], move_x_[0]

                                if next_position_with_move in positions_with_moves \
                                        or next_position_with_move in positions_with_moves_:
                                    obstructions += 1
                                    break
                                positions_with_moves_.add(next_position_with_move)
                        else:
                            break

                    grid[next_guard[0]][next_guard[1]] = False
                    # END OBSTRUCTION

                guard = next_guard
                positions.add(guard)
                positions_with_moves.add((guard[0], guard[1], move_y[0], move_x[0]))
        else:
            return obstructions


if __name__ == '__main__':
    main()
