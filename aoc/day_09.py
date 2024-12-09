from itertools import chain, repeat, starmap
from operator import mul


def main():
    disk_map = list(map(int, input()))

    print(part_1(disk_map))
    print(part_2(disk_map))


def get_memory(disk_map: list[int]) -> list[int | None]:
    return list(chain.from_iterable(repeat(None, size) if i % 2 else repeat(i // 2, size)
                                    for i, size in enumerate(disk_map)))


def part_1(disk_map: list[int]) -> int:
    memory = get_memory(disk_map)

    for i, id_ in enumerate(memory):
        if id_ is None:
            memory[i] = memory.pop()
        while memory[-1] is None:
            del memory[-1]

    return sum(starmap(mul, enumerate(memory)))


def part_2(disk_map: list[int]) -> int:
    memory = []
    free = []
    files = []

    for i, size in enumerate(disk_map):
        if i % 2:
            free.append((len(memory), size))
            memory.extend(repeat(None, size))
        else:
            files.append(((len(memory), size), i // 2))
            memory.extend(repeat(i // 2, size))

    for (file_start, file_size), id_ in reversed(files):
        while free and file_start < free[-1][0]:
            del free[-1]
        for i, (free_start, free_size) in enumerate(free):
            if file_size <= free_size:
                memory[free_start:free_start + file_size] = memory[file_start:file_start + file_size]
                memory[file_start:file_start + file_size] = repeat(None, file_size)
                if file_size == free_size:
                    del free[i]
                else:
                    free[i] = free_start + file_size, free_size - file_size
                break

    return sum(i * id_ for i, id_ in enumerate(memory) if id_ is not None)


if __name__ == '__main__':
    main()
