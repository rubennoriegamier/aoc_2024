import fileinput
from operator import methodcaller
from typing import NamedTuple, Self

import z3


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
        a, b = z3.Ints('a b')
        solver = z3.Solver()

        solver.add(a * self.a.x + b * self.b.x == self.prize.x + prize_offset)
        solver.add(a * self.a.y + b * self.b.y == self.prize.y + prize_offset)

        if solver.check() == z3.sat:
            model = solver.model()

            return model[a].as_long() * 3 + model[b].as_long()


def part_1(games: list[Game]) -> int:
    return sum(filter(None, map(methodcaller('play'), games)))


def part_2(games: list[Game]) -> int:
    return sum(filter(None, map(methodcaller('play', 10_000_000_000_000), games)))


if __name__ == '__main__':
    main()
