from aoc.day_19 import part_1_and_2

PATTERNS = ['r',
            'wr',
            'b',
            'g',
            'bwu',
            'rb',
            'gb',
            'br']
TOWELS = ['brwrr',
          'bggr',
          'gbbr',
          'rrbgbr',
          'ubwu',
          'bwurrg',
          'brgr',
          'bbrgwb']


def test_part_1():
    assert part_1_and_2(PATTERNS, TOWELS)[0] == 6


def test_part_2():
    assert part_1_and_2(PATTERNS, TOWELS)[1] == 16
