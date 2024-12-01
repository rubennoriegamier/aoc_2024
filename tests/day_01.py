from pytest import fixture

from aoc.day_01 import parse_pair, part_1, part_2, transpose


@fixture
def raw_pairs() -> list[str]:
    return ['3   4\n',
            '4   3\n',
            '2   5\n',
            '1   3\n',
            '3   9\n',
            '3   3\n']


@fixture
def pairs() -> list[tuple[int, int]]:
    return [(3, 4),
            (4, 3),
            (2, 5),
            (1, 3),
            (3, 9),
            (3, 3)]


@fixture
def left() -> list[int]:
    return [3, 4, 2, 1, 3, 3]


@fixture
def right() -> list[int]:
    return [4, 3, 5, 3, 9, 3]


def test_parse_pair(raw_pairs, pairs):
    assert list(map(parse_pair, raw_pairs)) == pairs


def test_transpose(pairs, left, right):
    assert transpose(pairs) == (left, right)


def test_part_1(left, right):
    assert part_1(left, right) == 11


def test_part_2(left, right):
    assert part_2(left, right) == 31
