import sys
from common import DataAnalyzer

def navigate(data, prefix='', waypoint=None):
    location = [0, 0]
    beacon = waypoint.copy()
    orientation = 1

    def traverse(n, steps):
        location[n] += steps
    
    def step(direction, steps):
        stepper = {
            0: lambda: traverse(0, steps),
            1: lambda: traverse(1, steps),
            2: lambda: traverse(0, -1 * steps),
            3: lambda: traverse(1, -1 * steps),
        }.get(direction, lambda: None)()

    for i in range(len(data)):
        direction = data[i][0]
        steps = int(''.join(data[i][1:]))

        if direction == 'F':
            step(orientation, steps)
        if direction == 'N':
            step(0, steps)
        elif direction == 'S':
            step(1, steps)
        elif direction == 'E':
            step(2, steps)
        elif direction == 'W':
            step(3, steps)
        elif direction == 'L':
            orientation = int(orientation - steps / 90) % 4
        elif direction == 'R':
            orientation = int(orientation + steps / 90) % 4
        
    print("{:s} N/E: {:d} {:d} => {:d}".format(prefix, location[0], location[1], abs(location[0]) + abs(location[1])))


def second():
    data = ['F10','N3','F7','R90','F11',]
    navigate(data, '(12.1.0)', [1, 10])
    data = DataAnalyzer.text("2020/day12.txt")
    pass


def first():
    data = ['F10','N3','F7','R90','F11',]
    navigate(data, '(12.1.0)')
    data = DataAnalyzer.text("2020/day12.txt")
    navigate(data, '(12.1)')
    pass


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
