import sys
from common import DataAnalyzer

input = DataAnalyzer.text("2022/day1.txt")

def most(menu):
    indices = [n for n, item in enumerate(menu, start=1) if item == max(menu)]
    return indices, menu[indices[0]-1]

def top(menu, count=3):
    return sum(sorted(menu, reverse=True)[:count])

def count(data, counter=most):
    from itertools import groupby
    elves = [list(g) for k, g in groupby(data, key=bool) if k]
    elves = [sum([int(i) for i in e]) for e in elves]
    
    return counter(elves)

def second():
    print(f"(2022 1.2) calorie group counter => {count(input, top)}")

def first():
    print(f"(2022 1.1) calorie counter => {count(input)}")


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()


if __name__ == '__main__':
    solve(sys.argv[1])
