import fileinput
from itertools import pairwise, starmap
from operator import sub


def main():
    reports = [list(map(int, raw_report.split())) for raw_report in fileinput.input()]

    print(part_1(reports))
    print(part_2(reports))


def is_safe_1(report: list[int]) -> bool:
    diffs = list(starmap(sub, pairwise(report)))

    return all(map(range(-3, 0).__contains__, diffs)) or all(map(range(1, 4).__contains__, diffs))


def is_safe_2(report: list[int]) -> bool:
    return is_safe_1(report) or any(is_safe_1(report[:i] + report[i + 1:]) for i in range(len(report)))


def part_1(reports: list[list[int]]) -> int:
    return sum(map(is_safe_1, reports))


def part_2(reports: list[list[int]]) -> int:
    return sum(map(is_safe_2, reports))


if __name__ == '__main__':
    main()
