from pytest import fixture

from aoc.day_08 import part_1, part_2


@fixture
def grid() -> list[str]:
    return ['............',
            '........0...',
            '.....0......',
            '.......0....',
            '....0.......',
            '......A.....',
            '............',
            '............',
            '........A...',
            '.........A..',
            '............',
            '............']


def test_part_1(grid):
    assert part_1(grid) == 14


def test_part_2(grid):
    assert part_2(grid) == 34
