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
        changes = [next_price - curr_price for curr_price, next_price in pairwise(prices)]
        prev_ids = set()

        id_ = changes[0] + 9 << 5 | changes[1] + 9 << 10 | changes[2] + 9 << 15

        for price, change in zip(islice(prices, 4, None), islice(changes, 3, None)):
            if (id_ := id_ >> 5 | change + 9 << 15) not in prev_ids:
                bananas[id_] += price
                prev_ids.add(id_)

    return bananas.most_common(1)[0][1]


if __name__ == '__main__':
    main()
