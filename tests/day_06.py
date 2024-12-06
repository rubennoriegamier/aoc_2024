from pytest import fixture

from aoc.day_06 import parse_grid, part_1, part_2


@fixture
def grid_and_guard() -> tuple[list[list[bool]], tuple[int, int]]:
    return parse_grid(['....#.....',
                       '.........#',
                       '..........',
                       '..#.......',
                       '.......#..',
                       '..........',
                       '.#..^.....',
                       '........#.',
                       '#.........',
                       '......#...'])


def test_part_1(grid_and_guard):
    assert part_1(*grid_and_guard) == 41


def test_part_2(grid_and_guard):
    assert part_2(*grid_and_guard) == 6
