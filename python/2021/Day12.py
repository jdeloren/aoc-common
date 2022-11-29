import sys
from common import DataAnalyzer


def dig(map):
    networks = []
    for m in map:
        networks.append(m.split('-'))
    
    return networks

def unique(list):
    import numpy as np
    temp = np.array(list, dtype=object)
    return np.unique(temp)

def explore(input, START='start', END='end', smalls=1):
    caves = dig(input)
    paths = []

    def walk(path):
        def small_route_check(path, max=2):
            from collections import Counter
            counts = Counter(path)
            duplicates = 0

            for k, v in zip(counts.keys(), counts.values()):
                if k.islower():
                    if v > max:
                        return False
                    if k != START and v > 1:
                        duplicates += 1
            
            return duplicates < smalls

        def valid(path, cave):
            return False if cave.islower() and not small_route_check(path+[cave]) else True

        def traverse(path, step):
            if step == END:
                paths.append(path + [step])
            elif valid(path, step):
                walk(path + [step])

        for x, y in caves:
            if x == path[-1] and y != START:
                traverse(path, y)
            elif y == path[-1] and x != START:
                traverse(path, x)

        return path

    for x, y in caves:
        if x == START:
            walk([x])
        if y == START:
            walk([y])
    
    return unique(paths)

def second():
    input = DataAnalyzer.text("2021/day12.txt")
    print(f"(12.2) paths => {len(explore(input, smalls=2))}")

def first():
    input = DataAnalyzer.text("2021/day12.txt")
    print(f"(12.1) paths => {len(explore(input))}")


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
