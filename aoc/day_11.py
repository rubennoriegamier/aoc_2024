from functools import cache


def main():
    stones = list(map(int, input().split()))

    print(part_1(25, stones))
    print(part_1(75, stones))


def part_1(blinks: int, stones: list[int]) -> int:
    @cache
    def blink(left_blinks: int, stone: int) -> int:
        if left_blinks == 0:
            return 1
        if stone == 0:
            return blink(left_blinks - 1, 1)
        if len(stone_as_str := str(stone)) % 2 == 0:
            return blink(left_blinks - 1, int(stone_as_str[:len(stone_as_str) // 2])) + \
                blink(left_blinks - 1, int(stone_as_str[len(stone_as_str) // 2:]))
        return blink(left_blinks - 1, stone * 2024)

    return sum(blink(blinks, stone) for stone in stones)


if __name__ == '__main__':
    main()
