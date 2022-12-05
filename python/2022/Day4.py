import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day4.txt")

def overlap(x, y, check=any):
    return 1 if check(item in x for item in y) or check(item in y for item in x) else 0

def assignments(data, check=all):
    count = 0

    for d in data:
        elves = d.split(',')
        r1 = [eval(i) for i in elves[0].split('-')]
        r2 = [eval(i) for i in elves[1].split('-')]
        l1 = list(range(r1[0], r1[1]+1))
        l2 = list(range(r2[0], r2[1]+1))
        count += overlap(l1, l2, check)

    return count

def second():
    print(f"(2022 4.2) partial overlaps => {assignments(input, any)}")

def first():
    print(f"(2022 4.1) full overlaps => {assignments(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
