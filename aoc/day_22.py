import fileinput
from collections import Counter
from collections.abc import Generator
from itertools import islice, pairwise


def main():
    secret_numbers = list(map(int, fileinput.input()))

    print(part_1(secret_numbers))
    print(part_2(secret_numbers))


def next_secret_numbers(secret_number: int) -> Generator[int]:
    while True:
        yield secret_number

        secret_number = ((secret_number << 6) ^ secret_number) & 0b11111111_11111111_11111111
        secret_number = (secret_number >> 5) ^ secret_number
        secret_number = ((secret_number << 11) ^ secret_number) & 0b11111111_11111111_11111111


def part_1(secret_numbers: list[int]) -> int:
    return sum(next(islice(next_secret_numbers(secret_number), 2_000, None))
               for secret_number in secret_numbers)


def part_2(secret_numbers: list[int]) -> int:
    bananas = Counter()

    for secret_number in secret_numbers:
        prices = [int(str(secret_number)[-1])
                  for secret_number in islice(next_secret_numbers(secret_number), 2_001)]
        diffs = [next_price - curr_price for curr_price, next_price in pairwise(prices)]
        prev_changes = set()

        for i, price in enumerate(islice(prices, 4, None), 4):
            if (changes := tuple(diffs[i - 4:i])) not in prev_changes:
                bananas[changes] += price
                prev_changes.add(changes)

    return bananas.most_common(1)[0][1]


if __name__ == '__main__':
    main()
