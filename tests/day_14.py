from pytest import fixture

from aoc.day_14 import Robot, part_1


@fixture
def robots() -> list[Robot]:
    return list(map(Robot.parse, ['p=0,4 v=3,-3',
                                  'p=6,3 v=-1,-3',
                                  'p=10,3 v=-1,2',
                                  'p=2,0 v=2,-1',
                                  'p=0,0 v=1,3',
                                  'p=3,0 v=-2,-2',
                                  'p=7,6 v=-1,-3',
                                  'p=3,0 v=-1,-2',
                                  'p=9,3 v=2,3',
                                  'p=7,3 v=-1,2',
                                  'p=2,4 v=2,-3',
                                  'p=9,5 v=-3,-3']))


def test_part_1(robots):
    assert part_1(robots, 100, 11, 7) == 12
