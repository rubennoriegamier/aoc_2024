import fileinput
from functools import cache


def main():
    patterns = input().split(', ')
    input()
    towels = list(map(str.rstrip, fileinput.input()))

    print(*part_1_and_2(patterns, towels), sep='\n')


def part_1_and_2(patterns: list[str], towels: list[str]) -> tuple[int, int]:
    patterns = set(patterns)
    pattern_max_len = max(map(len, patterns))

    @cache
    def get_arrangements(towel: str) -> int:
        if towel == '':
            return 1
        return sum(get_arrangements(towel[i:])
                   for i in range(1, min(pattern_max_len, len(towel)) + 1)
                   if towel[:i] in patterns)

    arrangements = list(map(get_arrangements, towels))

    return sum(map(bool, arrangements)), sum(arrangements)


if __name__ == '__main__':
    main()
