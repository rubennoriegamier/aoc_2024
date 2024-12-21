from pytest import mark

from aoc.day_21 import resolve


@mark.parametrize('code, length', [('029A', 68 * 29), ('980A', 60 * 980), ('179A', 68 * 179),
                                   ('456A', 64 * 456), ('379A', 64 * 379)])
def test_resolve(code: str, length: int):
    assert resolve(code, 2) == length
