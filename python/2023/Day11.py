import sys
from common import Solver, DataAnalyzer
import numpy as np

test_data = [
'...#......',
'.......#..',
'#.........',
'..........',
'......#...',
'.#........',
'.........#',
'..........',
'.......#..',
'#...#.....'
]


def ptolemy(data, age=1):
    distance = lambda a, b, c, d: \
        abs(c-a) + \
        abs(b-d) + \
        max(1, age-1) * (len(set(range(min(a,c), max(a,c))) & empty_rows) + len(set(range(min(b,d), max(b,d))) & empty_cols))

    universe = np.array([list(d) for d in data])
    empty_rows = set([i for i, row in enumerate(universe) if all(c == '.' for c in row)])
    empty_cols = set([j for j in range(universe.shape[1]) if all(c == '.' for c in universe[:, j])])

    galaxies = np.where(universe == '#')
    galaxies = [(g1,g2) for g1,g2 in zip(galaxies[0], galaxies[1])]
    
    return sum([distance(g1[0], g1[1], g2[0], g2[1]) for i, g1 in enumerate(galaxies) for g2 in galaxies[i+1:]])
    

def second():
    print(f"(2023 11.2) galactic distance => {ptolemy(test_data, 10)}")
    print(f"(2023 11.2) galactic distance => {ptolemy(test_data, 100)}")
    print(f"(2023 11.2) galactic distance => {ptolemy(input, 1000000)}")

def first():
    print(f"(2023 11.1) galactic distance => {ptolemy(test_data)}")
    print(f"(2023 11.1) galactic distance => {ptolemy(input)}")

if __name__ == '__main__':
    input = DataAnalyzer.text("2023/day11.txt")
    Solver.solve(sys.argv[1], first, second)
