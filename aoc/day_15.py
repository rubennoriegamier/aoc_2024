import fileinput
from copy import deepcopy

DIRECTIONS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def main():
    raw_grid, raw_moves = ''.join(fileinput.input()).split('\n\n')
    grid, robot = parse_grid(raw_grid)
    moves = ''.join(raw_moves.splitlines())

    print(part_1(grid, moves, robot))
    print(part_2(grid, moves, robot))


def parse_grid(raw_grid: str) -> tuple[list[list[str]], tuple[int, int]]:
    grid = []
    robot = -1, -1

    for y, line in enumerate(raw_grid.splitlines()):
        grid.append([])
        for x, tile in enumerate(line):
            if tile == '@':
                robot = y, x
                grid[-1].append('.')
            else:
                grid[-1].append(tile)

    return grid, robot


def part_1(grid: list[list[str]], moves: str, robot: tuple[int, int]) -> int:
    grid = deepcopy(grid)
    robot_y, robot_x = robot

    for move in moves:
        y_offset, x_offset = DIRECTIONS[move]
        new_robot_y = robot_y + y_offset
        new_robot_x = robot_x + x_offset

        match grid[new_robot_y][new_robot_x]:
            case '.':
                robot_y = new_robot_y
                robot_x = new_robot_x
            case 'O':
                hole_y = new_robot_y + y_offset
                hole_x = new_robot_x + x_offset

                while True:
                    match grid[hole_y][hole_x]:
                        case '.':
                            grid[hole_y][hole_x], grid[new_robot_y][new_robot_x] = \
                                grid[new_robot_y][new_robot_x], grid[hole_y][hole_x]
                            robot_y = new_robot_y
                            robot_x = new_robot_x
                            break
                        case '#':
                            break
                    hole_y += y_offset
                    hole_x += x_offset

    return sum(y * 100 + x
               for y, line in enumerate(grid)
               for x, tile in enumerate(line)
               if tile == 'O')


def part_2(grid: list[list[str]], moves: str, robot: tuple[int, int]) -> int:
    grid_ = []
    for y, line in enumerate(grid):
        grid_.append([])
        for x, tile in enumerate(line):
            match tile:
                case '.':
                    grid_[-1].append('.')
                    grid_[-1].append('.')
                case '#':
                    grid_[-1].append('#')
                    grid_[-1].append('#')
                case 'O':
                    grid_[-1].append('[')
                    grid_[-1].append(']')
    grid = grid_
    robot_y, robot_x = robot
    robot_x *= 2

    def can_move(y_: int, x_: int, y_offset: int) -> bool:
        match grid[y_][x_]:
            case '.':
                return True
            case '#':
                return False
            case '[':
                return can_move(y_ + y_offset, x_, y_offset) and can_move(y_ + y_offset, x_ + 1, y_offset)
            case ']':
                return can_move(y_ + y_offset, x_, y_offset) and can_move(y_ + y_offset, x_ - 1, y_offset)

    def move_(y_: int, x_: int, y_offset: int) -> None:
        match grid[y_][x_]:
            case '[':
                move_(y_ + y_offset, x_, y_offset)
                grid[y_][x_], grid[y_ + y_offset][x_] = grid[y_ + y_offset][x_], grid[y_][x_]
                move_(y_, x_ + 1, y_offset)
            case ']':
                move_(y_ + y_offset, x_, y_offset)
                grid[y_][x_], grid[y_ + y_offset][x_] = grid[y_ + y_offset][x_], grid[y_][x_]
                move_(y_, x_ - 1, y_offset)

    for move in moves:
        match move:
            case '^':
                if can_move(robot_y - 1, robot_x, -1):
                    move_(robot_y - 1, robot_x, -1)
                    robot_y -= 1
            case '>':
                hole_x = robot_x + 1
                while grid[robot_y][hole_x] != '#':
                    if grid[robot_y][hole_x] == '.':
                        grid[robot_y][robot_x + 1:hole_x + 1] = grid[robot_y][robot_x:hole_x]
                        robot_x += 1
                        break
                    hole_x += 1
            case 'v':
                if can_move(robot_y + 1, robot_x, 1):
                    move_(robot_y + 1, robot_x, 1)
                    robot_y += 1
            case '<':
                hole_x = robot_x - 1
                while grid[robot_y][hole_x] != '#':
                    if grid[robot_y][hole_x] == '.':
                        grid[robot_y][hole_x:robot_x] = grid[robot_y][hole_x + 1:robot_x + 1]
                        robot_x -= 1
                        break
                    hole_x -= 1

    return sum(y * 100 + x
               for y, line in enumerate(grid)
               for x, tile in enumerate(line)
               if tile == '[')


if __name__ == '__main__':
    main()
