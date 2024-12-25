import fileinput
from functools import cache
from itertools import islice
from operator import and_, methodcaller, or_, xor
from typing import Callable

OPERATORS = {'AND': and_,
             'OR': or_,
             'XOR': xor}


def main():
    raw_inputs, raw_gates = ''.join(fileinput.input()).split('\n\n')
    inputs = parse_inputs(raw_inputs)
    gates = parse_gates(raw_gates)

    print(part_1(inputs, gates))
    print(part_2(inputs, gates))


def parse_inputs(raw_inputs: str) -> dict[str, bool]:
    return {bit: is_set == '1'
            for bit, is_set in map(methodcaller('split', ': '), raw_inputs.splitlines())}


def parse_gates(raw_gates: str) -> dict[str, tuple[str, Callable[[bool, bool], bool], str]]:
    return {o: (i_1, OPERATORS[op], i_2)
            for i_1, op, i_2, _, o in map(str.split, raw_gates.splitlines())}


def part_1(inputs: dict[str, bool], gates: dict[str, tuple[str, Callable[[bool, bool], bool], str]]) -> int:
    @cache
    def get_value(wire_: str) -> bool:
        value = inputs.get(wire_)

        if value is None:
            i_1, op, i_2 = gates[wire_]

            return op(get_value(i_1), get_value(i_2))
        else:
            return value

    return sum(get_value(wire) * 2 ** int(wire[1:])
               for wire in gates
               if wire[0] == 'z')


def part_2(inputs: dict[str, bool], gates: dict[str, tuple[str, Callable[[bool, bool], bool], str]]) -> str:
    gates = gates.copy()
    x = 0
    y = 0

    for bit, is_set in inputs.items():
        if bit[0] == 'x':
            x += is_set * 2 ** int(bit[1:])
        else:
            y += is_set * 2 ** int(bit[1:])

    pairs = {}

    for wire, (_, op, __) in gates.items():
        if wire[0] == 'z' and op is not xor:
            pairs[wire] = None

    for wire, (i_1, op, i_2) in gates.items():
        if wire[0] != 'z' and i_1[0] not in 'xy' and op is xor:
            if gates[i_1][0][0] in 'xy':
                pairs[f'z{gates[i_1][0][1:]}'] = wire
            elif gates[i_2][0][0] in 'xy':
                pairs[f'z{gates[i_2][0][1:]}'] = wire

    result = set()

    for wire_1, wire_2 in pairs.items():
        if wire_2 is not None:
            gates[wire_1], gates[wire_2] = gates[wire_2], gates[wire_1]
            result.add(wire_1)
            result.add(wire_2)

    wires = [wire for wire in gates if wire not in result]

    @cache
    def get_path(wire_: str) -> set[str]:
        i_1_, op_, i_2_ = gates[wire_]
        path = set()
        if i_1_[0] not in 'xy':
            path.add(i_1_)
            path.add(i_2_)
            path.update(get_path(i_1_))
            path.update(get_path(i_2_))
        return path

    for i, wire_1 in enumerate(wires):
        for wire_2 in islice(wires, i + 1, None):
            if wire_1 not in get_path(wire_2) and wire_2 not in get_path(wire_1):
                gates[wire_1], gates[wire_2] = gates[wire_2], gates[wire_1]
                if part_1(inputs, gates) == x + y:
                    inputs_ = {bit: False if is_set else True for bit, is_set in inputs.items()}
                    x_ = 0
                    y_ = 0

                    for bit, is_set in inputs_.items():
                        if bit[0] == 'x':
                            x_ += is_set * 2 ** int(bit[1:])
                        else:
                            y_ += is_set * 2 ** int(bit[1:])
                    if part_1(inputs_, gates) == x_ + y_:
                        result.add(wire_1)
                        result.add(wire_2)

                        return ','.join(sorted(result))
                gates[wire_1], gates[wire_2] = gates[wire_2], gates[wire_1]


if __name__ == '__main__':
    main()
