import sys, itertools
import numpy as np
from common import Solver, DataAnalyzer

input = DataAnalyzer.text("2023/day13.txt")

test_data = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.',
    '',
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#'
]


def summarize_reflections(data, smudges):
    def check_reflections(mirror: np.ndarray):
        def directional_reflection_check(shape_index, multiplier) -> int:
            for i in range(mirror.shape[shape_index]):
                offset = 0
                differences = 0
                pure = True

                while i - offset >= 0 and i + offset + 1 < mirror.shape[shape_index]:
                    one = mirror[i-offset, None] if shape_index == 0 else mirror[:, i-offset]
                    two = mirror[i+offset+1, None] if shape_index == 0 else mirror[:, i+offset+1]
                    differences += np.sum(np.not_equal(one, two))

                    if (smudges and differences > 1) or (not smudges and not np.array_equal(one, two)):
                        pure = False
                        break
                    else:
                        offset += 1

                if pure and offset > 0 and not (smudges and differences == 0):
                    return multiplier * (i+1)

            return 0

        return directional_reflection_check(0, 100), directional_reflection_check(1, 1)


    black = [list(group) for k, group in itertools.groupby(data, lambda x: x == '') if not k]
    mirrors = [np.array([list(d) for d in b]) for b in black]

    total = 0
    for mirror in mirrors:
        horizontal, vertical = check_reflections(mirror)
        total += horizontal if horizontal > 0 else vertical

    return total

def second():
    print(f"(2023 13.2) sum => {summarize_reflections(test_data, True)}")
    print(f"(2023 13.2) sum => {summarize_reflections(input, True)}")

def first():
    print(f"(2023 13.1) sum => {summarize_reflections(test_data, False)}")
    print(f"(2023 13.1) sum => {summarize_reflections(input, False)}")


if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
