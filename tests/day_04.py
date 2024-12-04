from aoc.day_04 import part_1, part_2


def test_part_1():
    assert part_1(['MMMSXXMASM',
                   'MSAMXMSMSA',
                   'AMXSXMAAMM',
                   'MSAMASMSMX',
                   'XMASAMXAMM',
                   'XXAMMXXAMA',
                   'SMSMSASXSS',
                   'SAXAMASAAA',
                   'MAMMMXMMMM',
                   'MXMXAXMASX']) == 18


def test_part_2():
    assert part_2(['MMMSXXMASM',
                   'MSAMXMSMSA',
                   'AMXSXMAAMM',
                   'MSAMASMSMX',
                   'XMASAMXAMM',
                   'XXAMMXXAMA',
                   'SMSMSASXSS',
                   'SAXAMASAAA',
                   'MAMMMXMMMM',
                   'MXMXAXMASX']) == 9
