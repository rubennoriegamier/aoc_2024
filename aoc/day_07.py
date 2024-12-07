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
        operands = deque([self._operands[0]])

        for operand_a in self._operands[1:]:
            for _ in range(len(operands)):
                operand_b = operands.popleft()

                if (operand_c := operand_a + operand_b) <= self._result:
                    operands.append(operand_c)
                if (operand_c := operand_a * operand_b) <= self._result:
                    operands.append(operand_c)

        return any(map(partial(eq, self._result), operands))

    def part_2(self) -> bool:
        operands = deque([self._operands[0]])

        for operand_a in self._operands[1:]:
            for _ in range(len(operands)):
                operand_b = operands.popleft()

                if (operand_c := operand_a + operand_b) <= self._result:
                    operands.append(operand_c)
                if (operand_c := operand_a * operand_b) <= self._result:
                    operands.append(operand_c)
                    if (operand_c := int(f'{operand_b}{operand_a}')) <= self._result:
                        operands.append(operand_c)

        return any(map(partial(eq, self._result), operands))


def part_1(equations: Iterable[Equation]) -> int:
    # noinspection PyTypeChecker
    return sum(map(attrgetter('result'), filter(Equation.part_1, equations)))


def part_2(equations: Iterable[Equation]) -> int:
    # noinspection PyTypeChecker
    return sum(map(attrgetter('result'), filter(Equation.part_2, equations)))


if __name__ == '__main__':
    main()
