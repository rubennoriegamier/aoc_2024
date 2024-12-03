import fileinput
import re


def main():
    memory = ''.join(fileinput.input())

    print(part_1(memory))
    print(part_2(memory))


def part_1(memory: str) -> int:
    return sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', memory))


def part_2(memory: str) -> int:
    enabled = True
    result = 0

    for a, b, switch in re.findall(r'mul\((\d+),(\d+)\)|(do\(\)|don\'t\(\))', memory):
        if switch == 'do()':
            enabled = True
        elif switch == 'don\'t()':
            enabled = False
        elif enabled:
            result += int(a) * int(b)

    return result


if __name__ == '__main__':
    main()
