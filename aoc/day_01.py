import fileinput
from collections import Counter
from collections.abc import Iterable
from operator import mul, sub


def main() -> None:
    left, right = transpose(map(parse_pair, fileinput.input()))

    print(part_1(left, right))
    print(part_2(left, right))


def parse_pair(raw_pair: str) -> tuple[int, int]:
    # noinspection PyTypeChecker
    return tuple(map(int, raw_pair.split()))


def transpose(pairs: Iterable[tuple[int, int]]) -> tuple[list[int], list[int]]:
    # noinspection PyTypeChecker
    return tuple(map(list, zip(*pairs)))


def part_1(left: Iterable[int], right: Iterable[int]) -> int:
    return sum(map(abs, map(sub, sorted(left), sorted(right))))


def part_2(left: Iterable[int], right: Iterable[int]) -> int:
    return sum(map(mul, left, map(Counter(right).__getitem__, left)))


if __name__ == '__main__':
    main()
