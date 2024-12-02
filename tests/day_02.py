import pytest

from aoc.day_02 import is_safe_1, is_safe_2


@pytest.mark.parametrize('report, result', [
    pytest.param([7, 6, 4, 2, 1], True, id='safe because the levels are all decreasing by 1 or 2'),
    pytest.param([1, 2, 7, 8, 9], False, id='unsafe because 2 7 is an increase of 5'),
    pytest.param([9, 7, 6, 2, 1], False, id='unsafe because 6 2 is a decrease of 4'),
    pytest.param([1, 3, 2, 4, 5], False, id='unsafe because 1 3 is increasing but 3 2 is decreasing'),
    pytest.param([8, 6, 4, 4, 1], False, id='unsafe because 4 4 is neither an increase or a decrease'),
    pytest.param([1, 3, 6, 7, 9], True, id='safe because the levels are all increasing by 1, 2, or 3')
])
def test_is_safe_1(report, result):
    # noinspection PyTypeChecker
    assert is_safe_1(report) == result


@pytest.mark.parametrize('report, result', [
    pytest.param([7, 6, 4, 2, 1], True, id='safe without removing any level'),
    pytest.param([1, 2, 7, 8, 9], False, id='unsafe regardless of which level is removed'),
    pytest.param([9, 7, 6, 2, 1], False, id='unsafe regardless of which level is removed'),
    pytest.param([1, 3, 2, 4, 5], True, id='safe by removing the second level, 3'),
    pytest.param([8, 6, 4, 4, 1], True, id='safe by removing the third level, 4'),
    pytest.param([1, 3, 6, 7, 9], True, id='safe without removing any level')
])
def test_is_safe_2(report, result):
    # noinspection PyTypeChecker
    assert is_safe_2(report) == result
