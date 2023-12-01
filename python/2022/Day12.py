import sys
import numpy as np
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day12.txt")

test = [
    'Sabqponm',
    'abcryxxl',
    'accszExk',
    'acctuvwj',
    'abdefghi'
]

def track(data):
    plot = [x for x in "SabcdefghijklmnopqrstuvwxyzE"]
    indeces = {p: plot.index(p) for p in plot}

    def pprint(path):
        print(' > '.join([f'{map[point[0]][point[1]]}' for point in path]))

    def traverse(map, paths, deadzones=[], end='E'):
        def spot(x, y, path):
            try:
                step = indeces[map[x][y]] - indeces[map[path[-1][0], path[-1][1]]]
                # step = plot.index(map[x][y]) - plot.index(map[path[-1][0], path[-1][1]])
                return True if x > -1 and y > -1 and (x,y) not in deadzones and (x,y) not in path and step >= 0 and step < 2 else False
            except:
                return False
        
        extended = []
        dead = []

        def extender(path, x, y):
            return path[:] + [(x,y)]
        
        for path in paths:
            if map[path[-1][0]][path[-1][1]] == end or len(path) >= 80:
                break

            added = False
            if map[path[-1]] not in 'Sab' and spot(path[-1][0]-1, path[-1][1], path):
                added = True
                extended.append(extender(path, path[-1][0]-1, path[-1][1]))
            if spot(path[-1][0]+1, path[-1][1], path):
                added = True
                extended.append(extender(path, path[-1][0]+1, path[-1][1]))
            if spot(path[-1][0], path[-1][1]-1, path):
                added = True
                extended.append(extender(path, path[-1][0], path[-1][1]-1))
            if spot(path[-1][0], path[-1][1]+1, path):
                added = True
                extended.append(extender(path, path[-1][0], path[-1][1]+1))

            if not added:
                dead.append(path[-1])

        if len(dead) > 0:
            prune = []
            for path in paths:
                for p in path:
                    if p in deadzones:
                        prune.append(path)
                        break

            paths = [path for path in paths if path not in prune]
            deadzones.extend(dead)

        if len(extended) > 0:
            paths.extend(traverse(map, extended, deadzones, end))
            paths = [list(i) for i in set(tuple(i) for i in paths)]

        return paths

    # THIS WORKS
    map = np.array([list([*dd]) for dd in data])
    # start = tuple(n[0] for n in np.where(map == 'S'))
    # end = np.where(map == 'E')
    # end = [(m,n) for m,n in zip(end[0], end[1])]
    # paths = traverse(map, [[start]], end='E')
    # paths = [x for x in paths if x[-1] in end]
    # return len(min(paths, key=len)) - 1

    tokens = ['S', 'c', 'd', 'e', 'h', 'j', 'n', 'r', 'u', 'x']
    enders = tokens[:] + ['E']

    routes = []
    shortest = None
    for i, token in enumerate(tokens):
        start = tuple(n[0] for n in np.where(map == token)) if shortest == None else shortest[-1]
        print(f'STARTING AT {start} with {token}, ENDING at {enders[i+1]}')

        end = np.where(map == enders[i+1])
        end = [(m,n) for m,n in zip(end[0], end[1])]
        
        paths = traverse(map, [[start]], end=enders[i+1])
        paths = [x for x in paths if x[-1] in end]

        shortest = min(paths, key=len)
        routes.append(shortest)
        # print(f'\tENDING at {shortest[-1]} @ {map[shortest[-1]]}')

    return sum([len(x)-1 for x in routes])


def second():
    print(f"(2022 12.2) monkey business => {True}")

def first():
    print(f"(2022 12.1) minimal steps to summit => {track(input)}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
