import sys
from common import DataAnalyzer

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
        count += overlap(l1, l2, check) or overlap(l2, l1, check)

    return count

def second():
    print(f"(2022 4.2) partial overlaps => {assignments(input, any)}")

def first():
    print(f"(2022 4.1) full overlaps => {assignments(input)}")


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
