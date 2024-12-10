import fileinput


def main():
    top_map = [list(map(int, line.rstrip())) for line in fileinput.input()]

    print(part_1(top_map))
    print(part_2(top_map))


def part_1(top_map: list[list[int]]) -> int:
    def move(y: int, x: int) -> set[tuple[int, int]]:
        if top_map[y][x] == 9:
            return {(y, x)}

        scores = set()

        if y > 0 and top_map[y - 1][x] - top_map[y][x] == 1:
            scores.update(move(y - 1, x))
        if y < len(top_map) - 1 and top_map[y + 1][x] - top_map[y][x] == 1:
            scores.update(move(y + 1, x))
        if x > 0 and top_map[y][x - 1] - top_map[y][x] == 1:
            scores.update(move(y, x - 1))
        if x < len(top_map[0]) - 1 and top_map[y][x + 1] - top_map[y][x] == 1:
            scores.update(move(y, x + 1))

        return scores

    return sum(len(move(y, x))
               for y in range(len(top_map))
               for x in range(len(top_map[0]))
               if top_map[y][x] == 0)


def part_2(top_map: list[list[int]]) -> int:
    def move(y: int, x: int) -> int:
        if top_map[y][x] == 9:
            return 1

        scores = 0

        if y > 0 and top_map[y - 1][x] - top_map[y][x] == 1:
            scores += move(y - 1, x)
        if y < len(top_map) - 1 and top_map[y + 1][x] - top_map[y][x] == 1:
            scores += move(y + 1, x)
        if x > 0 and top_map[y][x - 1] - top_map[y][x] == 1:
            scores += move(y, x - 1)
        if x < len(top_map[0]) - 1 and top_map[y][x + 1] - top_map[y][x] == 1:
            scores += move(y, x + 1)

        return scores

    return sum(move(y, x)
               for y in range(len(top_map))
               for x in range(len(top_map[0]))
               if top_map[y][x] == 0)


if __name__ == '__main__':
    main()
