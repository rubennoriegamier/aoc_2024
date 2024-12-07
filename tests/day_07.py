from pytest import fixture

from aoc.day_07 import Equation, part_1, part_2


@fixture
def equations() -> list[Equation]:
    return list(map(Equation.parse, ['190: 10 19',
                                     '3267: 81 40 27',
                                     '83: 17 5',
                                     '156: 15 6',
                                     '7290: 6 8 6 15',
                                     '161011: 16 10 13',
                                     '192: 17 8 14',
                                     '21037: 9 7 18 13',
                                     '292: 11 6 16 20']))


def test_part_1(equations):
    assert part_1(equations) == 3749


def test_part_2(equations):
    assert part_2(equations) == 11387
