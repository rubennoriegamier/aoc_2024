from pytest import fixture

from aoc.day_13 import Game


@fixture
def sample_1() -> Game:
    return Game.parse('''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400'''.lstrip())


@fixture
def sample_2() -> Game:
    return Game.parse('''
Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176'''.lstrip())


def test_part_1(sample_1):
    assert sample_1.play() == 280


def test_part_1_is_none(sample_2):
    assert sample_2.play() is None


def test_part_2(sample_2):
    assert sample_2.play(10_000_000_000_000) == 459236326669


def test_part_2_is_none(sample_1):
    assert sample_1.play(10_000_000_000_000) is None
