from pytest import fixture

from aoc.day_11 import part_1


@fixture
def stones() -> list[int]:
    return [125, 17]


def test_part_1(stones):
    assert part_1(25, stones) == 55_312
