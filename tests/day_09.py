from pytest import fixture

from aoc.day_09 import part_1, part_2


@fixture
def disk_map() -> list[int]:
    return list(map(int, '2333133121414131402'))


def test_part_1(disk_map):
    assert part_1(disk_map) == 1928


def test_part_2(disk_map):
    assert part_2(disk_map) == 2858
