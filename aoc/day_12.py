import fileinput
from collections import Counter, defaultdict
from functools import partial
from itertools import chain, groupby, pairwise, starmap
from operator import itemgetter, lt, sub


def main():
    garden = list(map(str.rstrip, fileinput.input()))

    print(part_1(garden))
    print(part_2(garden))


def part_1(garden: list[str]) -> int:
    fences = Counter()
    regions = [[None for _ in range(len(garden[0]))] for _ in range(len(garden))]
    region = 0

    for y, line in enumerate(garden):
        for x, plant in enumerate(line):
            if regions[y][x] is None:
                plots = {(y, x)}

                while plots:
                    curr_y, curr_x = plots.pop()
                    regions[curr_y][curr_x] = region

                    for y_offset, x_offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if 0 <= (neigh_y := curr_y + y_offset) < len(garden) and \
                                0 <= (neigh_x := curr_x + x_offset) < len(garden[0]):
                            if garden[neigh_y][neigh_x] == plant:
                                if regions[neigh_y][neigh_x] is None:
                                    plots.add((neigh_y, neigh_x))
                            else:
                                fences[region] += 1
                        else:
                            fences[region] += 1

                region += 1

    return sum(size * fences[region]
               for region, size in Counter(chain.from_iterable(regions)).items())


# noinspection PyTypeChecker
def part_2(garden: list[str]) -> int:
    fences = defaultdict(list)
    regions = [[None for _ in range(len(garden[0]))] for _ in range(len(garden))]
    region = 0

    for y, line in enumerate(garden):
        for x, plant in enumerate(line):
            if regions[y][x] is None:
                plots = {(y, x)}

                while plots:
                    curr_y, curr_x = plots.pop()
                    regions[curr_y][curr_x] = region

                    for y_offset, x_offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if 0 <= (neigh_y := curr_y + y_offset) < len(garden) and \
                                0 <= (neigh_x := curr_x + x_offset) < len(garden[0]):
                            if garden[neigh_y][neigh_x] == plant:
                                if regions[neigh_y][neigh_x] is None:
                                    plots.add((neigh_y, neigh_x))
                            else:
                                fences[region, y_offset, x_offset].append((curr_y, curr_x))
                        else:
                            fences[region, y_offset, x_offset].append((curr_y, curr_x))

                region += 1

    regions = Counter(chain.from_iterable(regions))
    result = 0

    for (region, y_offset, x_offset), plots in fences.items():
        if y_offset:
            plots.sort(key=itemgetter(0, 1), reverse=True)
            for groups in map(itemgetter(1), groupby(plots, key=itemgetter(0))):
                result += (sum(map(partial(lt, 1), starmap(sub, pairwise(map(itemgetter(1), groups))))) + 1) \
                          * regions[region]
        else:
            plots.sort(key=itemgetter(1, 0), reverse=True)
            for groups in map(itemgetter(1), groupby(plots, key=itemgetter(1))):
                result += (sum(map(partial(lt, 1), starmap(sub, pairwise(map(itemgetter(0), groups))))) + 1) \
                          * regions[region]

    return result


if __name__ == '__main__':
    main()
