import fileinput


def main():
    words = list(map(str.rstrip, fileinput.input()))

    print(part_1(words))
    print(part_2(words))


def part_1(words: list[str]) -> int:
    result = 0

    for y, line in enumerate(words):
        for x, curr_char in enumerate(line):
            if curr_char == 'X':
                for mov_y, mov_x in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    y_ = y
                    x_ = x

                    for next_char in 'MAS':
                        y_ += mov_y
                        x_ += mov_x
                        if y_ < 0 or y_ == len(words) or x_ < 0 or x_ == len(line) or words[y_][x_] != next_char:
                            break
                    else:
                        result += 1

    return result


def part_2(words: list[str]) -> int:
    return sum(char == 'A' and
               {words[y - 1][x - 1], words[y + 1][x + 1]} == {'M', 'S'} and
               {words[y - 1][x + 1], words[y + 1][x - 1]} == {'M', 'S'}
               for y, line in enumerate(words[1:-1], 1)
               for x, char in enumerate(line[1:-1], 1))


if __name__ == '__main__':
    main()
