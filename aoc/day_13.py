import fileinput
from operator import methodcaller
from typing import NamedTuple, Self

import numpy as np


def main():
    games = list(map(Game.parse, ''.join(fileinput.input()).split('\n\n')))

    print(part_1(games))
    print(part_2(games))


class Button(NamedTuple):
    x: int
    y: int

    @classmethod
    def parse(cls, raw_button: str) -> Self:
        return cls(*(int(part.split('+')[-1]) for part in raw_button.split(',')))


class Prize(NamedTuple):
    x: int
    y: int

    @classmethod
    def parse(cls, raw_prize: str) -> Self:
        return cls(*(int(part.split('=')[-1]) for part in raw_prize.split(',')))


class Game(NamedTuple):
    a: Button
    b: Button
    prize: Prize

    @classmethod
    def parse(cls, raw_game: str) -> Self:
        raw_a, raw_b, raw_prize = raw_game.splitlines()

        return cls(Button.parse(raw_a), Button.parse(raw_b), Prize.parse(raw_prize))

    def play(self, prize_offset: int = 0) -> int | None:
        a, b = map(round, np.linalg.solve(np.array([[self.a.x, self.b.x], [self.a.y, self.b.y]]),
                                          np.array([self.prize.x + prize_offset, self.prize.y + prize_offset])))

        if a * self.a.x + b * self.b.x == self.prize.x + prize_offset and \
                a * self.a.y + b * self.b.y == self.prize.y + prize_offset:
            return int(a * 3 + b)


def part_1(games: list[Game]) -> int:
    return sum(filter(None, map(methodcaller('play'), games)))


def part_2(games: list[Game]) -> int:
    return sum(filter(None, map(methodcaller('play', 10_000_000_000_000), games)))


if __name__ == '__main__':
    main()
