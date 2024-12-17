def main():
    a = int(input().split(': ')[-1])
    input()
    input()
    input()
    program = list(map(int, input().split(': ')[-1].split(',')))

    print(*map(str, part_1(a, program)), sep=',')
    print(part_2(program))


def part_1(a: int, program: list[int]) -> list[int]:
    b = 0
    c = 0
    i = 0
    output = []

    while i < len(program):
        literal_operand = program[i + 1]
        match program[i + 1]:
            case 4:
                combo_operand = a
            case 5:
                combo_operand = b
            case 5:
                combo_operand = c
            case _:
                combo_operand = literal_operand

        match program[i]:
            case 0:
                a = a // 2 ** combo_operand
            case 1:
                b ^= literal_operand
            case 2:
                b = combo_operand % 8
            case 3:
                if a != 0:
                    i = literal_operand
                    continue
            case 4:
                b ^= c
            case 5:
                output.append(combo_operand % 8)
            case 6:
                b = a // 2 ** combo_operand
            case 7:
                c = a // 2 ** combo_operand

        i += 2

    return output


def part_2(program: list[int]) -> int:
    start = 0 if len(program) == 1 else 8 ** (len(program) - 1)
    stop = 8 ** len(program)
    ranges = [(range(start, stop, (stop - start) // 7), len(program) - 1)]
    a_min = float('inf')
    aaa = 0

    while ranges:
        range_, i = ranges.pop()

        for a in range_:
            program_ = part_1(a, program)

            if program_[i] == program[i]:
                aaa += 1
                if program_ == program:
                    a_min = min(a_min, a)
                else:
                    ranges.append((range(a, a + range_.step, range_.step // 8), i - 1))

    return int(a_min)


if __name__ == '__main__':
    main()
