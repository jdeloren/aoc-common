
import sys
from typing import List
from common import Solver, DataAnalyzer

test_data = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45'
]


def build_stack(data) -> List[List[int]]:
    stack = [[int(d) for d in data.split()]]
    diffs = [stack[0][i+1] - stack[0][i] for i in range(len(stack[0]) - 1)]
    stack.append(diffs.copy())

    while not all(i == 0 for i in diffs):
        diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs) - 1)]
        stack.append(diffs.copy())

    return stack

def subs(data: List[str]) -> int:
    stack = build_stack(data)
    stack[-1].append(0)
    [row.insert(0, row[0] - stack[-1 * (i+1)][0]) for i, row in enumerate(reversed(stack[:-1]))]
    return stack[0][0]

def sums(data: List[str]) -> int:
    stack = build_stack(data)
    stack[-1].append(0)
    [row.append(row[-1] + stack[-1 * (i+1)][-1]) for i, row in enumerate(reversed(stack[:-1]))]
    return stack[0][-1]

def second():
    print(f"(2023 9.2) sub => {sum(map(subs, test_data))}")
    print(f"(2023 9.2) sub => {sum(map(subs, input))}")

def first():
    print(f"(2023 9.1) sum => {sum(map(sums, test_data))}")
    print(f"(2023 9.1) sum => {sum(map(sums, input))}")

if __name__ == '__main__':
    input = DataAnalyzer.text("2023/day9.txt")
    Solver.solve(sys.argv[1], first, second)
