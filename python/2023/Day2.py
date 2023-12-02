import sys, re, math
from typing import List
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2023/day2.txt")

test_data = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

def power(data: List[str]):
    power = 0
    for d in data:
        bag = {'red': 0, 'green': 0, 'blue': 0}
        for num, col in re.findall(r'(\d+) (\w+)', d):
            bag[col] = max(bag[col], int(num))
        power += math.prod(bag.values())

    return power

def counter(data: List[str]):
    config = {'red': 12, 'green': 13, 'blue': 14}
    games = []

    for d in data:
        meta = d.split(':')
        valid = True        

        for num, col in re.findall(r'(\d+) (\w+)', d):
            if max(config[col], int(num)) != config[col]:
                valid = False

        if valid:
            games.append(int(meta[0].split()[1]))
    
    return sum(games)

def second():
    print(f"(2023 2.0) score => {power(test_data)}")
    print(f"(2023 2.1) score => {power(input)}")

def first():
    print(f"(2023 1.0) score => {counter(test_data)}")
    print(f"(2023 1.1) score => {counter(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
