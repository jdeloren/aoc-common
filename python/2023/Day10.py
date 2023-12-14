import sys
import numpy

from dataclasses import dataclass
from typing import List
from common import Solver, DataAnalyzer


test_data = [
    '..F7.',
    '.FJ|.',
    'SJ.L7',
    '|F--J',
    'LJ...'
]

more_test_data = [
'FF7FSF7F7F7F7F7F---7',
'L|LJ||||||||||||F--J',
'FL-7LJLJ||||||LJL-77',
'F--JF--7||LJLJ7F7FJ-',
'L---JF-JLJ.||-FJLJJ7',
'|F|F-JF---7F7-L7L|7|',
'|FFJF7L7F-JF7|JL---7',
'7-L-JL7||F7|L7F-7F7|',
'L.L7LFJ|||||FJL7||LJ',
'L7JLJL-JLJLJL--JLJ.L'
]

@dataclass
class Loop:
    direction: int
    path: List[int]

    def active(self, start):
        return self.path[-1] != start
    
    def track(self, world):
        return [(world[p[0]][p[1]]) for p in self.path]


def pipes(data):
    world = []
    for subworld in data:
        world.append(list(subworld))

    start = numpy.where(numpy.array(world) == 'S')
    return (start[0][0], start[1][0]), world

def run(world: List[List], spot: tuple, direction: int):
    def step(spot, direction):
        match direction:
            case 0:
                return (spot[0]-1, spot[1])
            case 1:
                return (spot[0], spot[1]+1)
            case 2:
                return (spot[0]+1, spot[1])
            case 3:
                return (spot[0], spot[1]-1)

    match world[spot[0]][spot[1]]:
        case '|':
            new = 0 if direction == 0 else 2
        case '-':
            new = 1 if direction == 1 else 3
        case 'F':
            new = 2 if direction == 3 else 1
        case '7':
            new = 2 if direction == 1 else 3
        case 'L':
            new = 1 if direction == 2 else 0
        case 'J':
            new = 3 if direction == 2 else 0
        case _:
            print(f'Illegal path?: {spot}:{world[spot[0]][spot[1]]}, {direction}')
            exit('-1')
    
    return step(spot, new), new

def path(start, world):
    loops: List[Loop] = []

    if start[0] > 0 and world[start[0]-1][start[1]] in ['|', 'F', '7']:
        loops.append(Loop(0, [(start[0]-1, start[1])]))
    if start[1] > 0 and world[start[0]][start[1]-1] in ['-', 'L', 'J']:
        loops.append(Loop(3, [(start[0], start[1]-1)]))
    if start[1] < len(world[0]) and world[start[0]][start[1]+1] in ['-', '7', 'J']:
        loops.append(Loop(1, [(start[0], start[1]+1)]))
    if start[0] < len(world[0]) and world[start[0]+1][start[1]] in ['|', 'F', 'L']:
        loops.append(Loop(2, [(start[0]+1, start[1])]))
    
    for _, loop in enumerate(loops):
        while loop.active(start):
            node, direction = run(world, loop.path[-1], loop.direction)
            loop.path.append(node)
            loop.direction = direction

    return max([loop.path for loop in loops], key=len)

def midpoint(data):
    start, world = pipes(data)
    return len(path(start, world)) // 2

def is_inside(data):
    from shapely.geometry import Polygon, Point

    start, world = pipes(data)
    track = path(start, world)
    poly = Polygon(track)
    xs = [t[0] for t in track]
    ys = [t[1] for t in track]
    return len([[i, j] for i in range(min(xs), max(xs)) for j in range(min(ys), max(ys)) if poly.contains(Point(i, j))])


def second():
    print(f"(2023 10.2) inside count => {is_inside(more_test_data)}")
    print(f"(2023 10.2) inside count => {is_inside(input)}")

def first():
    print(f"(2023 10.1) steps => {midpoint(test_data)}")
    print(f"(2023 10.1) steps => {midpoint(input)}")

if __name__ == '__main__':
    input = DataAnalyzer.text("2023/day10.txt")
    Solver.solve(sys.argv[1], first, second)
