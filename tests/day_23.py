from aoc.day_23 import part_1, part_2

EDGES = [('kh', 'tc'),
         ('qp', 'kh'),
         ('de', 'cg'),
         ('ka', 'co'),
         ('yn', 'aq'),
         ('qp', 'ub'),
         ('cg', 'tb'),
         ('vc', 'aq'),
         ('tb', 'ka'),
         ('wh', 'tc'),
         ('yn', 'cg'),
         ('kh', 'ub'),
         ('ta', 'co'),
         ('de', 'co'),
         ('tc', 'td'),
         ('tb', 'wq'),
         ('wh', 'td'),
         ('ta', 'ka'),
         ('td', 'qp'),
         ('aq', 'cg'),
         ('wq', 'ub'),
         ('ub', 'vc'),
         ('de', 'ta'),
         ('wq', 'aq'),
         ('wq', 'vc'),
         ('wh', 'yn'),
         ('ka', 'de'),
         ('kh', 'ta'),
         ('co', 'tc'),
         ('wh', 'qp'),
         ('tb', 'vc'),
         ('td', 'yn')]


def test_part_1():
    assert part_1(EDGES) == 7


def test_part_2():
    assert part_2(EDGES) == 'co,de,ka,ta'
