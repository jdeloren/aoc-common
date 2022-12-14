import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day10.txt")


def get_instructions(data):
    ins = []
    for d in data:
        s = d.split(' ')
        ins.append((s[0], 0 if len(s) == 1 else int(s[1])))
    
    return ins

def draw(data, cycles=40, end=240):
    def mprint(octopi):
        [print(''.join(map(str,v))) for v in octopi]
        print()

    crt = []
    instructions = get_instructions(data)
    counters = {'noop': 1, 'addx': 2}

    step = 0
    sprite = 1
    line = []
    for x in range(len(instructions)):
        for _ in range(counters[instructions[x][0]]):
            line.append('#' if abs((step % cycles) - sprite) < 2 else '.')
            step += 1
            if len(line) % cycles == 0:
                crt.append(line)
                line = []
        
        if step > end:
            break
        
        sprite += instructions[x][1]
    
    mprint(crt)
    return True

def cycle(data, steps=[20, 60, 100, 140, 180, 220]):    
    instructions = get_instructions(data)
    counters = {'noop': 1, 'addx': 2}
    register = 1
    values = []

    step = 0
    for x in range(len(instructions)):
        for _ in range(counters[instructions[x][0]]):
            step += 1
            if step in steps:
                values.append(step * register)
            
        if step > max(steps):
            break
        
        register += instructions[x][1]

    return sum(values)

def second():
    print(f"(2022 10.2) sprites => {draw(input)}")

def first():
    print(f"(2022 10.1) signal strength => {cycle(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
