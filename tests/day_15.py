from pytest import mark, param

from aoc.day_15 import parse_grid, part_1, part_2

SMALLER_EXAMPLE = '''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''.lstrip()

LARGER_EXAMPLE = '''
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''.lstrip()


@mark.parametrize('example, result', [param(SMALLER_EXAMPLE, 2028, id='smaller_example'),
                                      param(LARGER_EXAMPLE, 10092, id='larger_example')])
def test_part_1(example: str, result: int):
    raw_grid, raw_moves = example.split('\n\n')
    grid, robot = parse_grid(raw_grid)
    moves = ''.join(raw_moves.splitlines())

    assert part_1(grid, moves, robot) == result


@mark.parametrize('example, result', [param(LARGER_EXAMPLE, 9021, id='larger_example')])
def test_part_2(example: str, result: int):
    raw_grid, raw_moves = example.split('\n\n')
    grid, robot = parse_grid(raw_grid)
    moves = ''.join(raw_moves.splitlines())

    assert part_2(grid, moves, robot) == result
