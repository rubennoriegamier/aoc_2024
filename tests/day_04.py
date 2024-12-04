from pytest import fixture

from aoc.day_04 import part_1, part_2


@fixture
def sample() -> list[str]:
    return ['MMMSXXMASM',
            'MSAMXMSMSA',
            'AMXSXMAAMM',
            'MSAMASMSMX',
            'XMASAMXAMM',
            'XXAMMXXAMA',
            'SMSMSASXSS',
            'SAXAMASAAA',
            'MAMMMXMMMM',
            'MXMXAXMASX']


def test_part_1(sample):
    assert part_1(sample) == 18


def test_part_2(sample):
    assert part_2(sample) == 9
