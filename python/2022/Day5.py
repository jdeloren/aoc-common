import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day5.txt")

def pop(list, count):
    items = list[:count]
    del list[:count]
    return items

def arrange(data, reverse=True):
    instructions = False
    crates = []
    moves = []

    # build crates
    for i in range(int(len(data[0]) / 4)+1):
        crates.append([])    

    for row in data:
        if not instructions:
            if len(row) == 0:
                instructions = True
            elif not row.startswith(' 1'):
                for i in range(0, int(len(row)/4)+1):
                    crates[i] += row[i*4+1] if row[i*4+1] != ' ' else []
        else:
            moves.append(row)
    
    # start moves
    for move in moves:
        steps = move.split(' ')
        boxes = pop(crates[int(steps[3])-1], int(steps[1]))
        if reverse:
            boxes.reverse()
        crates[int(steps[5])-1][:0] = boxes

    return ''.join([c[0] for c in crates])

def second():
    print(f"(2022 5.2) top crates CM9001 => {arrange(input, False)}")

def first():
    print(f"(2022 5.1) top crates CM9000 => {arrange(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
