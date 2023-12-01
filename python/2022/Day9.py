import sys
from common import DataAnalyzer, Solver

input = DataAnalyzer.text("2022/day9.txt")

test = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2'
]

t2 = [
    'R 5',
    'U 8',
    # 'L 8',
    # 'D 3',
    # 'R 17',
    # 'D 10',
    # 'L 25',
    # 'U 20'
]


def rope(moves, length=2):
    import math

    start = (0,0)
    rope = [(0,0) for _ in range(length)]
    positions = set((0,0))

    def trail(direction, distance, rope):
        print(f'MOVE {direction} {distance} HEAD={rope[0]} TAIL={rope[len(rope)-1]}')
        def tail_move(x, y, update):
            t = (x, y)
            if update:
                # print(f'\ttail positions: {positions}, tail={t}')
                positions.update([t])
            return t

        for d in range(distance):
            if direction == 'L':
                rope[0] = (rope[0][0]-1, rope[0][1])
            elif direction == 'R':
                rope[0] = (rope[0][0]+1, rope[0][1])
            elif direction == 'U':
                rope[0] = (rope[0][0], rope[0][1]+1)
            elif direction == 'D':
                rope[0] = (rope[0][0], rope[0][1]-1)
            
            print(f'\tSTEPPING {rope}')

            for i in range(1, len(rope)):
                # print(f'\tDIST({i}): {math.dist(rope[i], rope[i-1])} HEAD={rope[0]} T1={rope[i]} T2={rope[i-1]}')
                if math.dist(rope[i], rope[i-1]) >= 2.0:
                    print(f'\t\t..MOVED {rope[i]} {rope[i-1]} {math.dist(rope[i], rope[i-1])}')
                    if d > 0:
                        # print(f'\t\t..V CHECK??: {rope[i][0]} {rope[i-1][0]}')
                        if rope[i][0] == rope[i-1][0]:
                            direction = 'D' if rope[i][1] < rope[i-1][1] else 'U'
                            print(f'\t\t\t..VERTICAL ADJUST: {direction}')
                        # print(f'\t\t..H CHECK??: {rope[i][1]} {rope[i-1][1]}')
                        if rope[i][1] == rope[i-1][1]:
                            direction = 'L' if rope[i][1] < rope[i-1][1] else 'R'
                            print(f'\t\t\t..HORIZONTAL ADJUST: {direction}')

                    if direction == 'L':
                        rope[i] = tail_move(rope[i-1][0]+1, rope[i-1][1], i==len(rope)-1)
                    elif direction == 'R':
                        rope[i] = tail_move(rope[i-1][0]-1, rope[i-1][1], i==len(rope)-1)
                    elif direction == 'U':
                        rope[i] = tail_move(rope[i-1][0], rope[i-1][1]-1, i==len(rope)-1)
                    elif direction == 'D':
                        rope[i] = tail_move(rope[i-1][0], rope[i-1][1]+1, i==len(rope)-1)
            
            print(f'\tSTEPPED {rope}')

        return rope


    for move in moves:
        direction = move.split(' ')
        rope = trail(direction[0], int(direction[1]), rope)
    
    return positions

def second():
    print(f"(2022 9.2) # of tail positions (10 knots) => {len(rope(t2, 10))}")

def first():
    # 6563
    print(f"(2022 9.1) # of tail positions (2 knots) => {len(rope(input))}")

if __name__ == '__main__':
    Solver.solve(sys.argv[1], first, second)
