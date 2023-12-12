import sys
from typing import Dict, List
from common import Solver, DataAnalyzer


test_data = [
    'RL',
    '',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)'
]

more_test_data = [
    'LLR',
    '',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)'
]

even_more_test_data = [
    'LR',
    '',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)'
]


def read(data, mapper=lambda x: x.isalpha()):
    map: Dict[str, str] = {}
    get_node = lambda x: ''.join([l for l in x if mapper(l)])

    for d in data[2:]:
        map[d.split('=')[0].strip()] = [get_node(n) for n in d.split('=')[1].split(',')]

    return [0 if d == 'L' else 1 for d in data[0]], map

def ghost(data: List[str]):
    path, map = read(data, mapper=lambda x: x.isalpha() or x.isdigit())
    start = [node for node in map.keys() if node.endswith('A')]
    multiples = []

    for node in start:
        index = 0
        steps = 1
        current = map[node][path[index]]
        while not current.endswith('Z'):
            index = index + 1 if index < len(path) - 1 else 0
            current = map[current][path[index]]
            steps += 1
        
        multiples.append(steps)

    import math
    return math.lcm(*multiples)


def travel(data: List[str], start='AAA', end='ZZZ'):
    path, map = read(data)
    steps = 0

    current = start
    while current != 'ZZZ':
        steps += len(path)
        for step in path:
            current = map[current][step]

    return steps

def second():
    print(f"(2023 8.2) steps => {ghost(even_more_test_data)}")
    print(f"(2023 8.2) steps => {ghost(input)}")

def first():
    print(f"(2023 8.1) steps => {travel(test_data)}")
    print(f"(2023 8.1) steps => {travel(more_test_data)}")
    print(f"(2023 8.1) steps => {travel(input)}")

if __name__ == '__main__':
    input = DataAnalyzer.text("2023/day8.txt")
    Solver.solve(sys.argv[1], first, second)
