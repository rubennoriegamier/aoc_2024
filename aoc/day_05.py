import fileinput
from collections import defaultdict
from itertools import pairwise


def main():
    raw_rules, raw_updates = ''.join(fileinput.input()).split('\n\n')
    rules = [tuple(map(int, raw_rule.split('|')))
             for raw_rule in raw_rules.splitlines()]
    updates = [list(map(int, raw_update.split(',')))
               for raw_update in raw_updates.splitlines()]

    # noinspection PyTypeChecker
    print(part_1(rules, updates))
    # noinspection PyTypeChecker
    print(part_2(rules, updates))


def part_1(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    rules = set(rules)

    return sum(update[len(update) // 2]
               for update in updates
               if all(map(rules.__contains__, pairwise(update))))


def part_2(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    rules = set(rules)
    following = defaultdict(set)

    for curr_page, next_page in rules:
        following[curr_page].add(next_page)

    return sum(next(page
                    for page in update
                    if len(following[page] & set(update)) == len(update) // 2)
               for update in updates
               if not all(map(rules.__contains__, pairwise(update))))


if __name__ == '__main__':
    main()
