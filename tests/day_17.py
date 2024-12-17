from aoc.day_17 import part_1, part_2


def test_part_1():
    assert part_1(729, [0, 1, 5, 4, 3, 0]) == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]


def test_part_2():
    assert part_2([0, 3, 5, 4, 3, 0]) == 117440
