import fileinput
from collections import deque
from collections.abc import Iterable
from functools import partial
from operator import eq, attrgetter
from typing import Self


def main():
    equations = list(map(Equation.parse, fileinput.input()))

    print(part_1(equations))
    print(part_2(equations))


class Equation:
    _result: int
    _operands: list[int]

    def __init__(self, result: int, operands: Iterable[int]):
        self._result = result
        self._operands = list(operands)

    @property
    def result(self) -> int:
        return self._result

    @classmethod
    def parse(cls, raw_equation: str) -> Self:
        raw_result, raw_operands = raw_equation.split(': ')

        return cls(int(raw_result), list(map(int, raw_operands.split())))

    def part_1(self) -> bool:
        operands = deque([self._result])

        for operand_a in self._operands[::-1]:
            for _ in range(len(operands)):
                operand_b = operands.popleft()

                if (operand_c := operand_b - operand_a) >= 0:
                    operands.append(operand_c)
                if (quotient_and_remainder := divmod(operand_b, operand_a))[1] == 0:
                    operands.append(quotient_and_remainder[0])

        return any(map(partial(eq, 0), operands))

    def part_2(self) -> bool:
        operands = deque([self._result])

        for operand_a in self._operands[::-1]:
            for _ in range(len(operands)):
                operand_b = operands.popleft()

                if (operand_c := operand_b - operand_a) >= 0:
                    operands.append(operand_c)
                if (quotient_and_remainder := divmod(operand_b, operand_a))[1] == 0:
                    operands.append(quotient_and_remainder[0])
                if 0 < len(operand_c := (operand_b := str(operand_b)).removesuffix(str(operand_a))) < len(operand_b):
                    operands.append(int(operand_c))

        return any(map(partial(eq, 0), operands))


def part_1(equations: Iterable[Equation]) -> int:
    # noinspection PyTypeChecker
    return sum(map(attrgetter('result'), filter(Equation.part_1, equations)))


def part_2(equations: Iterable[Equation]) -> int:
    # noinspection PyTypeChecker
    return sum(map(attrgetter('result'), filter(Equation.part_2, equations)))


if __name__ == '__main__':
    main()
