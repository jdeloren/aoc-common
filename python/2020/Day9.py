import sys
from common import DataAnalyzer


def weakness(data, index):
    total = data[index]
    for i in range(0, index):
        for j in range(i, index):
            if sum(data[i:j]) == total:
                return min(data[i:j]) + max(data[i:j])
    
    return -1


def checker(total, subset, index):
    s2 = subset.copy()
    return total - s2.pop(index) in s2


def hackXMAS(data, preamble=5):
    for i in range(preamble, len(data)):
        total = data[i]
        found = False
        for j in range(preamble):
            if checker(total, data[i-preamble:i], j):
                found = True
                break
        
        if not found:
            return i

    return -1

def second():
    data = DataAnalyzer.ints("2020/day9.txt")
    answer = hackXMAS(data, 25)
    print("(9.2) Attack vector: {:}".format(weakness(data, answer)))
    

def first():
    data = DataAnalyzer.ints("2020/day9.txt")
    answer = hackXMAS(data, 25)
    print("(9.1) Gap found at {:d} => {:d}".format(answer, data[answer]))


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
