from pytest import fixture

from aoc.day_12 import part_1, part_2


@fixture
def garden() -> list[str]:
    return ['RRRRIICCFF',
            'RRRRIICCCF',
            'VVRRRCCFFF',
            'VVRCCCJFFF',
            'VVVVCJJCFE',
            'VVIVCCJJEE',
            'VVIIICJJEE',
            'MIIIIIJJEE',
            'MIIISIJEEE',
            'MMMISSJEEE']


def test_part_1(garden):
    assert part_1(garden) == 1930


def test_part_2(garden):
    assert part_2(garden) == 1206
