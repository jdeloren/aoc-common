from audioop import reverse
import sys
from common import DataAnalyzer, Solver
import numpy as np

input = DataAnalyzer.text("2022/day8.txt")


def map(data):
    return np.array([[eval(d) for d in dd] for dd in [list([*dd]) for dd in data]])

def survey(data, scan=True):
    trees = map(data)

    def look(x, y, a, b, c, d, length=len(trees)-1):
        v = trees[x][y]
        return x == 0 or x == length or y == 0 or y==length or max(a) < v or max(b) < v or max(c) < v or max(d) < v

    def visibility(x, y, a, b, c, d):
        def match(height, treeline):
            return 0 if len(treeline) == 0 else next((i+1 for i, tree in enumerate(treeline) if tree >= height), len(treeline))
        
        return match(trees[x][y], list(reversed(a))) * match(trees[x][y], b) * match(trees[x][y], list(reversed(c))) * match(trees[x][y], d)

    def sight(x, y, scan=look):
        hor = list(trees[x])
        vrt = [v[-1] for v in trees[:,:y+1]]
        return scan(x, y, hor[:y], hor[y+1:], vrt[:x], vrt[x+1:])

    if scan:
        return [(x,y) for x in range(len(trees[0])) for y in range(len(trees)) if sight(x, y)]

    return [sight(x, y, visibility) for x in range(len(trees[0])) for y in range(len(trees))]


def second():
    print(f"(2022 8.2) top visibility score => {max(survey(input, False))}")

def first():
    print(f"(2022 8.1) # of visible trees => {len(survey(input))}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
