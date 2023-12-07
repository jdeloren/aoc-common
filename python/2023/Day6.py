import sys, math
from typing import List
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2023/day6.txt")

test_data = [
'Time:      7  15   30',
'Distance:  9  40  200'
]


def race(t: int, d: int):
    return sum(map(lambda x: 1 if x * (t - x) > d else 0, range(t)))

def parse(data: List[str]) -> int:
    return math.prod(map(race, [int(t) for t in data[0].split(':')[1].split()], [int(d) for d in data[1].split(':')[1].split()]))

def long_parse(data: List[str]) -> int:
    return race(int(''.join(data[0].split(':')[1].split())), int(''.join(data[1].split(':')[1].split())))

def second():
    print(f"(2023 6.2) score => {long_parse(test_data)}")
    print(f"(2023 6.2) score => {long_parse(input)}")

def first():
    print(f"(2023 6.1) score => {parse(test_data)}")
    print(f"(2023 6.1) score => {parse(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
