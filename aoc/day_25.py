import fileinput
from functools import partial
from operator import add, ge


def main():
    doors_and_keys = [door_or_key.splitlines()
                      for door_or_key in ''.join(fileinput.input()).split('\n\n')]

    print(part_1(doors_and_keys))


def part_1(door_and_keys: list[list[str]]) -> int:
    doors = []
    keys = []
    pairs = 0

    for i, door_or_key in enumerate(door_and_keys):
        pattern = [0, 0, 0, 0, 0]

        if door_or_key[0] == '#####':
            for y, line in enumerate(door_or_key[1:], 1):
                for x, tile in enumerate(line):
                    if tile == '#':
                        pattern[x] = y
            doors.append(pattern)
        else:
            # Key
            for y, line in enumerate(door_or_key[-2::-1], 1):
                for x, tile in enumerate(line):
                    if tile == '#':
                        pattern[x] = y
            keys.append(pattern)

    ge_5 = partial(ge, 5)

    for door in doors:
        for key in keys:
            if all(map(ge_5, map(add, door, key))):
                pairs += 1

    return pairs


if __name__ == '__main__':
    main()
