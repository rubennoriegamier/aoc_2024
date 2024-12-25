from aoc.day_25 import part_1

DOORS_AND_KEYS = '''
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''.lstrip()


def test_part_1():
    doors_and_keys = [door_or_key.splitlines()
                      for door_or_key in DOORS_AND_KEYS.split('\n\n')]

    assert part_1(doors_and_keys) == 3
