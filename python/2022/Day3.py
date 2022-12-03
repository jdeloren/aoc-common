import sys
from common import DataAnalyzer

input = DataAnalyzer.text("2022/day3.txt")

priorities = [s for s in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
sums = lambda items: sum([priorities.index(i)+1 for i in items])

def prioritize(sacks, score=sums):
    commons = []
    for sack in sacks:
        a,b = sack[:int(len(sack)/2)], sack[int(len(sack)/2):]
        commons.extend(list(set(a).intersection(b)))

    return score(commons)

def triplicate(sacks, score=sums):
    commons = []
    for a, b, c in zip(*[iter(sacks)]*3):
        commons.extend(list(set(a).intersection(b).intersection(c)))

    return score(commons)

def second():
    print(f"(2022 3.2) group priority score => {triplicate(input)}")

def first():
    print(f"(2022 3.1) priority score => {prioritize(input)}")


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
