import sys
from common import DataAnalyzer


def checker(total, subset, index):
    s2 = subset.copy()
    return total - s2.pop(index) in s2


def hackXMAS(data, preamble=5):
    built[]
    for i in range(preamble, len(data)):
        total = data[i]
        found = False
        for j in range(i-preamble, i):
            if checker(total, data[i-preamble:i], j):
                found = True
                break
        
        if not found:
            return i

    return -1

def second():
    pass
    

def first():
    print("(9.1) program execution")
    data = DataAnalyzer.ints("2020/day9.txt")
    data = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
    hackXMAS(data)


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
