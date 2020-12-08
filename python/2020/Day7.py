import sys
from common import DataAnalyzer


def split(word): 
    return [c for c in word]  


def audit_unique(data):
    answers = 0
    master = data.pop(0)

    for str in data:
        master = ''.join(list(set(split(master)) & set(split(str))))

    return len(master)


def audit_sum(data):
    big = ''
    for str in data:
        big += str
    
    return len(''.join(set(big)))


def questions(data, func=audit_sum):
    docket = []
    sum = 0

    for str in data:
        if not str:
            sum += func(docket)
            docket = []
        else:
            docket.append(str)
        
    return sum + func(docket)


def second():
    data = DataAnalyzer.text("2020/day6.txt")
    print("(6.2) question count: {:d}".format(questions(data, audit_unique)))


def first():
    data = DataAnalyzer.text("2020/day6.txt")
    print("(6.1) question count: {:d}".format(questions(data)))


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
