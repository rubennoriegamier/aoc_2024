from pytest import fixture

from aoc.day_10 import part_1, part_2


@fixture
def top_map() -> list[list[int]]:
    return [[8, 9, 0, 1, 0, 1, 2, 3],
            [7, 8, 1, 2, 1, 8, 7, 4],
            [8, 7, 4, 3, 0, 9, 6, 5],
            [9, 6, 5, 4, 9, 8, 7, 4],
            [4, 5, 6, 7, 8, 9, 0, 3],
            [3, 2, 0, 1, 9, 0, 1, 2],
            [0, 1, 3, 2, 9, 8, 0, 1],
            [1, 0, 4, 5, 6, 7, 3, 2]]


def test_part_1(top_map):
    assert part_1(top_map) == 36


def test_part_2(top_map):
    assert part_2(top_map) == 81
