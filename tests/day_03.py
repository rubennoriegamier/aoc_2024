from aoc.day_03 import part_1, part_2


def test_part_1():
    assert part_1('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))') == 161

def test_part_2():
    assert part_2('xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))') == 48