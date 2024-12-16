from pytest import mark, param

from aoc.day_16 import part_1, part_2

FIRST_EXAMPLE = '''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''.lstrip()

SECONDS_EXAMPLE = '''
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''.lstrip()


@mark.parametrize('example, result', [param(FIRST_EXAMPLE, 7036, id='first_example'),
                                      param(SECONDS_EXAMPLE, 11048, id='second_example')])
def test_part_1(example: str, result: int):
    assert part_1(example.splitlines()) == result


@mark.parametrize('example, result', [param(FIRST_EXAMPLE, 45, id='first_example'),
                                      param(SECONDS_EXAMPLE, 64, id='second_example')])
def test_part_2(example: str, result: int):
    assert part_2(example.splitlines()) == result
