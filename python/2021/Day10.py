import sys
from common import DataAnalyzer

def missteps(direction):
    if len(direction) > 1:
        return 0
    
    map = {')': 3, ']': 57, '}': 1197, '>': 25137}

    if direction in map.keys():
        return map[direction]
    
    return 0

def incomplete(directions):
    total = 0
    if hasattr(directions, "__len__") and not isinstance(directions, str):
        terminals = ['x', '(', '[', '{', '<']
        directions.reverse()
        for d in directions:
            total = (5 * total) + terminals.index(d)
    
    return total

def median(totals):
    import statistics
    totals = [i for i in totals if i != 0]
    return statistics.median(totals)

def parse(directions, scorer=missteps, overall=sum):
    totals = []
    for d in directions:
        totals.append(scorer(traverse(d)))
    
    return overall(totals)

def traverse(route):
    start = ['[', '{', '<', '(']
    path = []

    def end_check(c):
        if c == ')' and path[-1] == '(':
            return True
        if c == '}' and path[-1] == '{':
            return True
        if c == ']' and path[-1] == '[':
            return True
        if c == '>' and path[-1] == '<':
            return True
        
        return False

    for r in route:
        if r in start:
            path.append(r)
        elif end_check(r):
            path.pop()
        else:
            return r
    
    return path


def second():
    values = DataAnalyzer.text("2021/day10.txt")
    print(f"(10.2) 2021 Syntax Score => {parse(values, scorer=incomplete, overall=median)}")

def first():
    values = DataAnalyzer.text("2021/day10.txt")
    print(f"(10.1) 2021 Syntax Score => {parse(values)}")


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
